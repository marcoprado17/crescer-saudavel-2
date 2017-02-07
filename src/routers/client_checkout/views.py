# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask_login import login_required
from routers.client_checkout import client_checkout_blueprint


@client_checkout_blueprint.route("/")
@login_required
def checkout():
    return "Checkout."
