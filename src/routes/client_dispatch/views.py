# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template

from routes.client_dispatch import client_dispatch_blueprint
from routes.client_dispatch.data_providers.dispatch import client_dispatch_data_provider


@client_dispatch_blueprint.route("/")
def dispatch():
    return render_template("client_dispatch/dispatch.html", data=client_dispatch_data_provider.get_data())
