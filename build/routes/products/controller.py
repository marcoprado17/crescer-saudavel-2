# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template, abort, url_for
from sqlalchemy import desc

from components.data_providers.header import header_data_provider
from flask_bombril.utils.utils import get_int_from_request_arg, get_string_from_request_arg
from models.product.product import Product
from models.product.product_category import ProductCategory
from models.product.product_subcategory import ProductSubcategory
from r import R
from routes.products import products_blueprint


@products_blueprint.route("/")
def products():
    page = get_int_from_request_arg(R.string.page_arg_name, 1)
    sort_method_id = get_int_from_request_arg(R.string.sort_method_arg_name, R.id.SORT_METHOD_TITLE.value)

    category_id = get_int_from_request_arg(R.string.category_id_arg_name, 0)
    header_data_provider.current_category_id = category_id
    subcategory_id = get_int_from_request_arg(R.string.subcategory_id_arg_name, 0)
    q = get_string_from_request_arg(R.string.search_query_arg_name, default="")

    products_query = Product.query.filter(Product.active == True, Product.category_active == True, Product.subcategory_active == True)

    breadcumb = []

    if subcategory_id != 0:
        subcategory = ProductSubcategory.get(subcategory_id)
        if (subcategory is None) or (not subcategory.active) or (not subcategory.product_category.active):
            abort(404)
        products_query = products_query.filter(Product.subcategory_id == subcategory_id)
        breadcumb.append((R.string.home, url_for("home.home")))
        breadcumb.append((subcategory.product_category.name, subcategory.product_category.get_href()))
        breadcumb.append((subcategory.name, subcategory.get_href()))
    elif category_id != 0:
        category = ProductCategory.get(category_id)
        if (category is None) or (not category.active):
            abort(404)
        products_query = products_query.filter(Product.category_id == category_id)
        breadcumb.append((R.string.home, url_for("home.home")))
        breadcumb.append((category.name, category.get_href()))
    elif q != "":
        products_query = products_query.whoosh_search(q, or_=True)
        breadcumb.append((R.string.home, url_for("home.home")))
        breadcumb.append(R.string.search_for(q))
    else:
        breadcumb.append((R.string.home, url_for("home.home")))
        breadcumb.append(R.string.products)

    if sort_method_id == R.id.SORT_METHOD_TITLE.value:
        products_query = products_query.order_by(desc(Product.is_available_to_client), Product.title)
    elif sort_method_id == R.id.SORT_METHOD_LOWEST_PRICE.value:
        products_query = products_query.order_by(desc(Product.is_available_to_client), Product.price_with_discount)
    elif sort_method_id == R.id.SORT_METHOD_HIGHER_PRICE.value:
        products_query = products_query.order_by(desc(Product.is_available_to_client), desc(Product.price_with_discount))
    elif sort_method_id == R.id.SORT_METHOD_BEST_SELLER.value:
        products_query = products_query.order_by(desc(Product.is_available_to_client), desc(Product.sales_number))

    products_pagination = products_query.paginate(page=page, per_page=R.dimen.n_products_per_page)

    return render_template(
        "products/products.html",
        products_pagination=products_pagination,
        breadcumb=breadcumb,
        sort_method_id=sort_method_id
    )


@products_blueprint.route("/<int:product_id>")
def product(product_id):
    product = Product.get(product_id)
    if (product is None) or \
            (not product.category.active) or \
            (product.subcategory and not product.subcategory.active):
        abort(410)

    header_data_provider.current_category_id = product.category_id

    breadcumb = [(R.string.home, url_for("home.home"))]
    if product.category is not None:
        breadcumb.append((product.category.name, product.category.get_href()))
    if product.subcategory is not None:
        breadcumb.append((product.subcategory.name, product.subcategory.get_href()))
    breadcumb.append(product.title)

    more_products = Product.query.filter(Product.category_id == product.category_id, Product.is_available_to_client == True).limit(4).all()

    return render_template(
        "products/product.html",
        product=product,
        breadcumb=breadcumb,
        more_products=more_products
    )
