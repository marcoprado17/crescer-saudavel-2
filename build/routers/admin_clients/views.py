# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 24/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template
from routers.admin_clients import admin_clients_blueprint
from routers.admin_clients.data_providers.index import admin_clients_data_provider


@admin_clients_blueprint.route("/")
def index():
    return render_template("admin_clients/index.html", data=admin_clients_data_provider.get_data())
