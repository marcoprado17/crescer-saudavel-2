# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.dispatch import Dispatch


class ClientDispatchDataProvider(object):
    def get_data(self):
        return dict(
            content=Dispatch.get().content_html
        )

client_dispatch_data_provider = ClientDispatchDataProvider()
