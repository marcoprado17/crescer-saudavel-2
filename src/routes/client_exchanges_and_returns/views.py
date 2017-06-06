# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template

from routes.client_exchanges_and_returns import client_exchanges_and_returns_blueprint
from routes.client_exchanges_and_returns.data_providers.exchanges_and_returns import \
    client_exchanges_and_returns_data_provider


@client_exchanges_and_returns_blueprint.route("/")
def exchanges_and_returns():
    return render_template("client_exchanges_and_returns/exchanges_and_returns.html", data=client_exchanges_and_returns_data_provider.get_data())
