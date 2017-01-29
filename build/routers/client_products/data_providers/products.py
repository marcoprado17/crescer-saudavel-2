# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 28/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from pprint import pprint

from flask import current_app
from flask import url_for
from sqlalchemy import desc

from components.data_providers.paginator import paginator_data_provider
from flask_bombril.utils import get_page_range
from flask_bombril.utils import n_pages
from flask_bombril.utils import get_url_args
from flask_bombril.url_args import get_valid_enum
from flask_bombril.url_args import get_valid_page
from flask_bombril.utils import get_url_arg
from flask_bombril.url_args import get_valid_model_id
from models.product import Product
from models.product_category import ProductCategory
from models.product_subcategory import ProductSubcategory
from r import R


class ClientProductsDataProvider(object):
    def get_data(self):
        category_id = get_valid_model_id(model=ProductCategory, arg_name=R.string.category_id_arg_name,
                                         include_zero=True, default=0)
        subcategory_id = get_valid_model_id(model=ProductSubcategory, arg_name=R.string.subcategory_id_arg_name,
                                            include_zero=True, default=0)
        search_string = get_url_arg(R.string.search_string_arg_name, "")

        sort_method_id = get_valid_enum(arg_name=R.string.sort_method_arg_name, enum=R.id,
                                        default=R.id.SORT_METHOD_NAME,
                                        possible_values=Product.client_sort_method_map.ids)

        q = Product.query
        q = q.filter(Product.active == True)
        q = q.order_by(desc(Product.is_available_to_client), *Product.client_sort_method_map.order(sort_method_id))

        page_heading_title = R.string.products
        page_heading_path = [
            dict(
                name=R.string.home,
                href=url_for("client_home.home")
            ),
            dict(
                name=R.string.products
            )
        ]

        if category_id != 0 and subcategory_id == 0:
            q = q.filter(Product.category_id == category_id)
            category = ProductCategory.get(category_id)
            page_heading_title = R.string.get_products_by_category_title(category.name)
            page_heading_path.pop()
            page_heading_path.append(
                dict(
                    name=R.string.products,
                    href=url_for("client_products.products")
                )
            )
            page_heading_path.append(
                dict(
                    name=category.name
                )
            )
        elif subcategory_id != 0:
            q = q.filter(Product.subcategory_id == subcategory_id)
            subcategory = ProductSubcategory.get(subcategory_id)
            page_heading_title = R.string.get_products_by_subcategory_title(subcategory.name)
            page_heading_path.pop()
            page_heading_path.append(
                dict(
                    name=R.string.products,
                    href=url_for("client_products.products")
                )
            )
            page_heading_path.append(
                dict(
                    name=subcategory.category.name,
                    href=url_for("client_products.products", **{R.string.category_id_arg_name: subcategory.category_id})
                )
            )
            page_heading_path.append(
                dict(
                    name=subcategory.name
                )
            )
        elif search_string != "":
            # TODO: Implement filter of search
            page_heading_title = R.string.get_products_by_search_title(search_string)
            page_heading_path.pop()
            page_heading_path.append(
                dict(
                    name=R.string.products,
                    href=url_for("client_products.products")
                )
            )
            page_heading_path.append(
                dict(
                    name=R.string.search
                )
            )

        n_products = q.count()

        per_page = current_app.config["CLIENT_PRODUCTS_PER_PAGE"]
        curr_page = get_valid_page(page_arg_name=R.string.page_arg_name, per_page=per_page, n_items=n_products)

        return dict(
            page_heading_data=dict(
                path=page_heading_path,
                title=page_heading_title
            ),
            sort_methods=self.get_sort_methods_data(
                selected_sort_method_id=sort_method_id,
                sort_method_map=Product.client_sort_method_map,
            ),
            paginator_data=paginator_data_provider.get_data(
                min_page=R.dimen.min_page,
                curr_page=curr_page,
                max_page=n_pages(per_page=per_page, n_items=n_products)
            ),
            products=q.slice(*get_page_range(curr_page=curr_page, per_page=per_page, min_page=R.dimen.min_page)).all()
        )

    def get_sort_methods_data(self, selected_sort_method_id, sort_method_map):
        sort_method_ids = sort_method_map.ids
        sort_method_names = sort_method_map.names
        sort_method_data = []
        url_args = get_url_args()
        for sort_method_id, sort_method_name in zip(sort_method_ids, sort_method_names):
            url_args[R.string.sort_method_arg_name] = sort_method_id.value
            sort_method_data.append(
                dict(
                    name=sort_method_name,
                    href=url_for("client_products.products", **url_args),
                    selected=sort_method_id == selected_sort_method_id
                )
            )
        return sort_method_data


client_products_data_provider = ClientProductsDataProvider()
