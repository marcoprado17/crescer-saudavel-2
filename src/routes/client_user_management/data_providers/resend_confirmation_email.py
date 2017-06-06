# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 07/02/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routes.client_user_management.forms import ResendConfirmationEmailForm


class ClientResendConfirmationEmailDataProvider(object):
    def get_data_when_get(self):
        return dict(
            resend_confirmation_email_form=ResendConfirmationEmailForm()
        )

    def get_data_when_post(self, resend_confirmation_email_form):
        return dict(
            resend_confirmation_email_form=resend_confirmation_email_form
        )

client_resend_confirmation_email_data_provider = ClientResendConfirmationEmailDataProvider()
