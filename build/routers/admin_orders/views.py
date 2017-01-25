# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 24/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import json

from flask import render_template
from proj_decorators import valid_form, safe_id_to_model_elem
from proj_exceptions import InsufficientStockToSendOrder
from proj_forms import SubmitForm
from models.order import Order
from r import R
from routers.admin_orders import admin_orders_blueprint
from routers.admin_orders.data_providers.orders import admin_orders_data_provider


@admin_orders_blueprint.route("/")
def orders():
    return render_template("admin_orders/orders.html", data=admin_orders_data_provider.get_data())


# noinspection PyUnresolvedReferences
@admin_orders_blueprint.route("/marcar-como-enviado/<int:order_id>", methods=["POST"])
@valid_form(FormClass=SubmitForm)
@safe_id_to_model_elem(model=Order)
def mark_as_sent(order, form):
    # TODO: Sent email to client
    try:
        order.mark_as_sent()
        return json.dumps(
            dict(
                new_status=order.get_status_as_string(),
                new_sent_datetime=order.get_formatted_sent_datetime()
            )
        ), 200
    except InsufficientStockToSendOrder as e:
        return json.dumps(
            dict(
                error_message=R.string.product_stock_insufficient_to_send_order(e.limiting_product)
            )
        ), 409


# noinspection PyUnresolvedReferences
@admin_orders_blueprint.route("/desmarcar-como-enviado/<int:order_id>", methods=["POST"])
@valid_form(FormClass=SubmitForm)
@safe_id_to_model_elem(model=Order)
def unmark_as_sent(order, form):
    order.unmark_as_sent()
    return json.dumps(
        dict(
            new_status=order.get_status_as_string(),
            new_sent_datetime=order.get_formatted_sent_datetime()
        )
    ), 200


# noinspection PyUnresolvedReferences
@admin_orders_blueprint.route("/marcar-como-entregue/<int:order_id>", methods=["POST"])
@valid_form(FormClass=SubmitForm)
@safe_id_to_model_elem(model=Order)
def mark_as_delivered(order, form):
    order.mark_as_delivered()
    return json.dumps(
        dict(
            new_status=order.get_status_as_string(),
            new_delivered_datetime=order.get_formatted_delivered_datetime()
        )
    ), 200


# noinspection PyUnresolvedReferences
@admin_orders_blueprint.route("/desmarcar-como-entregue/<int:order_id>", methods=["POST"])
@valid_form(FormClass=SubmitForm)
@safe_id_to_model_elem(model=Order)
def unmark_as_delivered(order, form):
    order.unmark_as_delivered()
    return json.dumps(
        dict(
            new_status=order.get_status_as_string(),
            new_delivered_datetime=order.get_formatted_delivered_datetime()
        )
    ), 200


# noinspection PyUnresolvedReferences
@admin_orders_blueprint.route("/cancelar-pedido/<int:order_id>", methods=["POST"])
@valid_form(FormClass=SubmitForm)
@safe_id_to_model_elem(model=Order)
def mark_as_canceled(order, form):
    # TODO: Sent email to client
    order.mark_as_canceled()
    return json.dumps(
        dict(
            new_status=order.get_status_as_string()
        )
    ), 200


# noinspection PyUnresolvedReferences
@admin_orders_blueprint.route("/marcar-como-pago/<int:order_id>", methods=["POST"])
@valid_form(FormClass=SubmitForm)
@safe_id_to_model_elem(model=Order)
def mark_as_paid(order, form):
    order.mark_as_paid()
    return json.dumps(
        dict(
            new_status=order.get_status_as_string()
        )
    ), 200
