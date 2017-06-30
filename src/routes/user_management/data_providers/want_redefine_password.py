# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 07/02/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routes.user_management.forms import WantRedefinePasswordForm


class ClientWantRedefinePasswordDataProvider(object):
    def get_data_when_get(self):
        return dict(
            want_redefine_password_form=WantRedefinePasswordForm()
        )

    def get_data_when_post(self, want_redefine_password_form):
        return dict(
            want_redefine_password_form=want_redefine_password_form
        )


client_want_redefine_password_data_provider = ClientWantRedefinePasswordDataProvider()
