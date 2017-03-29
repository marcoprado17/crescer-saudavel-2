# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.exchanges_and_returns import ExchangesAndReturns
from routers.admin_content.forms import ExchangesAndReturnsForm


class AdminExchangesAndReturnsDataProvider(object):
    def get_data(self):
        return dict(
            exchanges_and_returns_form=ExchangesAndReturnsForm(ExchangesAndReturns.get())
        )

admin_exchanges_and_returns_data_provider = AdminExchangesAndReturnsDataProvider()
