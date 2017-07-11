# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 19/02/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import flash
from flask import url_for
from flask_login import current_user
from components.data_providers.cart_total_table import cart_total_table_data_provider
from r import R
from flask_bombril.r import R as bombril_R


class ClientCheckoutDataProvider(object):
    def get_data(self, step, user_form=None):
        user = current_user
        if user_form is None:
            user_form = user.get_form(edit=True)
        cart_data=user.get_cart_data()
        cart_update_messages = user.get_cart_update_messages()
        for message in cart_update_messages:
            flash(message, bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.info))
        return dict(
            page_heading_data=dict(
                path=[
                    dict(
                        name=R.string.home,
                        href=url_for("home.home")
                    ),
                    dict(
                        name=R.string.cart,
                        href=url_for("cart.cart")
                    ),
                    dict(
                        name=R.string.purchase_finalization,
                    )
                ],
                title=R.string.purchase_finalization
            ),
            step=step,
            user_form=user_form,
            cart_data=cart_data,
            cart_total_table_data=cart_total_table_data_provider.get_data(user)
        )

    def get_data_when_post(self, step, user_form):
        return self.get_data(step=step, user_form=user_form)


client_checkout_data_provider = ClientCheckoutDataProvider()
