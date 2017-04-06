# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.exchanges_and_returns import ExchangesAndReturns


class ClientExchangesAndReturnsDataProvider(object):
    def get_data(self):
        return dict(
            content=ExchangesAndReturns.get().content_html
        )

client_exchanges_and_returns_data_provider = ClientExchangesAndReturnsDataProvider()
