# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 24/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from proj_decorators import valid_form, safe_id_to_model_elem
from flask_bombril.r import R as bombril_R
from proj_forms import SubmitForm
from models.city import City
from r import R
from routers.admin_attended_cities import admin_attended_cities_blueprint
from routers.admin_attended_cities.data_providers.add_city import admin_add_city_data_provider
from routers.admin_attended_cities.data_providers.edit_city import admin_edit_city_data_provider
from routers.admin_attended_cities.data_providers.cities import admin_cities_data_provider
from routers.admin_attended_cities.forms import AddCityForm, EditCityForm


@admin_attended_cities_blueprint.route("/")
def cities():
    return render_template("admin_attended_cities/cities.html", data=admin_cities_data_provider.get_data())


@admin_attended_cities_blueprint.route("/adiciona-cidade", methods=["GET", "POST"])
def add_city():
    if request.method == "GET":
        return render_template("admin_attended_cities/add_city.html", data=admin_add_city_data_provider.get_data_when_get())
    else:
        add_city_form = AddCityForm()
        if add_city_form.validate_on_submit():
            city = City.create_from_form(form=add_city_form)
            flash(R.string.city_sent_successfully(city),
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.success))
            return redirect(url_for("admin_attended_cities.add_city"))
        else:
            return render_template("admin_attended_cities/add_city.html",
                               data=admin_add_city_data_provider.get_data_when_post(
                                   add_city_form=add_city_form))


# noinspection PyUnresolvedReferences
@admin_attended_cities_blueprint.route("/editar-cidade/<int:city_id>", methods=["GET", "POST"])
@safe_id_to_model_elem(model=City)
def edit_city(city):
    if request.method == "GET":
        return render_template("admin_attended_cities/edit_city.html",
                               data=admin_edit_city_data_provider.get_data_when_get(
                                   city=city))
    else:
        edit_city_form = EditCityForm()
        if edit_city_form.validate_on_submit():
            city.update_from_form(form=edit_city_form)
            flash(R.string.city_successful_edited(city),
                  bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.success))
            return redirect(url_for("admin_attended_cities.cities"))
        else:
            return render_template("admin_attended_cities/edit_city.html",
                                   data=admin_edit_city_data_provider.get_data_when_post(
                                       edit_city_form=edit_city_form))


# noinspection PyUnresolvedReferences
@admin_attended_cities_blueprint.route("/ativar-cidade/<int:city_id>", methods=["GET", "POST"])
@valid_form(FormClass=SubmitForm)
@safe_id_to_model_elem(model=City)
def to_activate_city(city, form):
    city.to_activate()
    return "", 200


# noinspection PyUnresolvedReferences
@admin_attended_cities_blueprint.route("/desativar-cidade/<int:city_id>", methods=["GET", "POST"])
@valid_form(FormClass=SubmitForm)
@safe_id_to_model_elem(model=City)
def disable_city(city, form):
    city.disable()
    return "", 200
