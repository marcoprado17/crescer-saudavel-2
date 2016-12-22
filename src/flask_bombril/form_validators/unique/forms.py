# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from flask_wtf import FlaskForm
from wtforms import StringField
from unique import Unique
from flask_bombril.r import R
from flask_bombril.form_validators.utils import AlwaysError, TestUser


class MockForm(FlaskForm):
    email = StringField(validators=[
        Unique(
            model=TestUser,
            field=TestUser.email
        )
    ])


class MockFormCustomMessage(FlaskForm):
    email = StringField(validators=[
        Unique(
            model=TestUser,
            field=TestUser.email,
            message=R.string.validators.email_already_registered
        )
    ])


class MockFormCustomCallableMessage(FlaskForm):
    email = StringField(validators=[
        Unique(
            model=TestUser,
            field=TestUser.email,
            message=lambda: R.string.validators.email_already_registered
        )
    ])


class MockFormStopTrue(FlaskForm):
    email = StringField(validators=[
        Unique(
            model=TestUser,
            field=TestUser.email,
            stop=True
        ),
        AlwaysError()
    ])


class MockFormStopFalse(FlaskForm):
    email = StringField(validators=[
        Unique(
            model=TestUser,
            field=TestUser.email,
            stop=False
        ),
        AlwaysError()
    ])
