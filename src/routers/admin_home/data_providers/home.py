# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 12/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import url_for

from models.order import Order
from r import R


class AdminHomeDataProvider(object):
    def get_data(self):
        return dict(
            n_new_orders=Order.get_n_orders(status=R.id.ORDER_STATUS_PAID),
            new_orders_href=url_for("admin_orders.orders")
        )

admin_home_data_provider = AdminHomeDataProvider()
