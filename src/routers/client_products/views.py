# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.client_products import client_products_blueprint


@client_products_blueprint.route("/")
def products():
    return "Produtos."


@client_products_blueprint.route("/<int:product_id>")
def product(product_id):
    return "Produto  #" + str(product_id) + "."
