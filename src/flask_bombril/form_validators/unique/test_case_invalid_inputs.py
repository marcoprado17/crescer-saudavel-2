# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from unittest import TestCase as BaseTestCase
from flask_bombril.form_validators.unique.forms import MockForm, MockFormCustomMessage, \
    MockFormCustomCallableMessage, MockFormStopTrue, MockFormStopFalse
from flask_bombril.r import R
from flask_bombril.form_validators.utils import TestUser
from app_contexts.unit_test_app import unit_test_app as app
from extensions import db

email = "marco.pdsv@gmail.com"


class TestCaseInvalidInputs(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        with app.app_context():
            db.drop_all()
            db.create_all()
            db.session.add(TestUser(email=email))
            db.session.commit()

    @classmethod
    def tearDownClass(cls):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_fail_default_message(self):
        with app.app_context():
            with app.test_client() as c:
                c.post("/", data=dict(
                    email=email
                ))
                form = MockForm()
                self.assertFalse(form.validate_on_submit())
                self.assertEqual(len(form.email.errors), 1)
                self.assertEqual(form.email.errors[0], R.string.validators.unique_field)

    def test_fail_custom_message(self):
        with app.app_context():
            with app.test_client() as c:
                c.post("/", data=dict(
                    email=email
                ))
                form = MockFormCustomMessage()
                self.assertFalse(form.validate_on_submit())
                self.assertEqual(len(form.email.errors), 1)
                self.assertEqual(form.email.errors[0], R.string.validators.email_already_registered)

    def test_fail_custom_callable_message(self):
        with app.app_context():
            with app.test_client() as c:
                c.post("/", data=dict(
                    email=email
                ))
                form = MockFormCustomCallableMessage()
                self.assertFalse(form.validate_on_submit())
                self.assertEqual(len(form.email.errors), 1)
                self.assertEqual(form.email.errors[0], R.string.validators.email_already_registered)

    def test_stop_true(self):
        with app.app_context():
            with app.test_client() as c:
                c.post("/", data=dict(
                    email=email
                ))
                form = MockFormStopTrue()
                self.assertFalse(form.validate_on_submit())
                self.assertEqual(len(form.email.errors), 1)

    def test_stop_false(self):
        with app.app_context():
            with app.test_client() as c:
                c.post("/", data=dict(
                    email=email
                ))
                form = MockFormStopFalse()
                self.assertFalse(form.validate_on_submit())
                self.assertEqual(len(form.email.errors), 2)
