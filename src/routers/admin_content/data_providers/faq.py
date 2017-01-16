# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 16/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.faq import Faq
from routers.admin_content.forms import FaqForm


class AdminFaqDataProvider(object):
    def get_data(self):
        faq_form = FaqForm()
        faq_form.set_values(Faq.get())
        return dict(
            faq_form=faq_form
        )

admin_faq_data_provider = AdminFaqDataProvider()
