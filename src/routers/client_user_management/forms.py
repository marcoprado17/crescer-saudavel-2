# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 06/02/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask.ext.wtf import FlaskForm
from wtforms import StringField, PasswordField

from flask_bombril.form_validators.unique.unique import Unique
from flask_bombril.form_validators.email_format.email_format import EmailFormat
from flask_bombril.form_validators.equal_to.equal_to import EqualTo
from flask_bombril.form_validators.length.length import Length
from flask_bombril.form_validators.required.required import Required
from models.user import User
from r import R


class RegisterForm(FlaskForm):
    email = StringField(
        label=R.string.email,
        validators=[
            Required(),
            Length(max_length=R.dimen.email_max_length),
            EmailFormat(),
            Unique(model=User, field=User.email, message=R.string.email_already_in_use)
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

    def __init__(self, email=None, **kwargs):
        super(RegisterForm, self).__init__(**kwargs)
        if email is not None:
            self.email.data = email


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


class WantRedefinePasswordForm(FlaskForm):
    email = StringField(
        label=R.string.email,
        validators=[
            Required(),
            Length(max_length=R.dimen.email_max_length),
            EmailFormat(),
        ]
    )


class ResendConfirmationEmailForm(FlaskForm):
    email = StringField(
        label=R.string.email,
        validators=[
            Required(),
            Length(max_length=R.dimen.email_max_length),
            EmailFormat(),
        ]
    )


class RedefinePasswordForm(FlaskForm):
    email = StringField(
        label=R.string.email,
        validators=[
            Required(),
            Length(max_length=R.dimen.email_max_length),
            EmailFormat(),
        ]
    )
    password = PasswordField(
        label=R.string.new_password,
        validators=[
            Required(),
            Length(min_length=R.dimen.password_min_length, max_length=R.dimen.password_max_length,
                   message=R.string.get_password_length_message()),
            EqualTo('password_confirmation', message=R.string.password_mismatch_message)
        ]
    )
    password_confirmation = PasswordField(
        label=R.string.new_password_confirmation,
        validators=[
            Required()
        ]
    )

    def __init__(self, email, **kwargs):
        super(RedefinePasswordForm, self).__init__(**kwargs)
        self.email.data = email
