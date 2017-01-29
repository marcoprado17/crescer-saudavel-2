# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 05/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from unittest import TestCase as BaseTestCase
from flask_wtf import FlaskForm
from wtforms import Field
from flask_bombril.form_validators.price.price import Price
from flask_bombril.form_validators.utils import AlwaysError
from app_contexts.unit_test_app import unit_test_app as app
from flask_bombril.r import R


class MockForm(FlaskForm):
    field = Field(validators=[Price()])


class MockFormCustomMessage(FlaskForm):
    field = Field(validators=[Price(message=R.string.test_message)])


class MockFormCustomCallableMessage(FlaskForm):
    field = Field(validators=[Price(message=lambda:R.string.test_message)])


class MockFormStopTrue(FlaskForm):
    field = Field(validators=[Price(stop=True), AlwaysError()])


class MockFormStopFalse(FlaskForm):
    field = Field(validators=[Price(stop=False), AlwaysError()])


class TestCase(BaseTestCase):
    def test_valid_inputs(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="8,90"
            ))
            form = MockForm()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
                field="0,00"
            ))
            form = MockForm()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
                field="0,10"
            ))
            form = MockForm()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
                field="18,30"
            ))
            form = MockForm()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
                field="98,90"
            ))
            form = MockForm()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
                field="108.00"
            ))
            form = MockForm()
            self.assertTrue(form.validate_on_submit())

    def test_invalid_inputs(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="8,,90"
            ))
            form = MockForm()
            self.assertFalse(form.validate_on_submit())

            c.post("/", data=dict(
                field="8,900"
            ))
            form = MockForm()
            self.assertFalse(form.validate_on_submit())

            c.post("/", data=dict(
                field="sasdasda"
            ))
            form = MockForm()
            self.assertFalse(form.validate_on_submit())

            c.post("/", data=dict(
                field="8a,90"
            ))
            form = MockForm()
            self.assertFalse(form.validate_on_submit())

            c.post("/", data=dict(
                field="8..90"
            ))
            form = MockForm()
            self.assertFalse(form.validate_on_submit())

            c.post("/", data=dict(
                field="8,,90"
            ))
            form = MockForm()
            self.assertFalse(form.validate_on_submit())

    def test_default_message(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="8a,90"
            ))
            form = MockForm()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(R.string.invalid_price_format, form.field.errors[0])

    def test_custom_message(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="8a,90"
            ))
            form = MockFormCustomMessage()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(R.string.test_message, form.field.errors[0])

    def test_custom_callable_message(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="8a,90"
            ))
            form = MockFormCustomCallableMessage()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(R.string.test_message, form.field.errors[0])

    def test_stop_true(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="8a,90"
            ))
            form = MockFormStopTrue()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)

    def test_stop_false(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="8a,90"
            ))
            form = MockFormStopFalse()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 2)
