# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 19/02/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from r import R


class CartTotalTableDataProvider(object):
    def get_data(self, base_user):
        return dict(
            products_total=base_user.get_cart_products_total(),
            freight=base_user.get_freight(),
            total=base_user.get_cart_products_total() + base_user.get_freight(),
            products_total_formatted=base_user.get_cart_products_total_as_string(include_rs=True),
            freight_formatted=base_user.get_freight_as_string(include_rs=True),
            total_formatted=R.string.decimal_price_as_string(price_as_decimal=base_user.get_cart_products_total()+base_user.get_freight(), include_rs=True)
        )

cart_total_table_data_provider = CartTotalTableDataProvider()
