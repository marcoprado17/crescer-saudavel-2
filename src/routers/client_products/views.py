# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template
from routers.client_products import client_products_blueprint
from routers.client_products.data_providers.products import client_products_data_provider


@client_products_blueprint.route("/")
def products():
    return render_template("client_products/products.html", data=client_products_data_provider.get_data())


@client_products_blueprint.route("/<int:product_id>")
def product(product_id):
    return "Produto  #" + str(product_id) + "."
