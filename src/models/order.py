# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 10/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import uuid

from collections import OrderedDict
from decimal import Decimal
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from proj_extensions import db
from models.base import BaseModel
from models.user.user import User
from models.product.product import Product
from proj_exceptions import InvalidOrderStatusIdError, InvalidOrderStatusChange, InsufficientStockToSendOrder, \
    InconsistentDataBaseError, InvalidClientToOrder, InvalidOrderError
from r import R


class Order(BaseModel):
    __tablename__ = "order"

    uuid = db.Column(db.String(R.dimen.uuid_length), nullable=False)
    client_id = db.Column(db.Integer, ForeignKey("user.id"), nullable=False)
    client_email = db.Column(db.String(R.dimen.email_max_length), nullable=False)
    client = relationship("User", back_populates="orders")
    status = db.Column(db.Enum(R.id), default=R.id.ORDER_STATUS_PAID, nullable=False)
    paid_datetime = db.Column(db.DateTime, nullable=False)
    sent_datetime = db.Column(db.DateTime)
    delivered_datetime = db.Column(db.DateTime)
    products_total_price = db.Column(db.Numeric(precision=12, scale=2), nullable=False)
    freight = db.Column(db.Numeric(precision=12, scale=2), nullable=False)
    products_data = db.Column(db.JSON, nullable=False)

    order_status_map = OrderedDict()
    order_status_map[R.id.ORDER_STATUS_ANY] = R.string.any
    order_status_map[R.id.ORDER_STATUS_CANCELED] = R.string.canceled
    order_status_map[R.id.ORDER_STATUS_PAID] = R.string.paid
    order_status_map[R.id.ORDER_STATUS_SENT] = R.string.sent
    order_status_map[R.id.ORDER_STATUS_DELIVERED] = R.string.delivered

    def __init__(self, client_id, status, product_ids_and_amount, **kwargs):
        self.client_id = client_id
        self.status = status
        self.product_ids_and_amount = product_ids_and_amount
        super(Order, self).__init__(**kwargs)

    @staticmethod
    def create_new(**kwargs):
        order = Order(**kwargs)
        client = User.get(order.client_id)
        if client is None:
            raise InvalidClientToOrder
        order.client_email = client.email
        order.freight = client.get_freight()

        products_amounts_zip = order.get_products_amounts_zip()

        for product, amount in products_amounts_zip:
            if amount <= 0 or product.stock < amount:
                raise InvalidOrderError

        order.products_total_price = order._get_products_total_price(products_amounts_zip)
        order.products_data = order._get_products_data(products_amounts_zip)
        order.inc_products_reserved(products_amounts_zip)
        order.uuid = str(uuid.uuid4())

        db.session.add(order)
        db.session.commit()
        return order

    def get_products_amounts_zip(self):
        products = []
        amounts = []

        if hasattr(self, "product_ids_and_amount"):
            for product_id, amount in self.product_ids_and_amount:
                product = Product.get(product_id)
                if product is None:
                    raise InvalidOrderError
                products.append(product)
                amounts.append(amount)
        elif self.products_data is not None:
            for row in self.products_data:
                product_id = row[0]
                amount = row[3]
                product = Product.get(product_id)
                if product is None:
                    raise InvalidOrderError
                products.append(product)
                amounts.append(amount)
        else:
            raise InvalidOrderError

        return zip(products, amounts)

    @staticmethod
    def inc_products_reserved(products_amounts_zip):
        for product, amount in products_amounts_zip:
            product.reserved += amount
            db.session.add(product)

    def get_status_as_string(self):
        return self.order_status_map[self.status]

    def get_formatted_paid_datetime(self, with_hifen=False):
        if self.paid_datetime is None:
            return R.string.empty_symbol
        if not with_hifen:
            return self.paid_datetime.strftime(R.string.default_datetime_format)
        else:
            return self.paid_datetime.strftime(R.string.default_datetime_format_with_hifen)

    def get_formatted_sent_datetime(self, with_hifen=False):
        if self.sent_datetime is None:
            return R.string.empty_symbol
        if not with_hifen:
            return self.sent_datetime.strftime(R.string.default_datetime_format)
        else:
            return self.sent_datetime.strftime(R.string.default_datetime_format_with_hifen)

    def get_formatted_delivered_datetime(self, with_hifen=False):
        if self.delivered_datetime is None:
            return R.string.empty_symbol
        if not with_hifen:
            return self.delivered_datetime.strftime(R.string.default_datetime_format)
        else:
            return self.delivered_datetime.strftime(R.string.default_datetime_format_with_hifen)

    @staticmethod
    def get_order_status_id_choices():
        choices = []
        for order_status_id, order_status_name in Order.order_status_map.iteritems():
            choices.append((str(order_status_id.value), order_status_name))
        return choices

    @staticmethod
    def _get_products_total_price(products_amounts_zip):
        products_total_price = Decimal("0.00")
        for product, amount in products_amounts_zip:
            products_total_price += product.get_price(n_units=amount)
        return products_total_price

    @staticmethod
    def _get_products_data(products_amounts_zip):
        rows = []
        for product, amount in products_amounts_zip:
            rows.append([
                product.id,
                product.title,
                R.string.format_price(product.price),
                amount,
                R.string.format_price(product.get_price(n_units=amount))
            ])
        return rows

    def get_formatted_total_price(self, include_rs=False):
        s = ""
        if include_rs:
            s += "R$ "
        s += str(self.products_total_price + self.freight).replace(".", ",")
        return s

    def mark_as_sent(self):
        if self.status != R.id.ORDER_STATUS_PAID:
            raise InvalidOrderStatusChange
        self.status = R.id.ORDER_STATUS_SENT
        self.sent_datetime = datetime.now()

        for product, amount in self.get_products_amounts_zip():
            if product.stock < amount:
                raise InsufficientStockToSendOrder(limiting_product=product)
            if product.reserved < amount:
                raise InconsistentDataBaseError
            product.reserved -= amount
            product.stock -= amount
            db.session.add(product)

        db.session.add(self)
        db.session.commit()

    def unmark_as_sent(self):
        if self.status != R.id.ORDER_STATUS_SENT:
            raise InvalidOrderStatusChange

        self.status = R.id.ORDER_STATUS_PAID
        self.sent_datetime = None

        for product, amount in self.get_products_amounts_zip():
            product.reserved += amount
            product.stock += amount
            if product.reserved < 0 or product.stock < 0:
                raise InconsistentDataBaseError
            db.session.add(product)

        db.session.add(self)
        db.session.commit()

    def mark_as_delivered(self):
        if self.status != R.id.ORDER_STATUS_SENT:
            raise InvalidOrderStatusChange

        self.status = R.id.ORDER_STATUS_DELIVERED
        self.delivered_datetime = datetime.now()

        db.session.add(self)
        db.session.commit()

    def unmark_as_delivered(self):
        if self.status != R.id.ORDER_STATUS_DELIVERED:
            raise InvalidOrderStatusChange

        self.status = R.id.ORDER_STATUS_SENT
        self.delivered_datetime = None

        db.session.add(self)
        db.session.commit()

    def mark_as_canceled(self):
        if self.status != R.id.ORDER_STATUS_PAID:
            raise InvalidOrderStatusChange

        self.status = R.id.ORDER_STATUS_CANCELED

        for product, amount in self.get_products_amounts_zip():
            product.reserved -= amount
            if product.reserved < 0:
                raise InconsistentDataBaseError
            db.session.add(product)

        db.session.add(self)
        db.session.commit()

    def mark_as_paid(self):
        if self.status != R.id.ORDER_STATUS_CANCELED:
            raise InvalidOrderStatusChange

        self.status = R.id.ORDER_STATUS_PAID

        for product, amount in self.get_products_amounts_zip():
            product.reserved += amount
            db.session.add(product)

        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_n_orders(status):
        if status not in Order.order_status_map.keys():
            raise InvalidOrderStatusIdError
        return Order.query.filter(Order.status == status).count()
