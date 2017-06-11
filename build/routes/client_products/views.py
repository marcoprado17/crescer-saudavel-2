# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template
from models.product.product import Product
from proj_decorators import safe_id_to_model_elem
from routes.client_products import client_products_blueprint
from routes.client_products.data_providers.product import client_product_data_provider
from routes.client_products.data_providers.products import client_products_data_provider


@client_products_blueprint.route("/")
def products():
    return render_template("client_products/products.html", data=client_products_data_provider.get_data())


# noinspection PyUnresolvedReferences
@client_products_blueprint.route("/<int:product_id>")
@safe_id_to_model_elem(model=Product)
def product(product):
    return render_template("client_products/product_2.html", data=client_product_data_provider.get_data(product))
