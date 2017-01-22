# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 10/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import uuid

from decimal import Decimal

from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy import asc
from sqlalchemy import desc
from sqlalchemy.orm import relationship
from extensions import db
from sqlalchemy.dialects.postgresql import JSON

from models.client import Client
from models.product import Product
from proj_exceptions import InvalidOrderStatusId
from r import R


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uuid = db.Column(db.String(R.dimen.uuid_length), nullable=False)
    client_email = db.Column(db.String(R.dimen.email_max_length), ForeignKey("client.email"), nullable=False)
    client = relationship("Client", back_populates="orders")
    status = db.Column(db.Enum(R.id), default=R.id.ORDER_STATUS_PAID, nullable=False)
    paid_datetime = db.Column(db.DateTime, nullable=False)
    sent_datetime = db.Column(db.DateTime)
    delivered_datetime = db.Column(db.DateTime)
    amount_by_product_id = db.Column(JSON, nullable=False)
    products_total_price = db.Column(db.Numeric(precision=12, scale=2), nullable=False)
    products_table_data = db.Column(db.JSON, nullable=False)
    total_table_data = db.Column(db.JSON, nullable=False)

    sort_method_ids = [
        R.id.SORT_METHOD_CLIENT_EMAIL,
        R.id.SORT_METHOD_NEWEST,
        R.id.SORT_METHOD_OLDER,
        R.id.SORT_METHOD_LOWER_TOTAL_PRICE,
        R.id.SORT_METHOD_HIGHER_TOTAL_PRICE
    ]
    sort_method_names = [
        R.string.client_email,
        R.string.newest,
        R.string.older,
        R.string.lowest_price,
        R.string.higher_price,
    ]
    sort_method_by_id = {
        R.id.SORT_METHOD_CLIENT_EMAIL: asc(client_email),
        R.id.SORT_METHOD_NEWEST: desc(paid_datetime),
        R.id.SORT_METHOD_OLDER: asc(paid_datetime),
        R.id.SORT_METHOD_LOWER_TOTAL_PRICE: asc(products_total_price),
        R.id.SORT_METHOD_HIGHER_TOTAL_PRICE: desc(products_total_price)
    }
    order_status_ids = [
        R.id.ORDER_STATUS_ANY,
        R.id.ORDER_STATUS_CANCELED,
        R.id.ORDER_STATUS_PAID,
        R.id.ORDER_STATUS_SENT,
        R.id.ORDER_STATUS_DELIVERED
    ]
    order_status_as_string_by_id = {
        R.id.ORDER_STATUS_ANY: R.string.any,
        R.id.ORDER_STATUS_CANCELED: R.string.canceled,
        R.id.ORDER_STATUS_PAID: R.string.paid,
        R.id.ORDER_STATUS_SENT: R.string.sent,
        R.id.ORDER_STATUS_DELIVERED: R.string.delivered
    }

    @staticmethod
    def create_new(**kwargs):
        order = Order(**kwargs)
        client = Client.get(order.client_email)
        assert client != None

        products_amounts_zip = order.get_products_amounts_zip()

        order.products_total_price = order._get_products_total_price(products_amounts_zip)
        order.products_table_data = order._get_products_table_data(products_amounts_zip)
        order.total_table_data = order._get_total_table_data(products_amounts_zip=products_amounts_zip, client=client)
        order.inc_products_reserved(products_amounts_zip)
        order.uuid = str(uuid.uuid4())

        db.session.add(order)
        db.session.commit()
        return order

    def get_products_amounts_zip(self):
        products = []
        amounts = []

        for product_id, amount in self.amount_by_product_id.iteritems():
            product = Product.get(product_id)
            products.append(product)
            amounts.append(amount)

        return zip(products, amounts)

    def inc_products_reserved(self, products_amounts_zip):
        for product, amount in products_amounts_zip:
            assert amount > 0
            assert product.available >= amount
            product.reserved += amount
            db.session.add(product)

    def get_status_as_string(self):
        return self.order_status_as_string_by_id[self.status]

    def get_formatted_paid_datetime(self):
        return R.string.formatted_datetime(self.paid_datetime)

    def get_formatted_sent_datetime(self):
        return R.string.formatted_datetime(self.sent_datetime)

    def get_formatted_delivered_datetime(self):
        return R.string.formatted_datetime(self.delivered_datetime)

    @staticmethod
    def get_choices():
        choices = []
        for order_status_id in Order.order_status_ids:
            choices.append((str(order_status_id.value), Order.order_status_as_string_by_id[order_status_id]))
        return choices

    @staticmethod
    def get(order_id):
        return Order.query.filter_by(id=order_id).one_or_none()

    @staticmethod
    def update(order_id, **kw):
        order = Order.get(order_id)
        assert order != None
        for key, val in kw.iteritems():
            setattr(order, key, val)
        db.session.add(order)
        db.session.commit()
        return order

    def _get_products_total_price(self, products_amounts_zip):
        products_total_price = Decimal("0.00")
        for product, amount in products_amounts_zip:
            products_total_price += product.get_price(n_units=amount)
        return products_total_price

    def _get_products_table_data(self, products_amounts_zip):
        rows = []
        for product, amount in products_amounts_zip:
            rows.append([
                "#" + str(product.id),
                product.title,
                product.get_formatted_price(),
                amount,
                product.get_formatted_price(n_units=amount)
            ])

        return dict(
            table_data=dict(
                id="products-table",
                cols=[
                    dict(
                        id="product-id",
                        title=R.string.id,
                        type=R.id.COL_TYPE_TEXT.value
                    ),
                    dict(
                        id="product-title",
                        title=R.string.product_title,
                        type=R.id.COL_TYPE_TEXT.value
                    ),
                    dict(
                        id="product-price",
                        title=R.string.price,
                        type=R.id.COL_TYPE_TEXT.value,
                        tooltip=R.string.product_price_tooltip
                    ),
                    dict(
                        id="product-amount",
                        title=R.string.amount,
                        type=R.id.COL_TYPE_TEXT.value
                    ),
                    dict(
                        id="product-subtotal",
                        title=R.string.subtotal,
                        type=R.id.COL_TYPE_TEXT.value,
                        tooltip=R.string.subtotal_tooltip
                    ),
                ],
                rows=rows
            )
        )

    def _get_total_table_data(self, products_amounts_zip, client):
        freight = client.get_freight()
        return dict(
            table_data=dict(
                no_head = True,
                bordered = True,
                classes="products-total-table",
                id="total-table",
                cols=[
                    dict(
                        type=R.id.COL_TYPE_TEXT.value
                    ),
                    dict(
                        type=R.id.COL_TYPE_TEXT.value,
                    )
                ],
                rows=[
                    [R.string.products, R.string.price_with_rs(self.products_total_price)],
                    [R.string.freight, R.string.price_with_rs(freight)],
                    [R.string.total, R.string.price_with_rs(self.products_total_price + freight)]
                ]
            )
        )

    def get_formatted_products_total_price(self):
        return str(self.products_total_price).replace(".", ",")

    def mark_as_sent(self):
        assert self.status == R.id.ORDER_STATUS_PAID
        self.status = R.id.ORDER_STATUS_SENT
        self.sent_datetime = datetime.now()

        for product, amount in self.get_products_amounts_zip():
            assert product.reserved >= amount
            assert product.stock >= amount
            product.reserved -= amount
            product.stock -= amount
            db.session.add(product)

        db.session.add(self)
        db.session.commit()

    def unmark_as_sent(self):
        assert self.status == R.id.ORDER_STATUS_SENT

        self.status=R.id.ORDER_STATUS_PAID
        self.sent_datetime=None

        for product, amount in self.get_products_amounts_zip():
            product.reserved += amount
            product.stock += amount
            db.session.add(product)

        db.session.add(self)
        db.session.commit()

    def mark_as_canceled(self):
        assert self.status == R.id.ORDER_STATUS_PAID

        self.status=R.id.ORDER_STATUS_CANCELED

        for product, amount in self.get_products_amounts_zip():
            product.reserved -= amount
            db.session.add(product)

        db.session.add(self)
        db.session.commit()

    def mark_as_paid(self):
        assert self.status == R.id.ORDER_STATUS_CANCELED

        self.status=R.id.ORDER_STATUS_PAID

        for product, amount in self.get_products_amounts_zip():
            product.reserved += amount
            db.session.add(product)

        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_n_orders(status):
        if not status in Order.order_status_ids:
            raise InvalidOrderStatusId
        return Order.query.filter(Order.status == status).count()
