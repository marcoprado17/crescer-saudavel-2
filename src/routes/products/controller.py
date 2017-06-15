# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template, abort, url_for

from models.product.product import Product
from r import R
from routes.products import products_blueprint
from routes.products.data_providers.products import client_products_data_provider


@products_blueprint.route("/")
def products():
    return render_template("client_products/products.html", data=client_products_data_provider.get_data())


@products_blueprint.route("/<int:product_id>")
def product(product_id):
    product = Product.get(product_id)
    if product is None:
        abort(404)

    breadcumb = [(R.string.home, url_for("home.home"))]
    if product.category is not None:
        breadcumb.append((product.category.name, product.category.get_href()))
    if product.subcategory is not None:
        breadcumb.append((product.subcategory.name, product.subcategory.get_href()))
    breadcumb.append(product.title)

    more_products = Product.query.filter(Product.category_id == product.category_id, Product.active == True).all()
    more_products = [p for p in more_products if p.is_available_to_client][0:4]

    return render_template(
        "products/product.html",
        product=product,
        breadcumb=breadcumb,
        more_products=more_products
    )
