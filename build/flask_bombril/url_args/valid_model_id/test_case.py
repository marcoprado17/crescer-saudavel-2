# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 05/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from unittest import TestCase as BaseTestCase

from flask import request

from app_contexts.unit_test_app import unit_test_app as app
from proj_extensions import db
from valid_model_id import get_valid_model_id

class TestValidModelId(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

class TestCase(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        with app.app_context():
            db.drop_all()
            db.create_all()
            db.session.add(TestValidModelId())
            db.session.add(TestValidModelId())
            db.session.add(TestValidModelId())
            db.session.commit()

    @classmethod
    def tearDownClass(cls):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_valid_model_id(self):
        with app.test_client() as c:
            c.get("/?" + "arg_name="+"0")
            self.assertEqual("default", get_valid_model_id(model=TestValidModelId, arg_name="arg_name", include_zero=False,
                                                   default="default"))

            c.get("/?" + "arg_name=" + "0")
            self.assertEqual(0,
                             get_valid_model_id(model=TestValidModelId, arg_name="arg_name", include_zero=True,
                                                default="default"))

            c.get("/?" + "arg_name=" + "1")
            self.assertEqual(1, get_valid_model_id(model=TestValidModelId, arg_name="arg_name", include_zero=False, default=1))

            c.get("/?" + "arg_name=" + "2")
            self.assertEqual(2, get_valid_model_id(model=TestValidModelId, arg_name="arg_name", include_zero=False,
                                                   default=1))

            c.get("/?" + "arg_name=" + "3")
            self.assertEqual(3, get_valid_model_id(model=TestValidModelId, arg_name="arg_name", include_zero=False,
                                                   default=1))

            c.get("/?" + "arg_name=" + "4")
            self.assertEqual(1, get_valid_model_id(model=TestValidModelId, arg_name="arg_name", include_zero=False,
                                                   default=1))

            c.get("/?" + "arg_name=" + "42")
            self.assertEqual(None, get_valid_model_id(model=TestValidModelId, arg_name="arg_name", include_zero=False,
                                                   default=None))
