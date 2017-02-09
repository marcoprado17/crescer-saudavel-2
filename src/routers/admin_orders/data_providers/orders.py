# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 10/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import current_app
from flask import url_for
from components.data_providers.paginator import paginator_data_provider
from flask_bombril.url_args import get_valid_enum
from flask_bombril.url_args import get_valid_page
from flask_bombril.utils import get_page_range
from flask_bombril.utils import n_pages
from proj_forms import SubmitForm
from models.order import Order
from proj_utils import get_sort_methods_data
from r import R
from routers.admin_orders.forms import AdminOrderFilterForm


class AdminOrdersDataProvider(object):
    def get_data(self):
        order_status_id = get_valid_enum(arg_name=R.string.order_status_id_arg_name, enum=R.id,
                                        default=R.id.ORDER_STATUS_PAID, possible_values=Order.order_status_map.keys())
        sort_method_id = get_valid_enum(arg_name=R.string.sort_method_arg_name, enum=R.id,
                                        default=R.id.SORT_METHOD_NEWEST, possible_values=Order.sort_method_map.ids)

        self.q = Order.query
        if order_status_id != R.id.ORDER_STATUS_ANY:
            self.q = self.q.filter(Order.status == order_status_id)
        self.q = self.q.order_by(*Order.sort_method_map.order(sort_method_id))

        n_orders = self.q.count()

        self.per_page = current_app.config["ORDERS_TABLE_PER_PAGE"]
        self.curr_page = get_valid_page(page_arg_name=R.string.page_arg_name, per_page=self.per_page,
                                        n_items=n_orders)

        self.orders_in_page = self.q.slice(
                *get_page_range(curr_page=self.curr_page, per_page=self.per_page, min_page=R.dimen.min_page)).all()

        return dict(
            n_items=n_orders,
            paginator_data=paginator_data_provider.get_data(
                min_page=R.dimen.min_page,
                curr_page=self.curr_page,
                max_page=n_pages(per_page=self.per_page, n_items=n_orders)
            ),
            filter_data=dict(
                filter_form=AdminOrderFilterForm(order_status_id=order_status_id)
            ),
            sort_methods=get_sort_methods_data(
                selected_sort_method_id=sort_method_id,
                sort_method_map=Order.sort_method_map
            ),
            table_data=self.get_table_data(),
            orders_in_page=self.orders_in_page
        )


    def get_table_data(self):
        rows = []
        for idx, order in enumerate(self.orders_in_page):
            rows.append([
                order.uuid,
                order.client_email,
                order.get_formatted_total_price(),
                order.get_status_as_string(),
                order.get_formatted_paid_datetime(),
                order.get_formatted_sent_datetime() if order.sent_datetime else R.string.empty_symbol,
                order.get_formatted_delivered_datetime() if order.delivered_datetime else R.string.empty_symbol,
                [
                    dict(
                        type=R.id.ACTION_TYPE_BUTTON,
                        text=R.string.details,
                        classes="details",
                        meta_data = {
                            "data-toggle": "modal",
                            "data-target": "#modal-" + str(idx)
                        }
                    )
                ] + self.get_actions(order)
            ])

        return dict(
            id="orders-table",
            expandable=True,
            cols=[
                dict(
                    id="order-id",
                    title=R.string.id,
                    type=R.id.COL_TYPE_MIN_UUID
                ),
                dict(
                    id="client-email",
                    title=R.string.client_email,
                    type=R.id.COL_TYPE_TEXT
                ),
                dict(
                    id="products-total-price",
                    title=R.string.total,
                    type=R.id.COL_TYPE_TEXT,
                    tooltip=R.string.order_total_tooltip
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
                    type=R.id.COL_TYPE_ACTION
                )
            ],
            rows=rows
        )

    def get_actions(self, order):
        if order.status == R.id.ORDER_STATUS_PAID:
            return [
                self.mark_as_sent_action(order, False),
                self.unmark_as_sent_action(order, True),
                self.mark_as_delivered_action(order, True),
                self.unmark_as_delivered_action(order, True),
                self.mark_as_canceled_action(order, False),
                self.mark_as_paid_action(order, True)
            ]
        elif order.status == R.id.ORDER_STATUS_SENT:
            return [
                self.mark_as_sent_action(order, True),
                self.unmark_as_sent_action(order, False),
                self.mark_as_delivered_action(order, False),
                self.unmark_as_delivered_action(order, True),
                self.mark_as_canceled_action(order, True),
                self.mark_as_paid_action(order, True)
            ]
        elif order.status == R.id.ORDER_STATUS_DELIVERED:
            return [
                self.mark_as_sent_action(order, True),
                self.unmark_as_sent_action(order, True),
                self.mark_as_delivered_action(order, True),
                self.unmark_as_delivered_action(order, False),
                self.mark_as_canceled_action(order, True),
                self.mark_as_paid_action(order, True)
            ]
        elif order.status == R.id.ORDER_STATUS_CANCELED:
            return [
                self.mark_as_sent_action(order, True),
                self.unmark_as_sent_action(order, True),
                self.mark_as_delivered_action(order, True),
                self.unmark_as_delivered_action(order, True),
                self.mark_as_canceled_action(order, True),
                self.mark_as_paid_action(order, False)
            ]

    def mark_as_sent_action(self, order, hidden):
        return dict(
            type=R.id.ACTION_TYPE_BUTTON,
            text=R.string.mark_as_sent,
            form=SubmitForm(),
            url=url_for("admin_orders.mark_as_sent", order_id=order.id),
            classes="mark-as-sent " + ("hidden" if hidden else ""),
            meta_data = self.get_meta_data(order)
        )

    def unmark_as_sent_action(self, order, hidden):
        return dict(
            type=R.id.ACTION_TYPE_BUTTON,
            text=R.string.unmark_as_sent,
            form=SubmitForm(),
            url=url_for("admin_orders.unmark_as_sent", order_id=order.id),
            classes="unmark-as-sent " + ("hidden" if hidden else ""),
            meta_data = self.get_meta_data(order)
        )

    def mark_as_delivered_action(self, order, hidden):
        return dict(
            type=R.id.ACTION_TYPE_BUTTON,
            text=R.string.mark_as_delivered,
            form=SubmitForm(),
            url=url_for("admin_orders.mark_as_delivered", order_id=order.id),
            classes="mark-as-delivered " + ("hidden" if hidden else ""),
            meta_data = self.get_meta_data(order)
        )

    def unmark_as_delivered_action(self, order, hidden):
        return dict(
            type=R.id.ACTION_TYPE_BUTTON,
            text=R.string.unmark_as_delivered,
            form=SubmitForm(),
            url=url_for("admin_orders.unmark_as_delivered", order_id=order.id),
            classes="unmark-as-delivered " + ("hidden" if hidden else ""),
            meta_data = self.get_meta_data(order)
        )

    def mark_as_canceled_action(self, order, hidden):
        return dict(
            type=R.id.ACTION_TYPE_BUTTON,
            text=R.string.cancel_order,
            form=SubmitForm(),
            url=url_for("admin_orders.mark_as_canceled", order_id=order.id),
            classes="mark-as-canceled " + ("hidden" if hidden else ""),
            meta_data = self.get_meta_data(order)
        )

    def mark_as_paid_action(self, order, hidden):
        return dict(
            type=R.id.ACTION_TYPE_BUTTON,
            text=R.string.mark_as_paid,
            form=SubmitForm(),
            url=url_for("admin_orders.mark_as_paid", order_id=order.id),
            classes="mark-as-paid " + ("hidden" if hidden else ""),
            meta_data = self.get_meta_data(order)
        )

    def get_meta_data(self, order):
        return {
            "data-order-id": str(order.id),
            "data-email": order.client_email
        }

admin_orders_data_provider = AdminOrdersDataProvider()
