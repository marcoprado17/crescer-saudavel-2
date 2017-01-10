# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 24/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.admin_orders import admin_orders_blueprint
from flask import render_template
from routers.admin_orders.data_providers.index import admin_orders_data_provider


@admin_orders_blueprint.route("/")
def index():
    return render_template("admin_orders/index.html", data=admin_orders_data_provider.get_data())


@admin_orders_blueprint.route("/marcar-como-enviado/<int:order_id>", methods=["POST"])
def mark_as_sent(order_id):
    return "mark_as_sent"

@admin_orders_blueprint.route("/desmarcar-como-enviado/<int:order_id>", methods=["POST"])
def unmark_as_sent(order_id):
    return "unmark_as_sent"

@admin_orders_blueprint.route("/marcar-como-entregue/<int:order_id>", methods=["POST"])
def mark_as_delivered(order_id):
    return "mark_as_delivered"

@admin_orders_blueprint.route("/desmarcar-como-entregue/<int:order_id>", methods=["POST"])
def unmark_as_delivered(order_id):
    return "unmark_as_delivered"