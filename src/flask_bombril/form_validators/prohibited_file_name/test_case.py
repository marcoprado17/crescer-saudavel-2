# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 25/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from unittest import TestCase as BaseTestCase
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from flask_bombril.form_validators.prohibited_file_name import ProhibitedFileName
from flask_bombril.utils import AlwaysError
from app_contexts.unit_test_app import unit_test_app as app
from flask_bombril.r import R


class MockFormString(FlaskForm):
    field = StringField(validators=[ProhibitedFileName(prohibited_names=["a", "b", "c"])])


class MockFormInt(FlaskForm):
    field = IntegerField(validators=[ProhibitedFileName(prohibited_names=[1, 2, 3])])


class MockFormCustomMessage(FlaskForm):
    field = StringField(validators=[ProhibitedFileName(prohibited_names=["a", "b", "c"], message=R.string.test_message)])


class MockFormCustomCallableMessage(FlaskForm):
    field = StringField(validators=[ProhibitedFileName(prohibited_names=["a", "b", "c"], message=lambda x :R.string.func_test_message(x))])


class MockFormStopTrue(FlaskForm):
    field = StringField(validators=[ProhibitedFileName(prohibited_names=["a", "b", "c"], stop=True), AlwaysError()])


class MockFormStopFalse(FlaskForm):
    field = StringField(validators=[ProhibitedFileName(prohibited_names=["a", "b", "c"], stop=False), AlwaysError()])


class TestCase(BaseTestCase):
    def test_valid_inputs(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="0"
            ))
            form = MockFormString()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
                field="12"
            ))
            form = MockFormString()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
                field="123"
            ))
            form = MockFormString()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
                field="1"
            ))
            form = MockFormString()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
                field="2123231"
            ))
            form = MockFormString()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
                field="42"
            ))
            form = MockFormString()
            self.assertTrue(form.validate_on_submit())

    def test_invalid_inputs(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="a"
            ))
            form = MockFormString()
            self.assertFalse(form.validate_on_submit())

            c.post("/", data=dict(
                field="b"
            ))
            form = MockFormString()
            self.assertFalse(form.validate_on_submit())

            c.post("/", data=dict(
                field="c"
            ))
            form = MockFormString()
            self.assertFalse(form.validate_on_submit())

            c.post("/", data=dict(
                field=1
            ))
            form = MockFormInt()
            self.assertFalse(form.validate_on_submit())

            c.post("/", data=dict(
                field=2
            ))
            form = MockFormInt()
            self.assertFalse(form.validate_on_submit())

            c.post("/", data=dict(
                field=3
            ))
            form = MockFormInt()
            self.assertFalse(form.validate_on_submit())


    def test_default_message(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="a"
            ))
            form = MockFormString()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(R.string.prohibited_value, form.field.errors[0])

    def test_custom_message(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="a"
            ))
            form = MockFormCustomMessage()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(R.string.test_message, form.field.errors[0])

    def test_custom_callable_message(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="a"
            ))
            form = MockFormCustomCallableMessage()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(R.string.func_test_message("a"), form.field.errors[0])

    def test_stop_true(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="a"
            ))
            form = MockFormStopTrue()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)

    def test_stop_false(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="a"
            ))
            form = MockFormStopFalse()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 2)
