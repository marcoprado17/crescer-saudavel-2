# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 10/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from decimal import Decimal

from sqlalchemy import ForeignKey
from sqlalchemy import asc
from sqlalchemy import desc
from sqlalchemy.orm import relationship
from extensions import db
from sqlalchemy.dialects.postgresql import JSON

from models.product import Product
from r import R


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_email = db.Column(db.String(R.dimen.email_max_length), ForeignKey("client.email"), nullable=False)
    client = relationship("Client", back_populates="orders")
    status = db.Column(db.Enum(R.id), default=R.id.ORDER_STATUS_PAID, nullable=False)
    paid_datetime = db.Column(db.DateTime, nullable=False)
    sent_datetime = db.Column(db.DateTime)
    delivered_datetime = db.Column(db.DateTime)
    quantity_by_product_id = db.Column(JSON, nullable=False)
    products_total_price = db.Column(db.Numeric(precision=12, scale=2), nullable=False)

    def __init__(self, **kwargs):
        super(Order, self).__init__(**kwargs)
        self.products_total_price = self.get_products_total_price()

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
        R.id.ORDER_STATUS_PAID,
        R.id.ORDER_STATUS_SENT,
        R.id.ORDER_STATUS_DELIVERED
    ]
    order_status_as_string_by_id = {
        R.id.ORDER_STATUS_ANY: R.string.any,
        R.id.ORDER_STATUS_PAID: R.string.paid,
        R.id.ORDER_STATUS_SENT: R.string.sent,
        R.id.ORDER_STATUS_DELIVERED: R.string.delivered
    }

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

    def get_products_total_price(self):
        products_total_price = Decimal("0.00")
        for product_id, quantity in self.quantity_by_product_id.iteritems():
            product = Product.get(product_id)
            products_total_price += product.get_price(n_units=quantity)
        return products_total_price

    def get_products_table_data(self):
        rows = []
        products = Product.query.filter(Product.id.in_(self.quantity_by_product_id.keys())).all()
        for product in products:
            quantity = self.quantity_by_product_id[str(product.id)]
            rows.append([
                product.title,
                product.get_formatted_price(),
                quantity,
                product.get_formatted_price(n_units=quantity)
            ])

        return dict(
            table_data=dict(
                id="products-table",
                cols=[
                    dict(
                        id="product-title",
                        title=R.string.product,
                        type=R.id.COL_TYPE_TEXT
                    ),
                    dict(
                        id="product-price",
                        title=R.string.price,
                        type=R.id.COL_TYPE_TEXT,
                        tooltip=R.string.product_price_tooltip
                    ),
                    dict(
                        id="product-quantity",
                        title=R.string.quantity,
                        type=R.id.COL_TYPE_TEXT
                    ),
                    dict(
                        id="product-subtotal",
                        title=R.string.subtotal,
                        type=R.id.COL_TYPE_TEXT,
                        tooltip=R.string.subtotal_tooltip
                    ),
                ],
                rows=rows
            )
        )

    def get_total_table_data(self):
        products_total_price = self.get_products_total_price()
        freight = self.client.get_freight()
        return dict(
            table_data=dict(
                no_head = True,
                bordered = True,
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
                    [R.string.products, R.string.price_with_rs(products_total_price)],
                    [R.string.freight, R.string.price_with_rs(freight)],
                    [R.string.total, R.string.price_with_rs(products_total_price + freight)]
                ]
            )
        )

    def get_formatted_products_total_price(self):
        return str(self.products_total_price).replace(".", ",")
