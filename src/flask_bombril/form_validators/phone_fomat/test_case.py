# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 14/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from unittest import TestCase as BaseTestCase
from wtforms import Field
from wtforms.fields.html5 import TelField

from flask_bombril.form_validators.phone_fomat.phone_format import PhoneFormat
from flask_bombril.r import R
from flask_bombril.form_validators.utils import AlwaysError
from flask_wtf import FlaskForm
from app_contexts.unit_test_app import unit_test_app as app


class MockForm(FlaskForm):
    tel = TelField(validators=[PhoneFormat()])


class MockFormStopTrue(FlaskForm):
    tel = TelField(validators=[PhoneFormat(stop=True), AlwaysError()])


class MockFormStopFalse(FlaskForm):
    tel = TelField(validators=[PhoneFormat(stop=False), AlwaysError()])


class TestCase(BaseTestCase):
    def test_valid_phones(self):
        with app.test_client() as c:
            valid_phones = [
                "(11) 98140-5682",
                "(00) 08200-1632",
                "(10) 12345-6789",
                "(65) 4573-2456",
                "(23) 4342-3462"
            ]

            def assert_valid_email(valid_phone):
                c.post("/", data=dict(
                    tel=valid_phone
                ))
                form = MockForm()
                self.assertTrue(form.validate_on_submit())

            for phone in valid_phones:
                assert_valid_email(phone)

    def test_invalid_phones(self):
        with app.test_client() as c:
            invalid_phones = [
                "marco@@",
                "@gmail.com",
                "@gmail.com.br",
                "@@@@",
                "....@...",
                "marco",
                "m.m",
                "marco.padasv21@b",
                "marco.psd231sv@b asd sd",
                "a@bbb",
                "sadsadsadwds",
                "(11)  2938-2343",
                "(12 2345-2314",
                "(11) 123456-2346",
                "(11) 12342-23234",
                "(11) 1234-23234"
            ]

            def assert_invalid_phone(invalid_phone):
                c.post("/", data=dict(
                    tel=invalid_phone
                ))
                form = MockForm()
                self.assertFalse(form.validate_on_submit())
                self.assertEqual(len(form.tel.errors), 1)
                self.assertEqual(form.tel.errors[0], R.string.invalid_phone_format)

            for phone in invalid_phones:
                assert_invalid_phone(phone)

    def test_stop_true(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                tel="marco@@"
            ))
            mock_form = MockFormStopTrue()
            self.assertFalse(mock_form.validate_on_submit())
            self.assertEqual(len(mock_form.tel.errors), 1)

    def test_stop_false(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                tel="marco@@"
            ))
            mock_form = MockFormStopFalse()
            self.assertFalse(mock_form.validate_on_submit())
            self.assertEqual(len(mock_form.tel.errors), 2)
