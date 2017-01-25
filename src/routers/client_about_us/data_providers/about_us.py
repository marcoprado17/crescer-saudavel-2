# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 25/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.about_us import AboutUs


class ClientAboutUsDataProvider(object):
    def get_data(self):
        return dict(
            content=AboutUs.get().content
        )

client_about_us_data_provider = ClientAboutUsDataProvider()
