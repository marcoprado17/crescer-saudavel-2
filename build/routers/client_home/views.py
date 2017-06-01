# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template
from routers.client_home import client_home_blueprint
from routers.client_home.data_providers.home import client_home_data_provider


@client_home_blueprint.route("/")
def home():
    return render_template("client_home/home.html", data=client_home_data_provider.get_data())

