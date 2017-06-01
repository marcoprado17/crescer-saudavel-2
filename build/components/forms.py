# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 28/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

from flask.ext.bombril.form_validators.email_format.email_format import EmailFormat
from flask.ext.bombril.form_validators.length.length import Length
from flask.ext.bombril.form_validators.required.required import Required
from r import R


class NewsletterEmailForm(FlaskForm):
    email = StringField(
        label=R.string.email,
        validators=[
            Required(),
            Length(max_length=R.dimen.email_max_length),
            EmailFormat(),
        ]
    )
    submit = SubmitField(label=R.string.sign)

    def __init__(self, email=None, **kwargs):
        super(NewsletterEmailForm, self).__init__(**kwargs)
