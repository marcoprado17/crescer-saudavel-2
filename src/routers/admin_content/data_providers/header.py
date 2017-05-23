# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.content.header import Header
from routers.admin_content.forms import HeaderForm


class AdminHeaderDataProvider(object):
    def get_data(self):
        return dict(
            header_form=HeaderForm(Header.get())
        )

admin_header_data_provider = AdminHeaderDataProvider()
