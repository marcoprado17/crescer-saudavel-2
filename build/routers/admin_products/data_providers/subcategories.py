# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 05/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import current_app
from flask import url_for

from components.data_providers.paginator import paginator_data_provider
from components.data_providers.super_table import super_table_data_provider
from flask_bombril.url_args import get_boolean_url_arg
from flask_bombril.url_args import get_valid_enum
from flask_bombril.url_args import get_valid_model_id
from flask_bombril.url_args import get_valid_page
from flask_bombril.utils import get_page_range
from flask_bombril.utils import n_pages
from proj_forms import SubmitForm
from models.product_subcategory import ProductSubcategory
from r import R
from routers.admin_products.forms import ProductSubcategoryFilterForm


class AdminProductSubcategoriesDataProvider(object):
    def get_data(self):
        active = get_boolean_url_arg(arg_name=R.string.subcategory_active_arg_name, default=True)
        category_id = get_valid_model_id(model=ProductSubcategory, arg_name=R.string.category_id_arg_name, include_zero=True, default=0)
        sort_method_id = get_valid_enum(arg_name=R.string.sort_method_arg_name, enum=R.id,
                                        default=R.id.SORT_METHOD_NAME, possible_values=ProductSubcategory.sort_method_map.ids)

        self.q = ProductSubcategory.query
        self.q = self.q.filter(ProductSubcategory.active == active)
        if category_id != 0:
            self.q = self.q.filter(ProductSubcategory.category_id == category_id)
        self.q = self.q.order_by(ProductSubcategory.sort_method_map.order(sort_method_id))

        n_subcategories = self.q.count()

        self.per_page = current_app.config["DEFAULT_PER_PAGE"]
        self.curr_page = get_valid_page(page_arg_name=R.string.page_arg_name, per_page=self.per_page,
                                        n_items=n_subcategories)

        return dict(
            n_items=n_subcategories,
            paginator_data=paginator_data_provider.get_data(
                min_page=R.dimen.min_page,
                curr_page=self.curr_page,
                max_page=n_pages(per_page=self.per_page, n_items=n_subcategories)
            ),
            filter_data=dict(
                filter_form=ProductSubcategoryFilterForm(category_id=category_id, active=active)
            ),
            sort_methods=super_table_data_provider.get_sort_methods_data(
                selected_sort_method_id=sort_method_id,
                sort_method_map=ProductSubcategory.sort_method_map
            ),
            table_data=self.get_table_data()
        )

    def get_table_data(self):
        rows = []
        for idx, product_subcategory in enumerate(self.q.slice(
                *get_page_range(curr_page=self.curr_page, per_page=self.per_page, min_page=R.dimen.min_page)).all()):
            rows.append([
                "#" + str(product_subcategory.id),
                product_subcategory.active,
                product_subcategory.category.name,
                product_subcategory.name,
                [
                    dict(
                        type=R.id.ACTION_TYPE_LINK_BUTTON,
                        text=R.string.edit,
                        classes=R.string.edit_class,
                        href=url_for("admin_products.edit_subcategory", product_subcategory_id=product_subcategory.id)
                    ),
                    dict(
                        type=R.id.ACTION_TYPE_ACTIVATE_DISABLE_BUTTON,
                        active=product_subcategory.active,
                        form=SubmitForm(),
                        meta_data={
                            "data-active-col-id": R.string.product_subcategory_active_col_id
                        },
                        to_activate_url=url_for(
                            "admin_products.to_activate_subcategory", product_subcategory_id=product_subcategory.id),
                        to_activate_meta_data={
                            "data-error-msg": R.string.to_activate_product_subcategory_error(product_subcategory),
                        },
                        disable_url=url_for(
                            "admin_products.disable_subcategory", product_subcategory_id=product_subcategory.id),
                        disable_meta_data={
                            "data-error-msg": R.string.disable_product_subcategory_error(product_subcategory),
                        }
                    )
                ]
            ])

        return dict(
            id=R.string.product_subcategories_table_id,
            expandable=True,
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
                    type=R.id.COL_TYPE_ACTION
                )
            ],
            rows=rows
        )


admin_product_subcategories_data_provider = AdminProductSubcategoriesDataProvider()