# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 06/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import current_app
from flask import url_for
from models.product_category import ProductCategory

from components.data_providers.paginator import paginator_data_provider
from flask_bombril.url_args import get_boolean_url_arg
from flask_bombril.url_args import get_valid_enum
from flask_bombril.url_args import get_valid_model_id
from flask_bombril.url_args import get_valid_page
from flask_bombril.utils import get_page_range
from flask_bombril.utils import n_pages
from models.product import Product
from models.product.product_subcategory import ProductSubcategory
from proj_forms import SubmitForm
from proj_utils import get_sort_methods_data
from r import R
from routers.admin_products.forms import ProductFilterForm, AddToStockForm, RemoveFromStockForm, UpdateStockForm


class AdminProductsDataProvider(object):

    def get_data(self):
        category_id = get_valid_model_id(model=ProductCategory, arg_name=R.string.category_id_arg_name,
                                         include_zero=True, default=0)
        subcategory_id = get_valid_model_id(model=ProductSubcategory, arg_name=R.string.subcategory_id_arg_name,
                                            include_zero=True, default=0)
        active = get_boolean_url_arg(arg_name=R.string.subcategory_active_arg_name, default=True)
        sort_method_id = get_valid_enum(arg_name=R.string.sort_method_arg_name, enum=R.id,
                                        default=R.id.SORT_METHOD_TITLE, possible_values=Product.sort_method_map.ids)

        self.q = Product.query
        self.q = self.q.filter(Product.active == active)
        if category_id != 0:
            self.q = self.q.filter(Product.category_id == category_id)
        if subcategory_id != 0:
            self.q = self.q.filter(Product.subcategory_id == subcategory_id)
        self.q = self.q.order_by(*Product.sort_method_map.order(sort_method_id))

        n_products = self.q.count()

        self.per_page = current_app.config["DEFAULT_PER_PAGE"]
        self.curr_page = get_valid_page(page_arg_name=R.string.page_arg_name, per_page=self.per_page,
                                        n_items=n_products)

        return dict(
            n_items=n_products,
            paginator_data=paginator_data_provider.get_data(
                min_page=R.dimen.min_page,
                curr_page=self.curr_page,
                max_page=n_pages(per_page=self.per_page, n_items=n_products)
            ),
            filter_data=dict(
                filter_form=ProductFilterForm(category_id=category_id, subcategory_id=subcategory_id, active=active)
            ),
            sort_methods=get_sort_methods_data(
                selected_sort_method_id=sort_method_id,
                sort_method_map=Product.sort_method_map,
            ),
            table_data=self.get_table_data()
        )

    def get_table_data(self):
        rows = []
        for idx, product in enumerate(self.q.slice(
                *get_page_range(curr_page=self.curr_page, per_page=self.per_page, min_page=R.dimen.min_page)).all()):
            rows.append([
                product.id_formatted,
                product.active,
                product.category.name,
                product.subcategory.name if product.subcategory else R.string.empty_symbol,
                product.title,
                product.get_formatted_price(),
                product.price_with_discount_as_string(),
                product.stock,
                product.available,
                product.reserved,
                product.min_available,
                product.sales_number,
                [
                    dict(
                        type=R.id.ACTION_TYPE_LINK_BUTTON,
                        text=R.string.preview,
                        classes="preview",
                        href=url_for("admin_products.product_preview", product_id=product.id),
                        new_tab=True
                    ),
                    dict(
                        type=R.id.ACTION_TYPE_LINK_BUTTON,
                        text=R.string.edit,
                        classes=R.string.edit_class,
                        href=url_for("admin_products.edit_product", product_id=product.id),
                    ),
                    dict(
                        type=R.id.ACTION_TYPE_INT_WITH_BUTTON,
                        form=AddToStockForm(),
                        classes="add-stock",
                        url=url_for("admin_products.product_stock_addition", product_id=product.id),
                        meta_data = {
                            "data-text": R.string.add_to_stock,
                            "data-doing-text": R.string.adding,
                            "data-error-4xx-msg": R.string.stock_change_invalid_form_error(product),
                            "data-error-5xx-msg": R.string.stock_change_error(product)
                        },
                    ),
                    dict(
                        type=R.id.ACTION_TYPE_INT_WITH_BUTTON,
                        form=RemoveFromStockForm(),
                        classes="remove-from-stock",
                        url=url_for("admin_products.product_stock_removal", product_id=product.id),
                        meta_data = {
                            "data-text": R.string.remove_from_stock,
                            "data-doing-text": R.string.removing,
                            "data-error-4xx-msg": R.string.stock_change_invalid_form_error(product),
                            "data-error-5xx-msg": R.string.stock_change_error(product)
                        }
                    ),
                    dict(
                        type=R.id.ACTION_TYPE_INT_WITH_BUTTON,
                        form=UpdateStockForm(),
                        classes="update-stock",
                        url=url_for("admin_products.product_stock_update", product_id=product.id),
                        meta_data = {
                            "data-text": R.string.update_stock,
                            "data-doing-text": R.string.updating,
                            "data-error-4xx-msg": R.string.stock_change_invalid_form_error(product),
                            "data-error-5xx-msg": R.string.stock_change_error(product)
                        }
                    ),
                    dict(
                        type=R.id.ACTION_TYPE_ACTIVATE_DISABLE_BUTTON,
                        active=product.active,
                        form=SubmitForm(),
                        meta_data= {
                            "data-active-col-id": R.string.product_active_col_id
                        },
                        to_activate_url=url_for(
                            "admin_products.to_activate_product", product_id=product.id),
                        to_activate_meta_data={
                            "data-error-msg": R.string.to_activate_product_error(product),
                        },
                        disable_url = url_for(
                                "admin_products.disable_product", product_id=product.id),
                        disable_meta_data= {
                            "data-error-msg": R.string.disable_product_error(product),
                        }
                    ),
                ]
            ])

        return dict(
            id=R.string.products_table_id,
            expandable=True,
            cols=[
                dict(
                    id="id",
                    title=R.string.id,
                    type=R.id.COL_TYPE_TEXT
                ),
                dict(
                    id=R.string.product_active_col_id,
                    title=R.string.active,
                    type=R.id.COL_TYPE_BOOL
                ),
                dict(
                    id=R.string.product_category_col_id,
                    title=R.string.category,
                    type=R.id.COL_TYPE_TEXT
                ),
                dict(
                    id=R.string.product_subcategory_name_col_id,
                    title=R.string.subcategory,
                    type=R.id.COL_TYPE_TEXT
                ),
                dict(
                    id=R.string.product_title_col_id,
                    title=R.string.title,
                    type=R.id.COL_TYPE_TEXT
                ),
                dict(
                    id=R.string.product_price_col_id,
                    title=R.string.price,
                    type=R.id.COL_TYPE_TEXT,
                    tooltip=R.string.price_in_real
                ),
                dict(
                    id="price-with-discount",
                    title=R.string.price_with_discount,
                    type=R.id.COL_TYPE_TEXT,
                    tooltip=R.string.price_in_real
                ),
                dict(
                    id=R.string.product_stock_col_id,
                    title=R.string.in_stock,
                    type=R.id.COL_TYPE_TEXT,
                ),
                dict(
                    id="available",
                    title=R.string.available,
                    type=R.id.COL_TYPE_TEXT,
                    tooltip=R.string.available_tooltip
                ),
                dict(
                    id="reserved",
                    title=R.string.reserved,
                    type=R.id.COL_TYPE_TEXT,
                    tooltip=R.string.reserved_tooltip
                ),
                dict(
                    id="min-available",
                    title=R.string.min_available,
                    type=R.id.COL_TYPE_TEXT,
                    tooltip=R.string.min_available_tooltip
                ),
                dict(
                    id=R.string.product_sales_number_col_id,
                    title=R.string.sales,
                    type=R.id.COL_TYPE_TEXT,
                ),
                dict(
                    id=R.string.action_col_id,
                    type=R.id.COL_TYPE_ACTION
                )
            ],
            rows=rows
        )


admin_products_data_provider = AdminProductsDataProvider()
