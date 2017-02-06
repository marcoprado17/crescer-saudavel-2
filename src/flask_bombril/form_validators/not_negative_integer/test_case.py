# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 05/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from unittest import TestCase as BaseTestCase
from flask_wtf import FlaskForm
from wtforms import Field

from not_negative_integer import NotNegativeInteger
from flask_bombril.utils import AlwaysError
from app_contexts.unit_test_app import unit_test_app as app
from flask_bombril.r import R


class MockForm(FlaskForm):
    field = Field(validators=[NotNegativeInteger()])


class MockFormCustomMessage(FlaskForm):
    field = Field(validators=[NotNegativeInteger(message=R.string.test_message)])


class MockFormCustomCallableMessage(FlaskForm):
    field = Field(validators=[NotNegativeInteger(message=lambda:R.string.test_message)])


class MockFormStopTrue(FlaskForm):
    field = Field(validators=[NotNegativeInteger(stop=True), AlwaysError()])


class MockFormStopFalse(FlaskForm):
    field = Field(validators=[NotNegativeInteger(stop=False), AlwaysError()])


class TestCase(BaseTestCase):
    def test_valid_inputs(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="0"
            ))
            form = MockForm()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
                field="12"
            ))
            form = MockForm()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
                field="123"
            ))
            form = MockForm()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
                field="1"
            ))
            form = MockForm()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
                field="2123231"
            ))
            form = MockForm()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
                field="42"
            ))
            form = MockForm()
            self.assertTrue(form.validate_on_submit())

    def test_invalid_inputs(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="asd"
            ))
            form = MockForm()
            self.assertFalse(form.validate_on_submit())

            c.post("/", data=dict(
                field="-1"
            ))
            form = MockForm()
            self.assertFalse(form.validate_on_submit())

            c.post("/", data=dict(
                field="-23"
            ))
            form = MockForm()
            self.assertFalse(form.validate_on_submit())

            c.post("/", data=dict(
                field="2,3"
            ))
            form = MockForm()
            self.assertFalse(form.validate_on_submit())

            c.post("/", data=dict(
                field="2.2"
            ))
            form = MockForm()
            self.assertFalse(form.validate_on_submit())

            c.post("/", data=dict(
                field="*2"
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
            self.assertEqual(R.string.invalid_not_negative_integer, form.field.errors[0])

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
