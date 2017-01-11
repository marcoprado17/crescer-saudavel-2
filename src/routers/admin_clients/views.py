# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 24/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.admin_clients import admin_clients_blueprint


@admin_clients_blueprint.route("/")
def index():
    return "Clientes."
