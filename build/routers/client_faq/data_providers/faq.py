# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 25/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.content.faq import Faq


class ClientFaqDataProvider(object):
    def get_data(self):
        return dict(
            content=Faq.get().content_html
        )

client_faq_data_provider = ClientFaqDataProvider()
