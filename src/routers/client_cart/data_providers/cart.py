# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 09/02/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import url_for
from flask.ext.login import current_user
from proj_forms import SubmitForm
from r import R


class ClientCartDataProvider(object):
    def get_data(self, base_user):
        return dict(
            submit_form=SubmitForm(),
            page_heading_data=dict(
                path=[
                    dict(
                        name=R.string.home,
                        href=url_for("client_home.home")
                    ),
                    dict(
                        name=R.string.my_cart,
                    )
                ],
                title=R.string.my_cart
            ),
            cart_data=base_user.get_cart_data(),
            cart_total_table_data= dict(
                products_total=base_user.get_cart_products_total(),
                freight=base_user.get_freight(),
                total=base_user.get_cart_products_total() + base_user.get_freight(),
                products_total_formatted=base_user.get_cart_products_total_as_string(include_rs=True),
                freight_formatted=base_user.get_freight_as_string(include_rs=True),
                total_formatted=R.string.decimal_price_as_string(price_as_decimal=base_user.get_cart_products_total()+base_user.get_freight(), include_rs=True)
            )
        )


client_cart_data_provider = ClientCartDataProvider()
