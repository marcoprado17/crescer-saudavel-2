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
from length import Length
from flask_bombril.r import R
from flask_bombril.form_validators.utils import AlwaysError
from app_contexts.unit_test_app import unit_test_app as app


class MockFormMin1MaxNone(FlaskForm):
    field = Field(validators=[Length(min_length=1)])


class MockFormMin3MaxNone(FlaskForm):
    field = Field(validators=[Length(min_length=3)])


class MockFormMinNoneMax1(FlaskForm):
    field = Field(validators=[Length(max_length=1)])


class MockFormMinNoneMax6(FlaskForm):
    field = Field(validators=[Length(max_length=6)])


class MockFormMin3Max6(FlaskForm):
    field = Field(validators=[Length(min_length=3, max_length=6)])


class MockFormMin3Max6CustomMessage(FlaskForm):
    field = Field(validators=[Length(min_length=3, max_length=6, message=R.string.test_message)])


class MockFormMin3Max6CustomCallableMessage(FlaskForm):
    field = Field(validators=[Length(min_length=3, max_length=6, message=lambda: R.string.test_message)])


class MockFormMin3Max6StopTrue(FlaskForm):
    field = Field(validators=[Length(min_length=3, max_length=6, stop=True), AlwaysError()])


class MockFormMin3Max6StopFalse(FlaskForm):
    field = Field(validators=[Length(min_length=3, max_length=6, stop=False), AlwaysError()])


class TestCase(BaseTestCase):
    def test_length_validator_creation(self):
        with self.assertRaises(AssertionError):
            Length()
        with self.assertRaises(AssertionError):
            Length(min_length=-2)
        with self.assertRaises(AssertionError):
            Length(max_length=-2)
        with self.assertRaises(AssertionError):
            Length(min_length=-2, max_length=-2)
        with self.assertRaises(AssertionError):
            Length(min_length=6, max_length=3)

    def test_valid_lengths_min_defined_max_none(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="aaa"
            ))
            form = MockFormMin3MaxNone()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
                field="aaaa"
            ))
            form = MockFormMin3MaxNone()
            self.assertTrue(form.validate_on_submit())

    def test_invalid_by_min_length_with_default_message(self):
        with app.test_client() as c:
            c.post("/", data=dict(
            ))
            form = MockFormMin1MaxNone()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(form.field.errors[0], R.string.validators.field_min_length_singular % dict(min_length=1))

            c.post("/", data=dict(
                field=""
            ))
            form = MockFormMin1MaxNone()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(form.field.errors[0], R.string.validators.field_min_length_singular % dict(min_length=1))

            c.post("/", data=dict(
                field="aa"
            ))
            form = MockFormMin3MaxNone()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(form.field.errors[0], R.string.validators.field_min_length_plural % dict(min_length=3))

    def test_valid_length_min_none_max_defined(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="aaa"
            ))
            form = MockFormMinNoneMax6()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
                field="aaaaaa"
            ))
            form = MockFormMinNoneMax6()
            self.assertTrue(form.validate_on_submit())

    def test_invalid_by_max_length_with_default_message(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="aa"
            ))
            form = MockFormMinNoneMax1()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(form.field.errors[0], R.string.validators.field_max_length_singular % dict(max_length=1))

            c.post("/", data=dict(
                field="aaaaaaa"
            ))
            form = MockFormMinNoneMax6()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(form.field.errors[0], R.string.validators.field_max_length_plural % dict(max_length=6))

    def test_valid_lengths_min_defined_max_defined(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="aaa"
            ))
            form = MockFormMin3Max6()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
                field="aaaaa"
            ))
            form = MockFormMin3Max6()
            self.assertTrue(form.validate_on_submit())

            c.post("/", data=dict(
                field="aaaaaaa"
            ))
            form = MockFormMin3Max6()
            self.assertFalse(form.validate_on_submit())

    def test_invalid_length_min_defined_max_defined_with_default_message(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="aa"
            ))
            form = MockFormMin3Max6()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(form.field.errors[0], R.string.validators.field_length_range %
                             dict(min_length=3, max_length=6))

    def test_invalid_length_min_defined_max_defined_with_custom_message(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="aaaaaaa"
            ))
            form = MockFormMin3Max6CustomMessage()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(form.field.errors[0], R.string.test_message)

    def test_invalid_length_min_defined_max_defined_with_custom_callable_message(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="aaaaaaa"
            ))
            form = MockFormMin3Max6CustomCallableMessage()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)
            self.assertEqual(form.field.errors[0], R.string.test_message)

    def test_stop_true(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="aaaaaaa"
            ))
            form = MockFormMin3Max6StopTrue()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 1)

    def test_stop_false(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="aaaaaaa"
            ))
            form = MockFormMin3Max6StopFalse()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.field.errors), 2)
