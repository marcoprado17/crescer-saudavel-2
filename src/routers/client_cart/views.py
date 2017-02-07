# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask_login import login_required
from routers.client_cart import client_cart_blueprint


@client_cart_blueprint.route("/")
@login_required
def cart():
    return "Carrinho."
