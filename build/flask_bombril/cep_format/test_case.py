# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 19/02/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from unittest import TestCase as BaseTestCase
from wtforms import Field, StringField
from wtforms.fields.html5 import TelField

from flask.ext.bombril.cep_format.cep_format import CepFormat
from flask_bombril.form_validators.phone_fomat.phone_format import PhoneFormat
from flask_bombril.r import R
from flask_bombril.utils import AlwaysError
from flask_wtf import FlaskForm
from app_contexts.unit_test_app import unit_test_app as app


class MockForm(FlaskForm):
    cep = StringField(validators=[CepFormat()])


class MockFormCanBeEmptyTrue(FlaskForm):
    cep = StringField(validators=[CepFormat(can_be_empty=True)])


class MockFormStopTrue(FlaskForm):
    cep = StringField(validators=[CepFormat(stop=True), AlwaysError()])


class MockFormStopFalse(FlaskForm):
    cep = StringField(validators=[CepFormat(stop=False), AlwaysError()])


class TestCase(BaseTestCase):
    def test_valid_phones(self):
        with app.test_client() as c:
            valid_ceps = [
                "23123-231",
                "02391-124",
                "99884-234",
                "02382-421",
                "93413-451"
            ]

            def assert_valid_cep(valid_cep):
                c.post("/", data=dict(
                    cep=valid_cep
                ))
                form = MockForm()
                self.assertTrue(form.validate_on_submit())

            for cep in valid_ceps:
                assert_valid_cep(cep)

    def test_invalid_ceps(self):
        with app.test_client() as c:
            invalid_ceps = [
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
                "(11) 1234-23234",
                "2312321-231",
                "231232-231",
                "2312-231",
                "23121-",
                "23121-1",
                "23121-23",
                "23121-1234",
                "23129*123",
                "23121@123",
                "23121#123",
                "23123-2a3",
                "2b1v3-223",
            ]

            def assert_invalid_cep(invalid_cep):
                c.post("/", data=dict(
                    tel=invalid_cep
                ))
                form = MockForm()
                self.assertFalse(form.validate_on_submit())
                self.assertEqual(len(form.cep.errors), 1)
                self.assertEqual(form.cep.errors[0], R.string.invalid_cep_format)

            for cep in invalid_ceps:
                assert_invalid_cep(cep)

    def test_can_be_empty_true(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                cep=""
            ))
            mock_form = MockFormCanBeEmptyTrue()
            self.assertTrue(mock_form.validate_on_submit())

            c.post("/", data=dict(
            ))
            mock_form = MockFormCanBeEmptyTrue()
            self.assertTrue(mock_form.validate_on_submit())

    def test_stop_true(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                cep="marco@@"
            ))
            mock_form = MockFormStopTrue()
            self.assertFalse(mock_form.validate_on_submit())
            self.assertEqual(len(mock_form.cep.errors), 1)

    def test_stop_false(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                tel="marco@@"
            ))
            mock_form = MockFormStopFalse()
            self.assertFalse(mock_form.validate_on_submit())
            self.assertEqual(len(mock_form.cep.errors), 2)
