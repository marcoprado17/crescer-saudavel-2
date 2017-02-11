# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template
from routers.client_cart import client_cart_blueprint
from routers.client_cart.data_providers.cart import client_cart_data_provider


@client_cart_blueprint.route("/")
def cart():
    return render_template("client_cart/cart.html", data=client_cart_data_provider.get_data())


@client_cart_blueprint.route("/remover-tudo", methods=["POST"])
def remove_all():
    print("Remove all items of cart!!!")
    return "", 200
