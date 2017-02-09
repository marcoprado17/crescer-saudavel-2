# !/usr/bin/env python
# -*- coding= utf-8 -*-
# ======================================================================================================================
# Created at 07/02/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask_login import current_user


class ClientMyAccountDataProvider(object):
    def get_data_when_get(self, edit):
        return dict(
            user=current_user,
            edit=edit,
            orders=current_user.orders
        )


client_my_account_data_provider = ClientMyAccountDataProvider()
