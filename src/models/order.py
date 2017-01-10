# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 10/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from sqlalchemy import ForeignKey
from sqlalchemy import asc
from sqlalchemy import desc
from sqlalchemy.orm import relationship
from extensions import db
from sqlalchemy.dialects.postgresql import JSON
from r import R


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_email = db.Column(db.String(R.dimen.email_max_length), ForeignKey("client.email"), nullable=False)
    client = relationship("Client", back_populates="orders")
    status = db.Column(db.Enum(R.id), default=R.id.ORDER_STATUS_PAID, nullable=False)
    paid_datetime = db.Column(db.DateTime, nullable=False)
    sent_datetime = db.Column(db.DateTime)
    delivered_datetime = db.Column(db.DateTime)
    products_total_price = db.Column(db.Numeric(precision=12, scale=2), nullable=False)
    products_table_as_json = db.Column(JSON, nullable=False)
    total_table_as_json = db.Column(JSON, nullable=False)

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

    @staticmethod
    def get_choices():
        choices = []
        for order_status_id in Order.order_status_ids:
            choices.append((str(order_status_id.value), Order.order_status_as_string_by_id[order_status_id]))
        return choices
