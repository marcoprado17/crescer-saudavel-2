# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 06/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import current_app
from flask import url_for
from sqlalchemy import asc
from sqlalchemy import desc

from components.data_providers.super_table import super_table_data_provider
from flask_bombril.url_args import get_valid_enum
from flask_bombril.url_args import get_valid_model_id
from flask_bombril.utils import n_pages
from components.data_providers.paginator import paginator_data_provider
from flask_bombril.utils import get_page_range
from flask_bombril.url_args import get_valid_page
from flask_bombril.url_args import get_boolean_url_arg
from models.product import Product
from models.product_category import ProductCategory
from models.product_subcategory import ProductSubcategory
from r import R
from routers.admin_products.forms import ProductFilterForm, AddToStockForm, RemoveFromStockForm, UpdateStockForm


class AdminProductsDataProvider:
    def __init__(self):
        self.sort_method_ids = [
            R.id.SORT_METHOD_TITLE,
            R.id.SORT_METHOD_LOWEST_PRICE,
            R.id.SORT_METHOD_HIGHER_PRICE,
            R.id.SORT_METHOD_LOWEST_STOCK,
            R.id.SORT_METHOD_HIGHER_STOCK,
            R.id.SORT_METHOD_BEST_SELLER,
            R.id.SORT_METHOD_LESS_SOLD
        ]
        self.sort_method_names = [
            R.string.title,
            R.string.lowest_price,
            R.string.higher_price,
            R.string.lowest_stock,
            R.string.higher_stock,
            R.string.best_seller,
            R.string.less_sold
        ]
        self.sort_method_by_id = {
            R.id.SORT_METHOD_TITLE: asc(Product.title),
            R.id.SORT_METHOD_LOWEST_PRICE: asc(Product.price),
            R.id.SORT_METHOD_HIGHER_PRICE: desc(Product.price),
            R.id.SORT_METHOD_LOWEST_STOCK: asc(Product.stock),
            R.id.SORT_METHOD_HIGHER_STOCK: desc(Product.stock),
            R.id.SORT_METHOD_BEST_SELLER: desc(Product.sales_number),
            R.id.SORT_METHOD_LESS_SOLD: asc(Product.sales_number)
        }

    def get_data(self):
        category_id = get_valid_model_id(model=ProductCategory, arg_name=R.string.category_id_arg_name,
                                         include_zero=True, default=0)
        subcategory_id = get_valid_model_id(model=ProductSubcategory, arg_name=R.string.subcategory_id_arg_name,
                                            include_zero=True, default=0)
        active = get_boolean_url_arg(arg_name=R.string.subcategory_active_arg_name, default=True)
        sort_method_id = get_valid_enum(arg_name=R.string.sort_method_arg_name, enum=R.id,
                                        default=R.id.SORT_METHOD_TITLE, possible_values=self.sort_method_ids)

        self.q = Product.query
        self.q = self.q.filter(Product.active == active)
        if category_id != 0:
            self.q = self.q.filter(Product.category_id == category_id)
        if subcategory_id != 0:
            self.q = self.q.filter(Product.subcategory_id == subcategory_id)
        self.q = self.q.order_by(self.sort_method_by_id[sort_method_id])

        n_products = self.q.count()

        self.per_page = current_app.config["DEFAULT_PER_PAGE"]
        self.curr_page = get_valid_page(page_arg_name=R.string.page_arg_name, per_page=self.per_page,
                                        n_items=n_products)

        filter_form = ProductFilterForm()
        filter_form.set_values(category_id=category_id, subcategory_id=subcategory_id, active=active)

        return dict(
            n_items=n_products,
            paginator_data=paginator_data_provider.get_data(
                min_page=R.dimen.min_page,
                curr_page=self.curr_page,
                max_page=n_pages(per_page=self.per_page, n_items=n_products)
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
        for idx, product in enumerate(self.q.slice(
                *get_page_range(curr_page=self.curr_page, per_page=self.per_page, min_page=R.dimen.min_page)).all()):
            rows.append([
                product.active,
                product.category.name,
                product.subcategory.name if product.subcategory else R.string.empty_subcategory_symbol,
                product.title,
                str(product.price).replace(".", ","),
                product.stock,
                product.min_stock,
                product.sales_number,
                [
                    dict(
                        type=R.id.ACTION_TYPE_LINK_BUTTON,
                        text=R.string.edit,
                        classes=R.string.edit_class,
                        href=url_for("admin_products.edit_product", product_id=product.id),
                    ),
                    dict(
                        type=R.id.ACTION_TYPE_INT_WITH_BUTTON,
                        form=AddToStockForm(),
                        classes=R.string.add_to_stock_class,
                        text=R.string.add_to_stock,
                        doing_text=R.string.adding,
                        url=url_for("admin_products.product_stock_addition", product_id=product.id),
                        error_4xx_msg=R.string.stock_change_invalid_form_error(product.title),
                        error_5xx_msg=R.string.stock_change_error(product.title)
                    ),
                    dict(
                        type=R.id.ACTION_TYPE_INT_WITH_BUTTON,
                        form=RemoveFromStockForm(),
                        classes=R.string.remove_from_stock_class,
                        text=R.string.remove_from_stock,
                        doing_text=R.string.removing,
                        url=url_for("admin_products.product_stock_removal", product_id=product.id),
                        error_4xx_msg=R.string.stock_change_invalid_form_error(product.title),
                        error_5xx_msg=R.string.stock_change_error(product.title)
                    ),
                    dict(
                        type=R.id.ACTION_TYPE_INT_WITH_BUTTON,
                        form=UpdateStockForm(),
                        classes=R.string.update_stock_class,
                        text=R.string.update_stock,
                        doing_text=R.string.updating,
                        url=url_for("admin_products.product_stock_update", product_id=product.id),
                        error_4xx_msg=R.string.stock_change_invalid_form_error(product.title),
                        error_5xx_msg=R.string.stock_change_error(product.title)
                    ),
                    dict(
                        type=R.id.ACTION_TYPE_ACTIVATE_DISABLE_BUTTON,
                        active=product.active,
                        to_activate_text=R.string.to_activate,
                        activating_text=R.string.activating,
                        active_col=R.string.product_active_col_id,
                        to_activate_url=url_for(
                            "admin_products.to_activate_product", product_id=product.id),
                        error_to_activate_msg=R.string.to_activate_product_error(product.title),
                        disable_text=R.string.disable,
                        disabling_text=R.string.disabling,
                        disable_url = url_for(
                                "admin_products.disable_product", product_id=product.id),
                        error_disable_msg=R.string.disable_product_error(product.title)
                    ),
                ]
            ])

        return dict(
            id=R.string.products_table_id,
            cols=[
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
                    id=R.string.product_stock_col_id,
                    title=R.string.in_stock,
                    type=R.id.COL_TYPE_TEXT,
                ),
                dict(
                    id=R.string.product_min_stock_col_id,
                    title=R.string.min_stock,
                    type=R.id.COL_TYPE_TEXT,
                    tooltip=R.string.min_stock_tooltip
                ),
                dict(
                    id=R.string.product_sales_number_col_id,
                    title=R.string.sales,
                    type=R.id.COL_TYPE_TEXT,
                ),
                dict(
                    id=R.string.action_col_id,
                    type=R.id.COL_TYPE_ACTION,
                    expandable=False
                )
            ],
            rows=rows
        )


admin_products_data_provider = AdminProductsDataProvider()
