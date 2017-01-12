# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 11/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.admin_attended_cities.forms import AddCityForm


class AdminAddCityDataProvider(object):
    def get_data(self, add_city_form=None):
        if add_city_form == None:
            add_city_form = AddCityForm()

        return dict(
            add_city_form=add_city_form
        )


admin_add_city_data_provider = AdminAddCityDataProvider()
