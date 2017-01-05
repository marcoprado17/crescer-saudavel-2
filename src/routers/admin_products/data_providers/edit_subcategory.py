# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 05/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.admin_products.forms import EditProductSubcategoryForm


class EditProductSubcategoryDataProvider(object):
    def get_data_when_get(self, product_subcategory):
        edit_product_subcategory_form = EditProductSubcategoryForm()
        edit_product_subcategory_form.set_values(product_subcategory=product_subcategory)
        return dict(
            edit_product_subcategory_form=edit_product_subcategory_form
        )

    def get_data_when_post(self, edit_product_subcategory_form):
        return dict(
            edit_product_subcategory_form=edit_product_subcategory_form
        )


admin_edit_product_subcategory_data_provider = EditProductSubcategoryDataProvider()