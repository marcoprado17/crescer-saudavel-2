# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from wtforms.validators import StopValidation, ValidationError
from flask_bombril.r import R
from extensions import db


class TestUser(db.Model):
    email = db.Column(db.String(), primary_key=True, unique=True)


class AlwaysError(object):
    def __init__(self):
        pass

    def __call__(self, form, field):
        raise ValidationError(R.string.validators.always_error)


def raise_with_stop(validator, message=None):
    if validator.stop:
        if message:
            raise StopValidation(message)
        else:
            raise StopValidation(validator.message)
    else:
        if message:
            raise ValidationError(message)
        else:
            raise ValidationError(validator.message)
