# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
from flask import url_for, request, redirect, flash
from flask_admin import expose
from markupsafe import Markup

from models.order import Order
from models_view.proj_base_view import ProjBaseView
from proj_decorators import protect_against_csrf
from r import R


class OrderView(ProjBaseView):
    # noinspection PyMethodMayBeStatic,PyMethodParameters,PyUnusedLocal
    def _products_formatter(view, context, model, name):
        table_rows = []
        for product_row in model.products_data:
            product_id = product_row[0]
            product_title = product_row[1]
            product_price = product_row[2]
            amount = product_row[3]
            subtotal = product_row[4]
            table_rows. append("<tr>")
            table_rows.append("<td><a href='%s'><b>#%s - %s</b></a></td>" % (
                url_for(R.string.products_endpoint+".details_view", id=product_id),
                product_id,
                product_title))
            table_rows.append("<td>%s</td>" % product_price)
            table_rows.append("<td>%s</td>" % amount)
            table_rows.append("<td>%s</td>" % subtotal)
            table_rows.append("</tr>")
        html = [
            "<table class='table'>",
            "   <tr>",
            "       <th style='border-top: 0;'>%s</th>" % R.string.product,
            "       <th style='border-top: 0;'>%s</th>" % R.string.price,
            "       <th style='border-top: 0;'>%s</th>" % R.string.quantity,
            "       <th style='border-top: 0;'>%s</th>" % R.string.subtotal,
            "   </tr>"
        ]
        for table_row in table_rows:
            html.append(table_row)
        html.append("</table>")
        return Markup(''.join(html))

    name = R.string.orders
    endpoint = R.string.orders_endpoint

    list_template = "admin/order_list.html"

    can_create = False
    can_delete = False
    can_edit = False
    can_view_details = True

    column_display_actions = [
        "oi"
    ]
    column_details_exclude_list = [
        "client",
        "uuid",
        "amount_by_product_id",
        "total_table_data"
    ]
    column_details_list = [
        "id",
        "client_email",
        "status",
        "paid_datetime",
        "sent_datetime",
        "delivered_datetime",
        "products",
        "products_total_price",
        "freight",
        "total_price"
    ]
    column_formatters = dict(
        client_email=lambda view, context, model, name:
        Markup("<a href=%s>%s</a>" % (
            url_for(R.string.clients_endpoint + ".details_view", id=model.client_id), model.client_email)),
        status=lambda view, context, model, name:
        model.order_status_map[model.status],
        paid_datetime=lambda view, context, model, name:
        R.string.default_datetime_format(model.paid_datetime) if model.paid_datetime is not None
        else R.string.empty_symbol,
        sent_datetime=lambda view, context, model, name:
        R.string.default_datetime_format(model.sent_datetime) if model.sent_datetime is not None
        else R.string.empty_symbol,
        delivered_datetime=lambda view, context, model, name:
        R.string.default_datetime_format(model.delivered_datetime) if model.delivered_datetime is not None
        else R.string.empty_symbol,
        products_total_price=lambda view, context, model, name:
        R.string.format_price(model.products_total_price),
        freight=lambda view, context, model, name:
        R.string.format_price(model.freight),
        total_price=lambda view, context, model, name:
        R.string.format_price(model.products_total_price + model.freight),
        products=_products_formatter,
    )
    column_list = [
        "id",
        "client_email",
        "status",
        "paid_datetime",
        "sent_datetime",
        "delivered_datetime",
        "total_price"
    ]
    column_sortable_list = [
        "id",
        "client_email",
        "status",
        "paid_datetime",
        "sent_datetime",
        "delivered_datetime",
    ]

    @expose("/mudar-status", methods=["POST"])
    @protect_against_csrf
    def change_status(self):
        send_email = True if "send_email" in request.form else False
        new_status = R.id(int(request.form.get("new_status")))
        order_id = int(request.form.get("order_id"))
        url = request.form.get("url")

        order = Order.get(order_id)

        if order.status == R.id.ORDER_STATUS_CANCELED and new_status == R.id.ORDER_STATUS_PAID:
            order.mark_as_paid()
            if send_email:
                # TODO: Send email
                pass
        elif order.status == R.id.ORDER_STATUS_PAID and new_status == R.id.ORDER_STATUS_CANCELED:
            order.mark_as_canceled()
            if send_email:
                # TODO: Send email
                pass
        elif order.status == R.id.ORDER_STATUS_PAID and new_status == R.id.ORDER_STATUS_SENT:
            order.mark_as_sent()
            if send_email:
                # TODO: Send email
                pass
        elif order.status == R.id.ORDER_STATUS_SENT and new_status == R.id.ORDER_STATUS_PAID:
            order.unmark_as_sent()
            if send_email:
                # TODO: Send email
                pass
        elif order.status == R.id.ORDER_STATUS_SENT and new_status == R.id.ORDER_STATUS_DELIVERED:
            order.mark_as_delivered()
            if send_email:
                # TODO: Send email
                pass
        elif order.status == R.id.ORDER_STATUS_DELIVERED and new_status == R.id.ORDER_STATUS_SENT:
            order.unmark_as_delivered()
            if send_email:
                # TODO: Send email
                pass

        flash(R.string.order_status_successfully_changed_message(order.id, order.status), 'success')
        return redirect(url)
