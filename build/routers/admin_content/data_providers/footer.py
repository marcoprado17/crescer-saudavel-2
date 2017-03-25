# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 16/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.footer import Footer
from routers.admin_content.forms import FooterForm


class AdminFooterDataProvider(object):
    def get_data(self):
        return dict(
            footer_form=FooterForm(Footer.get())
        )

admin_footer_data_provider = AdminFooterDataProvider()
