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
from models.city import City
from r import R
from routers.admin_attended_cities import admin_attended_cities_blueprint
from routers.admin_attended_cities.data_providers.add_city import admin_add_city_data_provider
from routers.admin_attended_cities.data_providers.edit_city import admin_edit_city_data_provider
from routers.admin_attended_cities.data_providers.index import admin_cities_data_provider
from routers.admin_attended_cities.forms import AddCityForm, EditCityForm
from flask_bombril.r import R as bombril_R
from wrappers.base.decorators import valid_form
from wrappers.base.forms import SubmitForm


@admin_attended_cities_blueprint.route("/")
def index():
    return render_template("admin_attended_cities/index.html", data=admin_cities_data_provider.get_data())


@admin_attended_cities_blueprint.route("/adiciona-cidade", methods=["GET", "POST"])
def add_city():
    if request.method == "GET":
        return render_template("admin_attended_cities/add_city.html", data=admin_add_city_data_provider.get_data())

    else:
        add_city_form = AddCityForm()

        if add_city_form.validate_on_submit():
            city = City.create_from_form(add_city_form=add_city_form)
            flash(R.string.city_sent_successfully(city),
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.success))
            return redirect(url_for("admin_attended_cities.add_city"))

        return render_template("admin_attended_cities/add_city.html",
                               data=admin_add_city_data_provider.get_data(
                                   add_city_form=add_city_form))


@admin_attended_cities_blueprint.route("/editar-cidade/<int:city_id>", methods=["GET", "POST"])
def edit_city(city_id):
    city = City.get(city_id=city_id)
    if not city:
        return "", 404

    if request.method == "GET":
        return render_template("admin_attended_cities/edit_city.html",
                               data=admin_edit_city_data_provider.get_data_when_get(
                                   city=city))
    else:
        edit_city_form = EditCityForm()

        if edit_city_form.validate_on_submit():
            City.update_from_form(city=city, edit_city_form=edit_city_form)
            flash(R.string.city_successful_edited(city),
                  bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.success))
            return redirect(url_for("admin_attended_cities.index"))
        else:
            return render_template("admin_attended_cities/edit_city.html",
                                   data=admin_edit_city_data_provider.get_data_when_post(
                                       edit_city_form=edit_city_form))


@admin_attended_cities_blueprint.route("/ativar-cidade/<int:city_id>", methods=["GET", "POST"])
@valid_form(FormClass=SubmitForm)
def to_activate_city(city_id):
    City.update(city_id, active=True)
    return "", 200


@admin_attended_cities_blueprint.route("/desativar-cidade/<int:city_id>", methods=["GET", "POST"])
@valid_form(FormClass=SubmitForm)
def disable_city(city_id):
    City.update(city_id, active=False)
    return "", 200
