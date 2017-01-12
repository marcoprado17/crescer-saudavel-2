# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 12/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.admin_attended_cities.forms import EditCityForm


class EditCityDataProvider(object):
    def get_data_when_get(self, city):
        edit_city_form = EditCityForm()
        edit_city_form.set_values(city=city)
        return dict(
            edit_city_form=edit_city_form
        )

    def get_data_when_post(self, edit_city_form):
        return dict(
            edit_city_form=edit_city_form
        )


admin_edit_city_data_provider = EditCityDataProvider()