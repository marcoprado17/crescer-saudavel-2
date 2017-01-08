# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 05/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import current_app
from flask import url_for
from sqlalchemy import asc

from flask_bombril.url_args import get_valid_model_id
from flask_bombril.utils import n_pages
from components.data_providers.paginator import paginator_data_provider
from flask_bombril.utils import get_page_range
from flask_bombril.url_args import get_valid_page
from flask_bombril.url_args import get_boolean_url_arg
from models.product_subcategory import ProductSubcategory
from r import R
from routers.admin_products.forms import ProductCategoryFilterForm, ProductSubcategoryFilterForm


class AdminProductSubcategoriesDataProvider(object):
    def get_data(self):
        active = get_boolean_url_arg(arg_name=R.string.subcategory_active_arg_name, default=True)
        category_id = get_valid_model_id(model=ProductSubcategory, arg_name=R.string.category_id_arg_name, include_zero=True, default=0)

        self.q = ProductSubcategory.query
        self.q = self.q.filter(ProductSubcategory.active == active)
        if category_id != 0:
            self.q = self.q.filter(ProductSubcategory.category_id == category_id)
        self.q = self.q.order_by(asc(ProductSubcategory.name))

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
            table_data=self.get_table_data()
        )

    def get_table_data(self):
        rows = []
        for idx, subcategory in enumerate(self.q.slice(
                *get_page_range(curr_page=self.curr_page, per_page=self.per_page, min_page=R.dimen.min_page)).all()):
            rows.append([
                subcategory.active,
                subcategory.category.name,
                subcategory.name,
                [
                    dict(
                        type=R.id.ACTION_TYPE_BUTTON,
                        text=R.string.edit,
                        classes=R.string.edit_class,
                        meta_data={
                            R.string.href_meta_data_key: url_for("admin_products.edit_subcategory",
                                                                 subcategory_id=subcategory.id),
                        }
                    ),
                    dict(
                        type=R.id.ACTION_TYPE_BUTTON,
                        text=R.string.disable,
                        classes=R.string.disable_class + " " + (R.string.hidden_class if not subcategory.active else ""),
                        id=R.string.disable_subcategory_button_id(subcategory.id),
                        meta_data={
                            R.string.to_activate_btn_id_meta_data_key: R.string.to_activate_subcategory_button_id(
                                subcategory.id),
                            R.string.disable_product_subcategory_url_meta_data_key: url_for(
                                "admin_products.disable_subcategory", subcategory_id=subcategory.id),
                            R.string.subcategory_name_meta_data_key: subcategory.name,
                            R.string.row_meta_data_key: idx
                        }
                    ),
                    dict(
                        type=R.id.ACTION_TYPE_BUTTON,
                        text=R.string.to_activate,
                        classes=R.string.to_activate_class + " " + (R.string.hidden_class if subcategory.active else ""),
                        id=R.string.to_activate_subcategory_button_id(subcategory.id),
                        meta_data={
                            R.string.disable_btn_id_meta_data_key: R.string.disable_subcategory_button_id(
                                subcategory.id),
                            R.string.to_activate_product_subcategory_url_meta_data_key: url_for(
                                "admin_products.to_activate_subcategory", subcategory_id=subcategory.id),
                            R.string.subcategory_name_meta_data_key: subcategory.name,
                            R.string.row_meta_data_key: idx
                        }
                    )
                ]
            ])

        return dict(
            id=R.string.product_subcategories_table_id,
            cols=[
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