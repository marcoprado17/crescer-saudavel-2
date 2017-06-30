# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 06/02/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routes.user_management.forms import RegisterForm


class ClientRegisterDataProvider(object):
    def get_data_when_get(self, email):
        return dict(
            register_form=RegisterForm(email)
        )

    def get_data_when_post(self, register_form):
        return dict(
            register_form=register_form
        )


client_register_data_provider = ClientRegisterDataProvider()
