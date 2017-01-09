# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from pprint import pprint

from flask import current_app
from flask import url_for
from sqlalchemy import asc

from flask_bombril.utils import n_pages
from components.data_providers.paginator import paginator_data_provider
from flask_bombril.utils import get_page_range
from flask_bombril.url_args import get_valid_page
from flask_bombril.url_args import get_boolean_url_arg
from models.product_category import ProductCategory
from r import R
from routers.admin_products.forms import ProductCategoryFilterForm


class AdminProductCategoriesDataProvider(object):
    def get_data(self):
        active = get_boolean_url_arg(R.string.category_active_arg_name, True)

        self.q = ProductCategory.query
        self.q = self.q.filter(ProductCategory.active == active)
        self.q = self.q.order_by(asc(ProductCategory.name))

        n_categories = self.q.count()

        self.per_page = current_app.config["DEFAULT_PER_PAGE"]
        self.curr_page = get_valid_page(page_arg_name=R.string.page_arg_name, per_page=self.per_page,
                                        n_items=n_categories)

        filter_form = ProductCategoryFilterForm()
        filter_form.set_values(active=active)

        return dict(
            n_items=n_categories,
            paginator_data=paginator_data_provider.get_data(
                min_page=R.dimen.min_page,
                curr_page=self.curr_page,
                max_page=n_pages(per_page=self.per_page, n_items=n_categories)
            ),
            filter_data=dict(
                filter_form=filter_form
            ),
            table_data=self.get_table_data()
        )

    def get_table_data(self):
        rows = []
        for idx, category in enumerate(self.q.slice(
                *get_page_range(curr_page=self.curr_page, per_page=self.per_page, min_page=R.dimen.min_page)).all()):
            rows.append([
                category.active,
                category.name,
                [
                    dict(
                        type=R.id.ACTION_TYPE_LINK_BUTTON,
                        text=R.string.edit,
                        classes=R.string.edit_class,
                        href=url_for("admin_products.edit_category", category_id=category.id)
                    ),
                    dict(
                        type=R.id.ACTION_TYPE_ACTIVATE_DISABLE_BUTTON,
                        active=category.active,
                        active_col_id=R.string.product_category_active_col_id,
                        to_activate_url=url_for(
                            "admin_products.to_activate_category", category_id=category.id),
                        error_to_activate_msg=R.string.to_activate_product_category_error(category.name),
                        disable_url=url_for(
                            "admin_products.disable_category", category_id=category.id),
                        error_disable_msg=R.string.disable_product_category_error(category.name)
                    )
                ]
            ])

        return dict(
            id=R.string.product_categories_table_id,
            cols=[
                dict(
                    id=R.string.product_category_active_col_id,
                    title=R.string.active_in_female,
                    type=R.id.COL_TYPE_BOOL
                ),
                dict(
                    id=R.string.product_category_name_col_id,
                    title=R.string.category,
                    type=R.id.COL_TYPE_TEXT
                ),
                dict(
                    id=R.string.action_col_id,
                    type=R.id.COL_TYPE_ACTION,
                    expandable=False
                )
            ],
            rows=rows
        )


admin_product_categories_data_provider = AdminProductCategoriesDataProvider()
