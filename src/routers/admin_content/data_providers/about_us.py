# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 16/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.about_us import AboutUs
from routers.admin_content.forms import AboutUsForm


class AdminAboutUsDataProvider(object):
    def get_data(self):
        return dict(
            about_us_form=AboutUsForm(AboutUs.get())
        )

admin_about_us_data_provider = AdminAboutUsDataProvider()
