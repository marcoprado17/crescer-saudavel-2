# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from datetime import datetime
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from email_blueprint import email_manager
from models.client import Client
from r import R
from routers.client_user_management import client_user_management_blueprint
from routers.client_user_management.data_providers.register import client_register_data_provider
from routers.client_user_management.forms import RegisterForm
from flask_bombril.r import R as bombril_R


@client_user_management_blueprint.route("/entrar")
def login():
    return "Entrar."


@client_user_management_blueprint.route("/cadastrar", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("client_user_management/register.html", data=client_register_data_provider.get_data_when_get())
    else:
        register_form = RegisterForm()
        if register_form.validate_on_submit():
            try:
                email_manager.send_create_account_confirmation_email(receiver_email=register_form.email.data)
            except:
                flash(R.string.send_confirmation_email_error_message,
                      bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.error))
                return render_template("client_user_management/register.html",
                                       data=client_register_data_provider.get_data_when_post(
                                           register_form=register_form))
            try:
                Client.create_from_form(form=register_form, other_attrs=dict(register_datetime=datetime.now()))
            except:
                flash(R.string.data_base_access_error_message,
                      bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.error))
                return render_template("client_user_management/register.html",
                                       data=client_register_data_provider.get_data_when_post(
                                           register_form=register_form))
            flash(R.string.account_successful_created(email=register_form.email.data),
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.success))
            return redirect(url_for("client_user_management.login"))
        else:
            return render_template("client_user_management/register.html",
                                   data=client_register_data_provider.get_data_when_post(register_form=register_form))


@client_user_management_blueprint.route("/email-confirmado/<string:token>")
def email_confirmed(token):
    return "Email confirmado, token: " + token
