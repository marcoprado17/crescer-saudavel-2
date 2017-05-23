# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import current_app
from flask import url_for

from components.data_providers.paginator import paginator_data_provider
from flask_bombril.url_args import get_boolean_url_arg
from flask_bombril.url_args import get_valid_enum
from flask_bombril.url_args import get_valid_page
from flask_bombril.utils import get_page_range
from flask_bombril.utils import n_pages
from models.product.product_category import ProductCategory
from proj_forms import SubmitForm
from proj_utils import get_sort_methods_data
from r import R
from routers.admin_products.forms import ProductCategoryFilterForm


class AdminProductCategoriesDataProvider(object):
    def get_data(self):
        active = get_boolean_url_arg(R.string.category_active_arg_name, True)
        sort_method_id = get_valid_enum(arg_name=R.string.sort_method_arg_name, enum=R.id,
                                        default=R.id.SORT_METHOD_NAME, possible_values=ProductCategory.sort_method_map.ids)

        self.q = ProductCategory.query
        self.q = self.q.filter(ProductCategory.active == active)
        self.q = self.q.order_by(*ProductCategory.sort_method_map.order(sort_method_id))

        n_categories = self.q.count()

        self.per_page = current_app.config["DEFAULT_PER_PAGE"]
        self.curr_page = get_valid_page(page_arg_name=R.string.page_arg_name, per_page=self.per_page,
                                        n_items=n_categories)

        return dict(
            n_items=n_categories,
            paginator_data=paginator_data_provider.get_data(
                min_page=R.dimen.min_page,
                curr_page=self.curr_page,
                max_page=n_pages(per_page=self.per_page, n_items=n_categories)
            ),
            filter_data=dict(
                filter_form=ProductCategoryFilterForm(active=active)
            ),
            sort_methods=get_sort_methods_data(
                selected_sort_method_id=sort_method_id,
                sort_method_map=ProductCategory.sort_method_map
            ),
            table_data=self.get_table_data()
        )

    def get_table_data(self):
        rows = []
        for idx, product_category in enumerate(self.q.slice(
                *get_page_range(curr_page=self.curr_page, per_page=self.per_page, min_page=R.dimen.min_page)).all()):
            rows.append([
                "#" + str(product_category.id),
                product_category.active,
                product_category.name,
                product_category.priority,
                [
                    dict(
                        type=R.id.ACTION_TYPE_LINK_BUTTON,
                        text=R.string.edit,
                        classes=R.string.edit_class,
                        href=url_for("admin_products.edit_category", product_category_id=product_category.id)
                    ),
                    dict(
                        type=R.id.ACTION_TYPE_ACTIVATE_DISABLE_BUTTON,
                        active=product_category.active,
                        form=SubmitForm(),
                        meta_data={
                            "data-active-col-id": R.string.product_category_active_col_id
                        },
                        to_activate_url=url_for(
                            "admin_products.to_activate_category", product_category_id=product_category.id),
                        to_activate_meta_data={
                            "data-error-msg": R.string.to_activate_product_category_error(product_category),
                        },
                        disable_url=url_for(
                            "admin_products.disable_category", product_category_id=product_category.id),
                        disable_meta_data={
                            "data-error-msg": R.string.disable_product_category_error(product_category),
                        }
                    )
                ]
            ])

        return dict(
            id=R.string.product_categories_table_id,
            expandable=True,
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
                    id="priority",
                    title=R.string.priority,
                    type=R.id.COL_TYPE_TEXT
                ),
                dict(
                    id=R.string.action_col_id,
                    type=R.id.COL_TYPE_ACTION
                )
            ],
            rows=rows
        )


admin_product_categories_data_provider = AdminProductCategoriesDataProvider()
