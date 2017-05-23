# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.content.dispatch import Dispatch
from routers.admin_content.forms import DispatchForm


class AdminDispatchDataProvider(object):
    def get_data(self):
        return dict(
            dispatch_form=DispatchForm(Dispatch.get())
        )

admin_dispatch_data_provider = AdminDispatchDataProvider()
