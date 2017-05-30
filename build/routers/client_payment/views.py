# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template

from routers.client_payment import client_payment_blueprint
from routers.client_payment.data_providers.payment import client_payment_data_provider


@client_payment_blueprint.route("/")
def payment():
    return render_template("client_payment/payment.html", data=client_payment_data_provider.get_data())
