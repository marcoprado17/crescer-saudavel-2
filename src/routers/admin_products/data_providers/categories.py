# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from pprint import pprint

from flask import current_app
from flask import url_for
from sqlalchemy import asc

from build.flask_bombril.utils import n_pages
from components.data_providers.paginator import paginator_data_provider
from flask_bombril.utils import get_page_range
from flask_bombril.url_args import get_valid_page
from flask_bombril.url_args import get_boolean_url_arg
from models.product_category import ProductCategory
from r import R
from routers.admin_products.forms import ProductCategoryFilterForm


class AdminProductCategoriesDataProvider(object):
    def get_data(self):
        active = get_boolean_url_arg(R.string.category_active_arg_name, False)

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
                category.name,
                category.active,
                [
                    dict(
                        type=R.id.ACTION_TYPE_BUTTON,
                        text=R.string.edit,
                        classes=R.string.edit_class,
                        meta_data={
                            R.string.href_meta_data_key: url_for("admin_products.edit_category",
                                                                 category_id=category.id),
                        }
                    ),
                    dict(
                        type=R.id.ACTION_TYPE_BUTTON,
                        text=R.string.disable,
                        classes=R.string.disable_class + " " + (R.string.hidden_class if not category.active else ""),
                        id=R.string.disable_category_button_id(category.id),
                        meta_data={
                            R.string.to_activate_btn_id_meta_data_key: R.string.to_activate_category_button_id(
                                category.id),
                            R.string.disable_product_category_url_meta_data_key: url_for(
                                "admin_products.disable_category", category_id=category.id),
                            R.string.category_name_meta_data_key: category.name,
                            R.string.row_meta_data_key: idx
                        }
                    ),
                    dict(
                        type=R.id.ACTION_TYPE_BUTTON,
                        text=R.string.to_activate,
                        classes=R.string.to_activate_class + " " + (R.string.hidden_class if category.active else ""),
                        id=R.string.to_activate_category_button_id(category.id),
                        meta_data={
                            R.string.disable_btn_id_meta_data_key: R.string.disable_category_button_id(
                                category.id),
                            R.string.to_activate_product_category_url_meta_data_key: url_for(
                                "admin_products.to_activate_category", category_id=category.id),
                            R.string.category_name_meta_data_key: category.name,
                            R.string.row_meta_data_key: idx
                        }
                    )
                ]
            ])

        return dict(
            id=R.string.product_categories_table_id,
            cols=[
                dict(
                    id=R.string.product_category_name_col_id,
                    title=R.string.category,
                    type=R.id.COL_TYPE_TEXT
                ),
                dict(
                    id=R.string.product_category_active_col_id,
                    title=R.string.active_in_female,
                    type=R.id.COL_TYPE_BOOL
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
