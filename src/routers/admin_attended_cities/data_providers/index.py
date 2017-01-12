# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 11/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import current_app
from flask import url_for
from sqlalchemy import asc

from components.data_providers.paginator import paginator_data_provider
from flask_bombril.utils import get_page_range
from flask_bombril.utils import n_pages
from flask_bombril.url_args import get_valid_page
from flask_bombril.url_args import get_boolean_url_arg
from flask_bombril.url_args import get_valid_model_id
from models.city import City
from models.state import State
from r import R
from routers.admin_attended_cities.forms import CityFilterForm
from wrappers.base.forms import SubmitForm


class AdminCitiesDataProvider(object):
    def get_data(self):
        active = get_boolean_url_arg(arg_name=R.string.active_arg_name, default=True)
        state_id = get_valid_model_id(model=State, arg_name=R.string.state_id_arg_name, include_zero=True, default=0)

        self.q = City.query
        self.q = self.q.filter(City.active == active)
        if state_id != 0:
            self.q = self.q.filter(City.state_id == state_id)
        self.q = self.q.order_by(asc(City.name))

        n_cities = self.q.count()

        self.per_page = current_app.config["DEFAULT_PER_PAGE"]
        self.curr_page = get_valid_page(page_arg_name=R.string.page_arg_name, per_page=self.per_page,
                                        n_items=n_cities)

        filter_form = CityFilterForm()
        filter_form.set_values(state_id=state_id, active=active)

        return dict(
            n_items=n_cities,
            paginator_data=paginator_data_provider.get_data(
                min_page=R.dimen.min_page,
                curr_page=self.curr_page,
                max_page=n_pages(per_page=self.per_page, n_items=n_cities)
            ),
            filter_data=dict(
                filter_form=filter_form
            ),
            table_data=self.get_table_data()
        )

    def get_table_data(self):
        rows = []
        for idx, city in enumerate(self.q.slice(
                *get_page_range(curr_page=self.curr_page, per_page=self.per_page, min_page=R.dimen.min_page)).all()):
            rows.append([
                city.active,
                city.state.name,
                city.name,
                [
                    dict(
                        type=R.id.ACTION_TYPE_LINK_BUTTON,
                        text=R.string.edit,
                        classes="edit",
                        href=url_for("admin_attended_cities.edit_city", city_id=city.id)
                    ),
                    dict(
                        type=R.id.ACTION_TYPE_ACTIVATE_DISABLE_BUTTON,
                        active=city.active,
                        form=SubmitForm(),
                        meta_data={
                            "data-active-col-id": "active"
                        },
                        to_activate_url=url_for(
                            "admin_attended_cities.to_activate_city", city_id=city.id),
                        to_activate_meta_data={
                            "data-error-msg": R.string.to_activate_city_error(city.name),
                        },
                        disable_url=url_for(
                            "admin_attended_cities.disable_city", city_id=city.id),
                        disable_meta_data={
                            "data-error-msg": R.string.disable_city_error(city.name),
                        }
                    )
                ]
            ])

        return dict(
            id="cities-table",
            cols=[
                dict(
                    id="active",
                    title=R.string.active_in_female,
                    type=R.id.COL_TYPE_BOOL
                ),
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
                    id="action",
                    type=R.id.COL_TYPE_ACTION,
                    expandable=False
                )
            ],
            rows=rows
        )


admin_cities_data_provider = AdminCitiesDataProvider()
