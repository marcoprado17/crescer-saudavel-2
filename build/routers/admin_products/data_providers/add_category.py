# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.admin_products.forms import AddProductCategoryForm


class AddProductCategoryDataProvider(object):
    def get_data(self, add_product_category_form=None):
        if not add_product_category_form:
            add_product_category_form = AddProductCategoryForm()

        return dict(
            add_product_category_form = add_product_category_form
        )

admin_add_product_category_data_provider = AddProductCategoryDataProvider()
