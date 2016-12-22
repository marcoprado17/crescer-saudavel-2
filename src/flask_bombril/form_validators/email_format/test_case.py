# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from unittest import TestCase as BaseTestCase
from wtforms import Field
from flask_bombril.r import R
from flask_bombril.form_validators.utils import AlwaysError
from email_format import EmailFormat
from flask_wtf import FlaskForm
from app_contexts.unit_test_app import unit_test_app as app


class MockForm(FlaskForm):
    email = Field(validators=[EmailFormat()])


class MockFormStopTrue(FlaskForm):
    email = Field(validators=[EmailFormat(stop=True), AlwaysError()])


class MockFormStopFalse(FlaskForm):
    email = Field(validators=[EmailFormat(stop=False), AlwaysError()])


class TestCase(BaseTestCase):
    def test_valid_emails(self):
        with app.test_client() as c:
            valid_emails = [
                "marccsaaso.s89sv@gmail.com",
                "sada.vidsdsaoca@bol.com.br",
                "marcoprado8827@hotmail.com",
                "ab@b.com",
                "marco aurelio@gmail.com"
            ]

            def assert_valid_email(valid_email):
                c.post("/", data=dict(
                    email=valid_email
                ))
                form = MockForm()
                self.assertTrue(form.validate_on_submit())

            for email in valid_emails:
                assert_valid_email(email)

    def test_invalid_emails(self):
        with app.test_client() as c:
            invalid_emails = [
                "marco@@",
                "@gmail.com",
                "@gmail.com.br",
                "@@@@",
                "....@...",
                "marco",
                "m.m",
                "marco.padasv21@b",
                "marco.psd231sv@b asd sd",
                "a@bbb"
            ]

            def assert_invalid_email(invalid_email):
                c.post("/", data=dict(
                    email=invalid_email
                ))
                form = MockForm()
                self.assertFalse(form.validate_on_submit())
                self.assertEqual(len(form.email.errors), 1)
                self.assertEqual(form.email.errors[0], R.string.validators.invalid_email_format)

            for email in invalid_emails:
                assert_invalid_email(email)

    def test_stop_true(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                email="marco@@"
            ))
            email_mock_form = MockFormStopTrue()
            self.assertFalse(email_mock_form.validate_on_submit())
            self.assertEqual(len(email_mock_form.email.errors), 1)

    def test_stop_false(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                email="marco@@"
            ))
            email_mock_form = MockFormStopFalse()
            self.assertFalse(email_mock_form.validate_on_submit())
            self.assertEqual(len(email_mock_form.email.errors), 2)
