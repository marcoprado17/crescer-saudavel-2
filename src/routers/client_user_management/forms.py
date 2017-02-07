# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 06/02/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask.ext.wtf import FlaskForm
from wtforms import StringField, PasswordField

from flask_bombril.form_validators import Unique
from flask_bombril.form_validators import EmailFormat
from flask_bombril.form_validators import EqualTo
from flask_bombril.form_validators import Length
from flask_bombril.form_validators import Required
from models.client import Client
from r import R


class RegisterForm(FlaskForm):
    email = StringField(
        label=R.string.email,
        validators=[
            Required(),
            Length(max_length=R.dimen.email_max_length),
            EmailFormat(),
            Unique(model=Client, field=Client.email, message=R.string.email_already_in_use)
        ]
    )
    password = PasswordField(
        label=R.string.password,
        validators=[
            Required(),
            Length(min_length=R.dimen.password_min_length, max_length=R.dimen.password_max_length, message=R.string.get_password_length_message()),
            EqualTo('password_confirmation', message=R.string.password_mismatch_message)
        ]
    )
    password_confirmation = PasswordField(
        label='Confirmação de senha',
        validators=[
            Required()
        ]
    )


class LoginForm(FlaskForm):
    email = StringField(
        label=R.string.email,
        validators=[
            Required(),
            Length(max_length=R.dimen.email_max_length),
            EmailFormat(),
        ]
    )
    password = PasswordField(
        label=R.string.password,
        validators=[
            Required(),
            Length(min_length=R.dimen.password_min_length, max_length=R.dimen.password_max_length, message=R.string.get_password_length_message()),
        ]
    )

    def __init__(self, email=None, **kwargs):
        super(LoginForm, self).__init__(**kwargs)
        if email is not None:
            self.email.data = email
