# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 24/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template
from flask_login import login_required
from proj_decorators import admin_required
from routers.admin_clients import admin_clients_blueprint
from routers.admin_clients.data_providers.clients import admin_clients_data_provider


@admin_clients_blueprint.route("/")
@login_required
@admin_required
def clients():
    return render_template("admin_clients/clients.html", data=admin_clients_data_provider.get_data())
