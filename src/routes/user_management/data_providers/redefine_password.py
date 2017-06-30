# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 07/02/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routes.user_management.forms import RedefinePasswordForm


class ClientRedefinePasswordDataProvider(object):
    def get_data_when_get(self, email):
        return dict(
            redefine_password_form=RedefinePasswordForm(email=email)
        )

    def get_data_when_post(self, redefine_password_form):
        return dict(
            redefine_password_form=redefine_password_form
        )

client_redefine_password_data_provider = ClientRedefinePasswordDataProvider()
