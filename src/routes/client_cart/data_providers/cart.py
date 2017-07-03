# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 09/02/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import flash
from flask import url_for

from components.data_providers.cart_total_table import cart_total_table_data_provider
from proj_forms import SubmitForm
from r import R
from flask_bombril.r import R as bombril_R


class ClientCartDataProvider(object):
    def get_data(self, base_user):
        carta_data = base_user.get_cart_data()
        cart_update_messages = base_user.get_cart_update_messages()
        for message in cart_update_messages:
            flash(message, bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.info))
        return dict(
            submit_form=SubmitForm(),
            page_heading_data=dict(
                path=[
                    dict(
                        name=R.string.home,
                        href=url_for("home.home")
                    ),
                    dict(
                        name=R.string.my_cart,
                    )
                ],
                title=R.string.my_cart
            ),
            cart_data=carta_data,
            cart_total_table_data=cart_total_table_data_provider.get_data(base_user)
        )


client_cart_data_provider = ClientCartDataProvider()
