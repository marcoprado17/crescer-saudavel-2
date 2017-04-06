# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 05/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.admin_products.forms import AddProductForm


class AddProductDataProvider(object):
    def get_data_when_get(self):
        return dict(
            add_product_form=AddProductForm()
        )

    def get_data_when_post(self, add_product_form):
        return dict(
            add_product_form=add_product_form
        )


admin_add_product_data_provider = AddProductDataProvider()
