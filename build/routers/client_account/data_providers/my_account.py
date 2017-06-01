# !/usr/bin/env python
# -*- coding= utf-8 -*-
# ======================================================================================================================
# Created at 07/02/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask_login import current_user


class ClientMyAccountDataProvider(object):
    def get_data_when_get(self, edit):
        user = current_user
        return dict(
            user=user,
            edit=edit,
            orders=current_user.orders,
            user_form=user.get_form(edit=edit)
        )

    def get_data_when_post(self, edit, user_form):
        return dict(
            user=current_user,
            edit=edit,
            orders=current_user.orders,
            user_form=user_form
        )


client_my_account_data_provider = ClientMyAccountDataProvider()
