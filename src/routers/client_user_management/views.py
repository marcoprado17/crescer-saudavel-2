# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from datetime import datetime
from flask import current_app
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_login import logout_user
from flask_login import login_required
from itsdangerous import URLSafeTimedSerializer
from email_blueprint import email_manager
from flask_bombril.utils import get_url_arg
from models.user import User
from r import R
from routers.client_user_management import client_user_management_blueprint
from routers.client_user_management.data_providers.login import client_login_data_provider
from routers.client_user_management.data_providers.redefine_password import client_redefine_password_data_provider
from routers.client_user_management.data_providers.register import client_register_data_provider
from routers.client_user_management.data_providers.resend_confirmation_email import \
    client_resend_confirmation_email_data_provider
from routers.client_user_management.data_providers.want_redefine_password import \
    client_want_redefine_password_data_provider
from routers.client_user_management.forms import RegisterForm, LoginForm, WantRedefinePasswordForm, RedefinePasswordForm, \
    ResendConfirmationEmailForm
from flask_bombril.r import R as bombril_R


@client_user_management_blueprint.route("/entrar", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        email = get_url_arg(R.string.email_arg_name)
        return render_template("client_user_management/login.html",
                               data=client_login_data_provider.get_data_when_get(email))
    else:
        login_form = LoginForm()

        if not login_form.validate_on_submit():
            return render_template("client_user_management/login.html",
                                   data=client_login_data_provider.get_data_when_post(login_form=login_form))

        user = User.get_by_email(login_form.email.data)
        if (user is None) or (not user.is_correct_password(login_form.password.data)):
            flash(R.string.email_or_password_invalid(),
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.error))
            return render_template("client_user_management/login.html",
                                   data=client_login_data_provider.get_data_when_post(login_form=login_form))
        if not user.email_confirmed:
            flash(R.string.email_not_confirmed(email=login_form.email.data),
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.info))
            return render_template("client_user_management/login.html",
                                   data=client_login_data_provider.get_data_when_post(login_form=login_form))

        try:
            user.login_danger_danger()
        except:
            flash(R.string.login_error,
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.error))
            return render_template("client_user_management/login.html",
                                   data=client_login_data_provider.get_data_when_post(login_form=login_form))

        next = get_url_arg("next")
        if next:
            return redirect(next)

        if user.email == current_app.config["ADMIN_MAIL"]:
            return redirect(url_for('admin_home.home'))
        else:
            return redirect(url_for('client_home.home'))


@client_user_management_blueprint.route("/cadastrar", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        email=get_url_arg(R.string.email_arg_name)
        return render_template("client_user_management/register.html",
                               data=client_register_data_provider.get_data_when_get(email))
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
                User.create_from_form(form=register_form, other_attrs=dict(register_datetime=datetime.now()))
            except:
                flash(R.string.data_base_access_error_message,
                      bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.error))
                return render_template("client_user_management/register.html",
                                       data=client_register_data_provider.get_data_when_post(
                                           register_form=register_form))
            flash(R.string.account_successful_created(email=register_form.email.data),
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.success))
            return redirect(
                url_for("client_user_management.login", **{R.string.email_arg_name: register_form.email.data}))
        else:
            return render_template("client_user_management/register.html",
                                   data=client_register_data_provider.get_data_when_post(register_form=register_form))


@client_user_management_blueprint.route("/email-confirmado/<string:token>")
def email_confirmed(token):
    ts = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
    try:
        email = ts.loads(token, salt=current_app.config["EMAIL_TOKEN_SALT"])
    except:
        return "", 400
    client = User.get_by_email(email)
    if client == None:
        return "", 404
    client.mark_email_as_confirmed()
    flash(R.string.email_successful_confirmed(email=email),
          bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.success))
    return redirect(url_for("client_user_management.login", **{R.string.email_arg_name: email}))


@client_user_management_blueprint.route("/quero-redefinir-minha-senha", methods=["GET", "POST"])
def want_redefine_password():
    if request.method == "GET":
        return render_template("client_user_management/want_redefine_password.html",
                               data=client_want_redefine_password_data_provider.get_data_when_get())
    else:
        want_redefine_password_form = WantRedefinePasswordForm()

        if not want_redefine_password_form.validate_on_submit():
            return render_template("client_user_management/want_redefine_password.html",
                                   data=client_want_redefine_password_data_provider.get_data_when_post(
                                       want_redefine_password_form=want_redefine_password_form))

        user = User.get_by_email(want_redefine_password_form.email.data)
        if user == None:
            flash(R.string.email_not_found(email=want_redefine_password_form.email.data),
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.error))
            return render_template("client_user_management/want_redefine_password.html",
                                   data=client_want_redefine_password_data_provider.get_data_when_post(
                                       want_redefine_password_form=want_redefine_password_form))

        try:
            email_manager.send_redefine_password_email(receiver_email=want_redefine_password_form.email.data)
        except:
            flash(R.string.send_redefine_password_email_error_message,
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.error))
            return render_template("client_user_management/want_redefine_password.html",
                                   data=client_want_redefine_password_data_provider.get_data_when_post(
                                       want_redefine_password_form=want_redefine_password_form))

        flash(R.string.successful_send_redefine_password_email(email=want_redefine_password_form.email.data),
              bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.success))
        return redirect(url_for("client_user_management.login"))


@client_user_management_blueprint.route("/redefinir-senha/<string:token>", methods=["GET", "POST"])
def redefine_password(token):
    ts = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
    try:
        email = ts.loads(token, salt=current_app.config["EMAIL_TOKEN_SALT"], max_age=R.dimen.day_in_seconds)
    except:
        flash(R.string.invalid_redefine_password_requisition,
              bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.error))
        return redirect(url_for("client_user_management.want_redefine_password"))
    if request.method == "GET":
        return render_template("client_user_management/redefine_password.html",
                               data=client_redefine_password_data_provider.get_data_when_get(email=email))
    else:
        redefine_password_form = RedefinePasswordForm(email=email)

        if not redefine_password_form.validate_on_submit():
            return render_template("client_user_management/redefine_password.html",
                                   data=client_redefine_password_data_provider.get_data_when_post(
                                       redefine_password_form=redefine_password_form))

        user = User.get_by_email(email)
        if user == None:
            return "", 400
        user.change_password(redefine_password_form.password.data)

        flash(R.string.password_successful_redefined,
              bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.success))
        return redirect(url_for("client_user_management.login", email=email))


@client_user_management_blueprint.route("/reenviar-email-de-confirmacao", methods=["GET", "POST"])
def resend_confirmation_email():
    if request.method == "GET":
        return render_template("client_user_management/resend_confirmation_email.html",
                               data=client_resend_confirmation_email_data_provider.get_data_when_get())
    else:
        resend_confirmation_email_form = ResendConfirmationEmailForm()

        if not resend_confirmation_email_form.validate_on_submit():
            return render_template("client_user_management/resend_confirmation_email.html",
                                   data=client_resend_confirmation_email_data_provider.get_data_when_post(resend_confirmation_email_form=resend_confirmation_email_form))

        user = User.get_by_email(resend_confirmation_email_form.email.data)
        if user is None:
            flash(R.string.account_never_created(email=resend_confirmation_email_form.email.data),
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.error))
            return render_template("client_user_management/resend_confirmation_email.html",
                                   data=client_resend_confirmation_email_data_provider.get_data_when_post(
                                       resend_confirmation_email_form=resend_confirmation_email_form))

        try:
            email_manager.send_create_account_confirmation_email(receiver_email=user.email)
        except:
            flash(R.string.send_confirmation_email_error_message,
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.error))
            return render_template("client_user_management/resend_confirmation_email.html",
                                   data=client_resend_confirmation_email_data_provider.get_data_when_post(
                                       resend_confirmation_email_form=resend_confirmation_email_form))

        flash(R.string.successful_resend_of_confirmation_email(email=user.email),
              bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.success))
        return redirect(url_for("client_user_management.login", **{R.string.email_arg_name: user.email}))


@client_user_management_blueprint.route("/sair")
@login_required
def logout():
    logout_user()
    return redirect(url_for("client_home.home"))
