# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 09/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from functools import wraps

from flask import abort
from flask import current_app
from flask import flash
from flask import redirect
from flask import request
from flask import session
from flask import url_for
from flask_login import current_user

from flask_bombril.r import R as bombril_R
from flask_bombril.utils import camel_case_to_snake_case
from models.user.anonymous_user import AnonymousUser
from r import R


def valid_form(FormClass):
    def real_decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            form = FormClass()
            if form.validate_on_submit():
                kwargs["form"] = form
                return func(*args, **kwargs)
            elif "csrf_token" in form.errors:
                return "", 403
            else:
                return "", 400
        return decorated_function
    return real_decorator

def safe_id_to_model_elem(model):
    '''
    The name of the variable that represents the id of the model element is the name of the model + "Id" converted to snake_case
    The name of the variable that represents the model element is the name of the model converted to snake_case
    '''
    def real_decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            elem_id_name = camel_case_to_snake_case(model.__name__ + "Id")
            elem_name = camel_case_to_snake_case(model.__name__)
            id = kwargs[elem_id_name]
            model_elem = model.get(id)
            del kwargs[elem_id_name]
            kwargs[elem_name] = model_elem
            if model_elem == None:
                return "", 404
            else:
                return func(*args, **kwargs)
        return decorated_function
    return real_decorator

def admin_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if (not current_user) or (not current_user.is_authenticated) or (current_user.email != current_app.config['ADMIN_MAIL']):
            flash(R.string.admin_login_required, bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.info))
            return redirect(url_for("client_user_management.login", next=request.url))
        return func(*args, **kwargs)
    return decorated_function

def login_or_anonymous(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        user = current_user
        if user.is_anonymous and \
                (R.string.anonymous_user_id in session) and \
                (session[R.string.anonymous_user_id] is not None):
            user = AnonymousUser.get(session[R.string.anonymous_user_id])
            if user is None:
                user = current_user
        returned_value = func(user=user, *args, **kwargs)
        if user.is_anonymous:
            session[R.string.anonymous_user_id] = user.id
        return returned_value
    return decorated_function

def protect_against_csrf(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        token = session.get(R.string.csrf_token_session_arg_name, None)
        if not token or (token != request.args.get(R.string.csrf_token_arg_name) and token != request.form.get(R.string.csrf_token_arg_name)):
            abort(403)
        return func(*args, **kwargs)
    return decorated_function
