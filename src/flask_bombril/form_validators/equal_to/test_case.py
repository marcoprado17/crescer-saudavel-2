# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from unittest import TestCase as BaseTestCase
from flask_wtf import FlaskForm
from wtforms import StringField
from flask_bombril.exceptions import InvalidFieldError
from equal_to import EqualTo
from flask_bombril.r import R
from flask_bombril.form_validators.utils import AlwaysError
from app_contexts.unit_test_app import unit_test_app as app


class MockForm(FlaskForm):
    field_1 = StringField(validators=[EqualTo("field_2")])
    field_2 = StringField()


class MockFormCustomMessage(FlaskForm):
    field_1 = StringField(validators=[EqualTo("field_2", message=R.string.test_message)])
    field_2 = StringField()


class MockFormCustomCallableMessage(FlaskForm):
    field_1 = StringField(validators=[EqualTo("field_2", message=lambda: R.string.test_message)])
    field_2 = StringField()


class MockFormKeyError(FlaskForm):
    field_1 = StringField(validators=[EqualTo("field_3")])
    field_2 = StringField()


class MockFormStopTrue(FlaskForm):
    field_1 = StringField(validators=[EqualTo("field_2", stop=True), AlwaysError()])
    field_2 = StringField()


class MockFormStopFalse(FlaskForm):
    field_1 = StringField(validators=[EqualTo("field_2", stop=False), AlwaysError()])
    field_2 = StringField()


class TestCase(BaseTestCase):
    def test_valid_input(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field_1="aaa",
                field_2="aaa"
            ))
            form = MockForm()
            self.assertTrue(form.validate_on_submit())

    def test_invalid_input_default_singular_error_message(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field_1="aaa",
                field_2="aa"
            ))
            form = MockForm()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field_1.errors), 1)
            self.assertEqual(form.field_1.errors[0], R.string.validators.field_must_be_equal_to %
                             dict(other_name="field_2"))

    def test_invalid_input_other_field_missing(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field_1="aaa"
            ))
            form = MockForm()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field_1.errors), 1)
            self.assertEqual(form.field_1.errors[0], R.string.validators.field_must_be_equal_to %
                             dict(other_name="field_2"))

    def test_invalid_input_custom_message(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field_1="aaa",
                field_2="aa"
            ))
            form = MockFormCustomMessage()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field_1.errors), 1)
            self.assertEqual(form.field_1.errors[0], R.string.test_message)

    def test_invalid_input_custom_callable_message(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field_1="aaa",
                field_2="aa"
            ))
            form = MockFormCustomCallableMessage()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field_1.errors), 1)
            self.assertEqual(form.field_1.errors[0], R.string.test_message)

    def test_invalid_field_name_declaration(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field_1="aaa",
                field_2="aa"
            ))
            form = MockFormKeyError()
            with self.assertRaises(InvalidFieldError):
                form.validate_on_submit()

    def test_stop_true(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field_1="aaa",
                field_2="aa"
            ))
            form = MockFormStopTrue()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field_1.errors), 1)

    def test_stop_false(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field_1="aaa",
                field_2="aa"
            ))
            form = MockFormStopFalse()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field_1.errors), 2)
