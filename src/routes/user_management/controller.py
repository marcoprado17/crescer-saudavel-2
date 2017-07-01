# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import json

import httplib2
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
from models.user.user import User
from proj_decorators import login_or_anonymous, protect_against_csrf
from proj_extensions import db
from r import R
from routes.user_management import user_management_blueprint
from routes.user_management.data_providers.redefine_password import client_redefine_password_data_provider
from routes.user_management.data_providers.resend_confirmation_email import \
    client_resend_confirmation_email_data_provider
from routes.user_management.data_providers.want_redefine_password import \
    client_want_redefine_password_data_provider
from routes.user_management.forms import RegisterForm, LoginForm, WantRedefinePasswordForm, RedefinePasswordForm, \
    ResendConfirmationEmailForm
from flask_bombril.r import R as bombril_R


@user_management_blueprint.route("/entrar", methods=["GET", "POST"])
@login_or_anonymous
def login(base_user):
    if request.method == "GET":
        email = get_url_arg(R.string.email_arg_name)
        return render_template("user_management/login.html", login_form=LoginForm(email))
    else:
        login_form = LoginForm()

        if not login_form.validate_on_submit():
            return render_template("user_management/login.html", login_form=login_form)

        user = User.get_by_email(login_form.email.data)

        if (user is not None) and user.facebook_login:
            flash(R.string.user_registered_with_facebook(user.email), "static-error")
            return render_template("user_management/login.html", login_form=login_form)
        if (user is None) or (not user.is_correct_password(login_form.password.data)):
            flash(R.string.email_or_password_invalid(), "static-error")
            return render_template("user_management/login.html", login_form=login_form)
        if not user.email_confirmed:
            flash(R.string.email_not_confirmed(email=login_form.email.data), "static-info")
            return render_template("user_management/login.html", login_form=login_form)

        try:
            logout_user()
            user.login_danger_danger(base_user)
        except Exception as e:
            db.session.rollback()
            flash(R.string.login_error, "static-error")
            return render_template("user_management/login.html", login_form=login_form)

        next_url = get_url_arg("next")
        if next_url:
            return redirect(next_url)

        if user.email == current_app.config["ADMIN_MAIL"]:
            return redirect(url_for('admin.index'))
        else:
            flash(R.string.successful_login, "toast-success")
            return redirect(url_for('client_home.home'))


@user_management_blueprint.route("/cadastrar", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        email = get_url_arg(R.string.email_arg_name)
        return render_template("user_management/register.html", register_form=RegisterForm(email))
    else:
        register_form = RegisterForm()
        if register_form.validate_on_submit():
            try:
                email_manager.send_create_account_confirmation_email(receiver_email=register_form.email.data)
            except:
                flash(R.string.send_confirmation_email_error_message, "static-error")
                return render_template("user_management/register.html", register_form=register_form)
            try:
                User.create_from_form(form=register_form, other_attrs=dict(register_datetime=datetime.now()))
            except:
                flash(R.string.data_base_access_error_message, "static-error")
                return render_template("user_management/register.html", register_form=register_form)
            flash(R.string.account_successful_created(email=register_form.email.data), "static-success")
            return redirect(url_for("user_management.login", **{R.string.email_arg_name: register_form.email.data}))
        else:
            return render_template("user_management/register.html", register_form=register_form)


@user_management_blueprint.route("/email-confirmado/<string:token>")
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
    return redirect(url_for("user_management.login", **{R.string.email_arg_name: email}))


@user_management_blueprint.route("/quero-redefinir-minha-senha", methods=["GET", "POST"])
def want_redefine_password():
    if request.method == "GET":
        return render_template("user_management/want_redefine_password.html",
                               data=client_want_redefine_password_data_provider.get_data_when_get())
    else:
        want_redefine_password_form = WantRedefinePasswordForm()

        if not want_redefine_password_form.validate_on_submit():
            return render_template("user_management/want_redefine_password.html",
                                   data=client_want_redefine_password_data_provider.get_data_when_post(
                                       want_redefine_password_form=want_redefine_password_form))

        user = User.get_by_email(want_redefine_password_form.email.data)
        if user == None:
            flash(R.string.email_not_found(email=want_redefine_password_form.email.data),
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.error))
            return render_template("user_management/want_redefine_password.html",
                                   data=client_want_redefine_password_data_provider.get_data_when_post(
                                       want_redefine_password_form=want_redefine_password_form))

        if user.facebook_login:
            flash(R.string.users_registered_with_facebook_cant_redefine_password,
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.error))
            return render_template("user_management/want_redefine_password.html",
                                   data=client_want_redefine_password_data_provider.get_data_when_post(
                                       want_redefine_password_form=want_redefine_password_form))

        try:
            email_manager.send_redefine_password_email(receiver_email=want_redefine_password_form.email.data)
        except:
            flash(R.string.send_redefine_password_email_error_message,
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.error))
            return render_template("user_management/want_redefine_password.html",
                                   data=client_want_redefine_password_data_provider.get_data_when_post(
                                       want_redefine_password_form=want_redefine_password_form))

        flash(R.string.successful_send_redefine_password_email(email=want_redefine_password_form.email.data),
              bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.success))
        return redirect(url_for("user_management.login"))


@user_management_blueprint.route("/redefinir-senha/<string:token>", methods=["GET", "POST"])
def redefine_password(token):
    ts = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
    try:
        email = ts.loads(token, salt=current_app.config["EMAIL_TOKEN_SALT"], max_age=R.dimen.day_in_seconds)
    except:
        flash(R.string.invalid_redefine_password_requisition,
              bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.error))
        return redirect(url_for("user_management.want_redefine_password"))
    if request.method == "GET":
        return render_template("user_management/redefine_password.html",
                               data=client_redefine_password_data_provider.get_data_when_get(email=email))
    else:
        redefine_password_form = RedefinePasswordForm(email=email)

        if not redefine_password_form.validate_on_submit():
            return render_template("user_management/redefine_password.html",
                                   data=client_redefine_password_data_provider.get_data_when_post(
                                       redefine_password_form=redefine_password_form))

        user = User.get_by_email(email)
        if user == None:
            return "", 400

        if user.facebook_login:
            flash(R.string.users_registered_with_facebook_cant_redefine_password,
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.error))
            return render_template("user_management/redefine_password.html",
                                   data=client_redefine_password_data_provider.get_data_when_post(
                                       redefine_password_form=redefine_password_form))

        user.change_password(redefine_password_form.password.data)

        flash(R.string.password_successful_redefined,
              bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.success))
        return redirect(url_for("user_management.login", email=email))


@user_management_blueprint.route("/reenviar-email-de-confirmacao", methods=["GET", "POST"])
def resend_confirmation_email():
    if request.method == "GET":
        return render_template("user_management/resend_confirmation_email.html",
                               data=client_resend_confirmation_email_data_provider.get_data_when_get())
    else:
        resend_confirmation_email_form = ResendConfirmationEmailForm()

        if not resend_confirmation_email_form.validate_on_submit():
            return render_template("user_management/resend_confirmation_email.html",
                                   data=client_resend_confirmation_email_data_provider.get_data_when_post(resend_confirmation_email_form=resend_confirmation_email_form))

        user = User.get_by_email(resend_confirmation_email_form.email.data)
        if user is None:
            flash(R.string.account_never_created(email=resend_confirmation_email_form.email.data),
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.error))
            return render_template("user_management/resend_confirmation_email.html",
                                   data=client_resend_confirmation_email_data_provider.get_data_when_post(
                                       resend_confirmation_email_form=resend_confirmation_email_form))

        if user.facebook_login:
            flash(R.string.users_registered_with_facebook_no_need_confirm_email,
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.error))
            return render_template("user_management/resend_confirmation_email.html",
                                   data=client_resend_confirmation_email_data_provider.get_data_when_post(
                                       resend_confirmation_email_form=resend_confirmation_email_form))

        try:
            email_manager.send_create_account_confirmation_email(receiver_email=user.email)
        except:
            flash(R.string.send_confirmation_email_error_message,
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.error))
            return render_template("user_management/resend_confirmation_email.html",
                                   data=client_resend_confirmation_email_data_provider.get_data_when_post(
                                       resend_confirmation_email_form=resend_confirmation_email_form))

        flash(R.string.successful_resend_of_confirmation_email(email=user.email),
              bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.success))
        return redirect(url_for("user_management.login", **{R.string.email_arg_name: user.email}))


@user_management_blueprint.route("/sair")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home.home"))


@user_management_blueprint.route("/entrar-com-facebook", methods=["POST"])
@protect_against_csrf
@login_or_anonymous
def facebook_login(base_user):
    access_token = request.data
    app_id = current_app.config["FACEBOOK_APP_ID"]
    app_secret = current_app.config["FACEBOOK_APP_SECRET"]

    url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (
        app_id, app_secret, access_token)
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]

    token = result.split("&")[0]
    url = 'https://graph.facebook.com/v2.4/me?%s&fields=name,id,email' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)

    email=data["email"]

    user = User.get_by_email(email)

    if user is None:
        user = User.create_user_with_facebook_login(email=email)
        # TODO: Send email
    else:
        if user.facebook_login == False:
            return json.dumps(dict(error=R.string.email_not_registered_with_facebook(email))), 400

    logout_user()
    user.login_danger_danger(base_user)

    flash(R.string.successful_facebook_login,
          bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.success))

    return "", 200
