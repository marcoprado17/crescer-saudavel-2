# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 06/02/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.client_user_management.forms import LoginForm


class ClientLoginDataProvider(object):
    def get_data_when_get(self, email=None):
        return dict(
            login_form=LoginForm(email)
        )

    def get_data_when_post(self, login_form):
        return dict(
            login_form=LoginForm()
        )


client_login_data_provider = ClientLoginDataProvider()
