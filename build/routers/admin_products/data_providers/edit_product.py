# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 08/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.admin_products.forms import EditProductForm


class EditProductDataProvider(object):
    def get_data_when_get(self, product):
        edit_product_form = EditProductForm()
        edit_product_form.set_values(product=product)
        return dict(
            edit_product_form=edit_product_form
        )

    def get_data_when_post(self, edit_product_form):
        return dict(
            edit_product_form=edit_product_form
        )


admin_edit_product_data_provider = EditProductDataProvider()
