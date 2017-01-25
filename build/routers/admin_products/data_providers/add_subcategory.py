# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.admin_products.forms import AddProductSubcategoryForm


class AddProductSubcategoryDataProvider(object):
    def get_data(self, add_product_subcategory_form=None):
        if not add_product_subcategory_form:
            add_product_subcategory_form = AddProductSubcategoryForm()

        return dict(
            add_product_subcategory_form = add_product_subcategory_form
        )

admin_add_product_subcategory_data_provider = AddProductSubcategoryDataProvider()
