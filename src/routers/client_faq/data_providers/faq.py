# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 25/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.faq import Faq


class ClientFaqDataProvider(object):
    def get_data(self):
        return dict(
            content=Faq.get().content
        )

client_faq_data_provider = ClientFaqDataProvider()
