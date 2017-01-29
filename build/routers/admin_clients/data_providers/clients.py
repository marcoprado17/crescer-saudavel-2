# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 11/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import current_app
from components.data_providers.paginator import paginator_data_provider
from flask_bombril.url_args import get_valid_model_id
from flask_bombril.utils import n_pages
from flask_bombril.utils import get_page_range
from flask_bombril.url_args import get_valid_page
from flask_bombril.url_args import get_valid_enum
from models.city import City
from models.client import Client
from models.state import State
from proj_utils import get_sort_methods_data
from r import R
from routers.admin_clients.forms import AdminClientFilterForm


class AdminClientsDataProvider(object):
    def get_data(self):
        state_id = get_valid_model_id(model=State, arg_name=R.string.state_id_arg_name,
                                         include_zero=True, default=0)
        city_id = get_valid_model_id(model=City, arg_name=R.string.city_id_arg_name,
                                      include_zero=True, default=0)
        sort_method_id = get_valid_enum(arg_name=R.string.sort_method_arg_name, enum=R.id,
                                        default=R.id.SORT_METHOD_CLIENT_NAME, possible_values=Client.sort_method_map.ids)

        self.q = Client.query
        if state_id != 0:
            self.q = self.q.filter(Client.state_id == state_id)
        if city_id != 0:
            self.q = self.q.filter(Client.city_id == city_id)
        self.q = self.q.order_by(*Client.sort_method_map.order(sort_method_id))

        n_orders = self.q.count()

        self.per_page = current_app.config["CLIENTS_TABLE_PER_PAGE"]
        self.curr_page = get_valid_page(page_arg_name=R.string.page_arg_name, per_page=self.per_page,
                                        n_items=n_orders)

        filter_form = AdminClientFilterForm()
        filter_form.set_values(state_id=state_id, city_id=city_id)

        self.clients_in_page = self.q.slice(
                *get_page_range(curr_page=self.curr_page, per_page=self.per_page, min_page=R.dimen.min_page)).all()

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
            sort_methods=get_sort_methods_data(
                selected_sort_method_id=sort_method_id,
                sort_method_map=Client.sort_method_map
            ),
            table_data=self.get_table_data(),
            clients_in_page=self.clients_in_page
        )


    def get_table_data(self):
        rows = []
        for idx, client in enumerate(self.clients_in_page):
            rows.append([
                client.state.name if client.state else R.string.empty_symbol,
                client.city.name if client.city else R.string.empty_symbol,
                client.email,
                client.first_name if client.first_name else R.string.empty_symbol,
                client.get_formatted_register_datetime(),
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
                ]
            ])

        return dict(
            id="clients-table",
            cols=[
                dict(
                    id="state",
                    title=R.string.state,
                    type=R.id.COL_TYPE_TEXT
                ),
                dict(
                    id="city",
                    title=R.string.city,
                    type=R.id.COL_TYPE_TEXT
                ),
                dict(
                    id="email",
                    title=R.string.email,
                    type=R.id.COL_TYPE_TEXT
                ),
                dict(
                    id="name",
                    title=R.string.name,
                    type=R.id.COL_TYPE_TEXT,
                ),
                dict(
                    id="register-datetime",
                    title=R.string.register_date,
                    type=R.id.COL_TYPE_TEXT,
                ),
                dict(
                    id="action",
                    type=R.id.COL_TYPE_ACTION
                )
            ],
            rows=rows
        )


admin_clients_data_provider = AdminClientsDataProvider()
