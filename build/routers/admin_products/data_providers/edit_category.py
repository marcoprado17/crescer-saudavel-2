# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.admin_products.forms import EditProductCategoryForm


class EditProductCategoryDataProvider(object):
    def get_data_when_get(self, product_category):
        return dict(
            edit_product_category_form=EditProductCategoryForm(product_category=product_category)
        )

    def get_data_when_post(self, edit_product_category_form):
        return dict(
            edit_product_category_form=edit_product_category_form
        )


admin_edit_product_category_data_provider = EditProductCategoryDataProvider()
