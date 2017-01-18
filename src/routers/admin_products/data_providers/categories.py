# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from pprint import pprint

from flask import current_app
from flask import url_for
from sqlalchemy import asc

from components.data_providers.super_table import super_table_data_provider
from flask_bombril.url_args import get_valid_enum
from flask_bombril.utils import n_pages
from components.data_providers.paginator import paginator_data_provider
from flask_bombril.utils import get_page_range
from flask_bombril.url_args import get_valid_page
from flask_bombril.url_args import get_boolean_url_arg
from models.product_category import ProductCategory
from r import R
from routers.admin_products.forms import ProductCategoryFilterForm
from wrappers.base.forms import SubmitForm


class AdminProductCategoriesDataProvider:
    def __init__(self):
        self.sort_method_ids = [
            R.id.SORT_METHOD_ID,
            R.id.SORT_METHOD_NAME,
        ]
        self.sort_method_names = [
            R.string.id,
            R.string.category_name,
        ]
        self.sort_method_by_id = {
            R.id.SORT_METHOD_ID: asc(ProductCategory.id),
            R.id.SORT_METHOD_NAME: asc(ProductCategory.name),
        }

    def get_data(self):
        active = get_boolean_url_arg(R.string.category_active_arg_name, True)
        sort_method_id = get_valid_enum(arg_name=R.string.sort_method_arg_name, enum=R.id,
                                        default=R.id.SORT_METHOD_NAME, possible_values=self.sort_method_ids)

        self.q = ProductCategory.query
        self.q = self.q.filter(ProductCategory.active == active)
        self.q = self.q.order_by(self.sort_method_by_id[sort_method_id])

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
            sort_methods=super_table_data_provider.get_sort_methods_data(
                selected_sort_method_id=sort_method_id,
                sort_method_ids=self.sort_method_ids,
                sort_method_names=self.sort_method_names
            ),
            table_data=self.get_table_data()
        )

    def get_table_data(self):
        rows = []
        for idx, category in enumerate(self.q.slice(
                *get_page_range(curr_page=self.curr_page, per_page=self.per_page, min_page=R.dimen.min_page)).all()):
            rows.append([
                "#" + str(category.id),
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
                        form=SubmitForm(),
                        meta_data={
                            "data-active-col-id": R.string.product_category_active_col_id
                        },
                        to_activate_url=url_for(
                            "admin_products.to_activate_category", category_id=category.id),
                        to_activate_meta_data={
                            "data-error-msg": R.string.to_activate_product_category_error(category),
                        },
                        disable_url=url_for(
                            "admin_products.disable_category", category_id=category.id),
                        disable_meta_data={
                            "data-error-msg": R.string.disable_product_category_error(category),
                        }
                    )
                ]
            ])

        return dict(
            id=R.string.product_categories_table_id,
            cols=[
                dict(
                    id="id",
                    title=R.string.id,
                    type=R.id.COL_TYPE_TEXT
                ),
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
