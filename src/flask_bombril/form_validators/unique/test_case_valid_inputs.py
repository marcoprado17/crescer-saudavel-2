# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from unittest import TestCase as BaseTestCase
from flask_bombril.form_validators.unique.forms import MockForm
from app_contexts.unit_test_app import unit_test_app as app
from extensions import db


class TestCaseValidInputs(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        with app.app_context():
            db.drop_all()
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test(self):
        with app.app_context():
            with app.test_client() as c:
                c.post("/", data=dict(
                    email="marco.pdsv@gmail.com"
                ))
                form = MockForm()
                self.assertTrue(form.validate_on_submit())
