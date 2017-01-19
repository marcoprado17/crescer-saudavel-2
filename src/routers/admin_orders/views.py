# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 24/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import json

from datetime import datetime

from models.order import Order
from r import R
from routers.admin_orders import admin_orders_blueprint
from flask import render_template
from routers.admin_orders.data_providers.index import admin_orders_data_provider
from wrappers.base.decorators import valid_form
from wrappers.base.forms import SubmitForm


@admin_orders_blueprint.route("/")
def index():
    data = admin_orders_data_provider.get_data()
    return render_template("admin_orders/index.html", data=data)


@admin_orders_blueprint.route("/marcar-como-enviado/<int:order_id>", methods=["POST"])
@valid_form(FormClass=SubmitForm)
def mark_as_sent(order_id):
    order = Order.get(order_id)
    assert order != None and order.status == R.id.ORDER_STATUS_PAID
    order = Order.update(
        order_id,
        status = R.id.ORDER_STATUS_SENT,
        sent_datetime = datetime.now()
    )
    return json.dumps(
        dict(
            new_status=order.get_status_as_string(),
            new_sent_datetime=order.get_formatted_sent_datetime()
        )
    ), 200

@admin_orders_blueprint.route("/desmarcar-como-enviado/<int:order_id>", methods=["POST"])
@valid_form(FormClass=SubmitForm)
def unmark_as_sent(order_id):
    order = Order.get(order_id)
    assert order != None and order.status == R.id.ORDER_STATUS_SENT
    order = Order.update(
        order_id,
        status=R.id.ORDER_STATUS_PAID,
        sent_datetime=None
    )
    return json.dumps(
        dict(
            new_status=order.get_status_as_string(),
            new_sent_datetime=order.get_formatted_sent_datetime()
        )
    ), 200

@admin_orders_blueprint.route("/marcar-como-entregue/<int:order_id>", methods=["POST"])
@valid_form(FormClass=SubmitForm)
def mark_as_delivered(order_id):
    order = Order.get(order_id)
    assert order != None and order.status == R.id.ORDER_STATUS_SENT
    order = Order.update(
        order_id,
        status=R.id.ORDER_STATUS_DELIVERED,
        delivered_datetime=datetime.now()
    )
    return json.dumps(
        dict(
            new_status=order.get_status_as_string(),
            new_delivered_datetime=order.get_formatted_delivered_datetime()
        )
    ), 200

@admin_orders_blueprint.route("/desmarcar-como-entregue/<int:order_id>", methods=["POST"])
@valid_form(FormClass=SubmitForm)
def unmark_as_delivered(order_id):
    order = Order.get(order_id)
    assert order != None and order.status == R.id.ORDER_STATUS_DELIVERED
    order = Order.update(
        order_id,
        status=R.id.ORDER_STATUS_SENT,
        delivered_datetime=None
    )
    return json.dumps(
        dict(
            new_status=order.get_status_as_string(),
            new_delivered_datetime=order.get_formatted_delivered_datetime()
        )
    ), 200


@admin_orders_blueprint.route("/cancelar-pedido/<int:order_id>", methods=["POST"])
@valid_form(FormClass=SubmitForm)
def mark_as_canceled(order_id):
    order = Order.get(order_id)
    assert order != None and order.status == R.id.ORDER_STATUS_PAID
    order = Order.update(
        order_id,
        status=R.id.ORDER_STATUS_CANCELED,
    )
    return json.dumps(
        dict(
            new_status=order.get_status_as_string()
        )
    ), 200

@admin_orders_blueprint.route("/marcar-como-pago/<int:order_id>", methods=["POST"])
@valid_form(FormClass=SubmitForm)
def mark_as_paid(order_id):
    order = Order.get(order_id)
    assert order != None and order.status == R.id.ORDER_STATUS_CANCELED
    order = Order.update(
        order_id,
        status=R.id.ORDER_STATUS_PAID,
    )
    return json.dumps(
        dict(
            new_status=order.get_status_as_string()
        )
    ), 200
