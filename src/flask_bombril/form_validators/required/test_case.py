# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from unittest import TestCase as BaseTestCase
from flask_wtf import FlaskForm
from wtforms import Field
from flask_bombril.r import R
from required import Required
from flask_bombril.form_validators.utils import AlwaysError
from app_contexts.unit_test_app import unit_test_app as app


class MockForm(FlaskForm):
    field = Field(validators=[Required()])


class MockFormWithAlwaysError(FlaskForm):
    field = Field(validators=[Required(), AlwaysError()])


class TestCase(BaseTestCase):
    def test_valid_input(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="a"
            ))
            form = MockForm()
            self.assertTrue(form.validate_on_submit())

    def test_invalid_inputs(self):
        with app.test_client() as c:
            c.post("/")
            form = MockForm()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(form.field.errors[0], R.string.validators.required_field)

            c.post("/", data=dict(
                field=None
            ))
            form = MockForm()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(form.field.errors[0], R.string.validators.required_field)

    def test_stop_true(self):
        with app.test_client() as c:
            c.post("/")
            form = MockFormWithAlwaysError()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
