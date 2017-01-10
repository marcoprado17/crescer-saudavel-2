# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 10/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import current_app
from flask import url_for

from components.data_providers.paginator import paginator_data_provider
from components.data_providers.super_table import super_table_data_provider
from flask_bombril.utils import get_page_range
from flask_bombril.utils import n_pages
from flask_bombril.url_args import get_valid_page
from flask_bombril.url_args import get_valid_enum
from models.order import Order
from r import R
from routers.admin_orders.forms import AdminOrderFilterForm
from wrappers.base.forms import SubmitForm


class AdminOrdersDataProvider(object):
    def get_data(self):
        order_status_id = get_valid_enum(arg_name=R.string.order_status_id_arg_name, enum=R.id,
                                        default=R.id.ORDER_STATUS_PAID, possible_values=Order.order_status_ids)
        sort_method_id = get_valid_enum(arg_name=R.string.sort_method_arg_name, enum=R.id,
                                        default=R.id.SORT_METHOD_NEWEST, possible_values=Order.sort_method_ids)

        self.q = Order.query
        if order_status_id != R.id.ORDER_STATUS_ANY:
            self.q = self.q.filter(Order.status == order_status_id)
        self.q = self.q.order_by(Order.sort_method_by_id[sort_method_id])

        n_orders = self.q.count()

        self.per_page = current_app.config["DEFAULT_PER_PAGE"]
        self.curr_page = get_valid_page(page_arg_name=R.string.page_arg_name, per_page=self.per_page,
                                        n_items=n_orders)

        filter_form = AdminOrderFilterForm()
        filter_form.set_values(order_status_id=order_status_id)

        return dict(
            n_items=n_orders,
            paginator_data=paginator_data_provider.get_data(
                min_page=R.dimen.min_page,
                curr_page=self.curr_page,
                max_page=n_pages(per_page=self.per_page, n_items=n_orders)
            ),
            filter_data=dict(
                filter_form=filter_form
            ),
            sort_methods=super_table_data_provider.get_sort_methods_data(
                selected_sort_method_id=sort_method_id,
                sort_method_ids=Order.sort_method_ids,
                sort_method_names=Order.sort_method_names
            ),
            table_data=self.get_table_data()
        )

    def get_table_data(self):
        rows = []
        for idx, order in enumerate(self.q.slice(
                *get_page_range(curr_page=self.curr_page, per_page=self.per_page, min_page=R.dimen.min_page)).all()):
            rows.append([
                "#" + str(order.id),
                order.client_email,
                str(order.products_total_price),
                order.get_status_as_string(),
                str(order.paid_datetime)[0:R.dimen.datetime_important_chars_size],
                str(order.sent_datetime)[0:R.dimen.datetime_important_chars_size] if order.sent_datetime else "",
                str(order.delivered_datetime)[0:R.dimen.datetime_important_chars_size] if order.delivered_datetime else "",
                [
                    dict(
                        type=R.id.ACTION_TYPE_BUTTON,
                        text=R.string.details,
                        classes="details"
                    )
                ] + self.get_actions(order)
            ])

        return dict(
            id="orders-table",
            cols=[
                dict(
                    id="client-email",
                    title=R.string.id,
                    type=R.id.COL_TYPE_TEXT
                ),
                dict(
                    id="client-email",
                    title=R.string.client_email,
                    type=R.id.COL_TYPE_TEXT
                ),
                dict(
                    id="products-total-price",
                    title=R.string.price,
                    type=R.id.COL_TYPE_TEXT,
                    tooltip=R.string.order_products_price_tooltip
                ),
                dict(
                    id="status",
                    title=R.string.status,
                    type=R.id.COL_TYPE_TEXT
                ),
                dict(
                    id="paid-datetime",
                    title=R.string.paid_date,
                    type=R.id.COL_TYPE_TEXT,
                    tooltip=R.string.paid_date_tooltip
                ),
                dict(
                    id="sent-datetime",
                    title=R.string.sent_date,
                    type=R.id.COL_TYPE_TEXT,
                    tooltip=R.string.sent_date_tooltip
                ),
                dict(
                    id="delivered-datetime",
                    title=R.string.delivered_date,
                    type=R.id.COL_TYPE_TEXT,
                    tooltip=R.string.delivered_date_tooltip
                ),
                dict(
                    id="action",
                    type=R.id.COL_TYPE_ACTION,
                    expandable=False
                )
            ],
            rows=rows
        )

    def get_actions(self, order):
        if order.status == R.id.ORDER_STATUS_PAID:
            return [self.mark_as_sent_action(order)]
        elif order.status == R.id.ORDER_STATUS_SENT:
            return [self.unmark_as_sent_action(order), self.mark_as_delivered_action(order)]
        elif order.status == R.id.ORDER_STATUS_DELIVERED:
            return [self.unmark_as_delivered_action(order)]

    @staticmethod
    def mark_as_sent_action(order):
        return dict(
            type=R.id.ACTION_TYPE_BUTTON,
            text=R.string.mark_as_sent,
            form=SubmitForm(),
            url=url_for("admin_orders.mark_as_sent", order_id=order.id),
            classes="mark-as-sent",
        )

    @staticmethod
    def unmark_as_sent_action(order):
        return dict(
            type=R.id.ACTION_TYPE_BUTTON,
            text=R.string.unmark_as_sent,
            form=SubmitForm(),
            url=url_for("admin_orders.unmark_as_sent", order_id=order.id),
            classes="unmark-as-sent",
        )

    @staticmethod
    def mark_as_delivered_action(order):
        return dict(
            type=R.id.ACTION_TYPE_BUTTON,
            text=R.string.mark_as_delivered,
            form=SubmitForm(),
            url=url_for("admin_orders.mark_as_delivered", order_id=order.id),
            classes="mark-as-delivered",
        )

    @staticmethod
    def unmark_as_delivered_action(order):
        return dict(
            type=R.id.ACTION_TYPE_BUTTON,
            text=R.string.unmark_as_delivered,
            form=SubmitForm(),
            url=url_for("admin_orders.unmark_as_delivered", order_id=order.id),
            classes="unmark-as-delivered",
        )

admin_orders_data_provider = AdminOrdersDataProvider()
