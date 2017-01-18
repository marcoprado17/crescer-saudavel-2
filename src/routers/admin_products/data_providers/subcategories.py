# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 05/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import current_app
from flask import url_for
from sqlalchemy import asc

from components.data_providers.super_table import super_table_data_provider
from flask_bombril.url_args import get_valid_enum
from flask_bombril.url_args import get_valid_model_id
from flask_bombril.utils import n_pages
from components.data_providers.paginator import paginator_data_provider
from flask_bombril.utils import get_page_range
from flask_bombril.url_args import get_valid_page
from flask_bombril.url_args import get_boolean_url_arg
from models.product_subcategory import ProductSubcategory
from r import R
from routers.admin_products.forms import ProductSubcategoryFilterForm
from wrappers.base.forms import SubmitForm


class AdminProductSubcategoriesDataProvider:
    def __init__(self):
        self.sort_method_ids = [
            R.id.SORT_METHOD_ID,
            R.id.SORT_METHOD_NAME,
        ]
        self.sort_method_names = [
            R.string.id,
            R.string.subcategory_name,
        ]
        self.sort_method_by_id = {
            R.id.SORT_METHOD_ID: asc(ProductSubcategory.id),
            R.id.SORT_METHOD_NAME: asc(ProductSubcategory.name),
        }

    def get_data(self):
        active = get_boolean_url_arg(arg_name=R.string.subcategory_active_arg_name, default=True)
        category_id = get_valid_model_id(model=ProductSubcategory, arg_name=R.string.category_id_arg_name, include_zero=True, default=0)
        sort_method_id = get_valid_enum(arg_name=R.string.sort_method_arg_name, enum=R.id,
                                        default=R.id.SORT_METHOD_NAME, possible_values=self.sort_method_ids)


        self.q = ProductSubcategory.query
        self.q = self.q.filter(ProductSubcategory.active == active)
        if category_id != 0:
            self.q = self.q.filter(ProductSubcategory.category_id == category_id)
        self.q = self.q.order_by(self.sort_method_by_id[sort_method_id])

        n_subcategories = self.q.count()

        self.per_page = current_app.config["DEFAULT_PER_PAGE"]
        self.curr_page = get_valid_page(page_arg_name=R.string.page_arg_name, per_page=self.per_page,
                                        n_items=n_subcategories)

        filter_form = ProductSubcategoryFilterForm()
        filter_form.set_values(category_id=category_id, active=active)

        return dict(
            n_items=n_subcategories,
            paginator_data=paginator_data_provider.get_data(
                min_page=R.dimen.min_page,
                curr_page=self.curr_page,
                max_page=n_pages(per_page=self.per_page, n_items=n_subcategories)
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
        for idx, subcategory in enumerate(self.q.slice(
                *get_page_range(curr_page=self.curr_page, per_page=self.per_page, min_page=R.dimen.min_page)).all()):
            rows.append([
                "#" + str(subcategory.id),
                subcategory.active,
                subcategory.category.name,
                subcategory.name,
                [
                    dict(
                        type=R.id.ACTION_TYPE_LINK_BUTTON,
                        text=R.string.edit,
                        classes=R.string.edit_class,
                        href=url_for("admin_products.edit_subcategory", subcategory_id=subcategory.id)
                    ),
                    dict(
                        type=R.id.ACTION_TYPE_ACTIVATE_DISABLE_BUTTON,
                        active=subcategory.active,
                        form=SubmitForm(),
                        meta_data={
                            "data-active-col-id": R.string.product_subcategory_active_col_id
                        },
                        to_activate_url=url_for(
                            "admin_products.to_activate_subcategory", subcategory_id=subcategory.id),
                        to_activate_meta_data={
                            "data-error-msg": R.string.to_activate_product_subcategory_error(subcategory.name),
                        },
                        disable_url=url_for(
                            "admin_products.disable_subcategory", subcategory_id=subcategory.id),
                        disable_meta_data={
                            "data-error-msg": R.string.disable_product_subcategory_error(subcategory.name),
                        }
                    )
                ]
            ])

        return dict(
            id=R.string.product_subcategories_table_id,
            cols=[
                dict(
                    id="id",
                    title=R.string.id,
                    type=R.id.COL_TYPE_TEXT
                ),
                dict(
                    id=R.string.product_subcategory_active_col_id,
                    title=R.string.active_in_female,
                    type=R.id.COL_TYPE_BOOL
                ),
                dict(
                    id=R.string.product_category_name_col_id,
                    title=R.string.category,
                    type=R.id.COL_TYPE_TEXT
                ),
                dict(
                    id=R.string.product_subcategory_name_col_id,
                    title=R.string.subcategory,
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


admin_product_subcategories_data_provider = AdminProductSubcategoriesDataProvider()