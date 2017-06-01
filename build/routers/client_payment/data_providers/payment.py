# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.content.payment import Payment


class ClientPaymentDataProvider(object):
    def get_data(self):
        return dict(
            content=Payment.get().content_html
        )

client_payment_data_provider = ClientPaymentDataProvider()
