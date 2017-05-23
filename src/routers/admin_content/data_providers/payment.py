# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.content.payment import Payment
from routers.admin_content.forms import PaymentForm


class AdminPaymentDataProvider(object):
    def get_data(self):
        return dict(
            payment_form=PaymentForm(Payment.get())
        )

admin_payment_data_provider = AdminPaymentDataProvider()
