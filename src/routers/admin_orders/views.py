# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 24/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.admin_orders import admin_orders_blueprint


@admin_orders_blueprint.route("/")
def index():
    return "Pedidos."
