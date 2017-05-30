# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from unittest import TestCase as BaseTestCase
from flask import request
from flask_bombril.url_args.boolean.boolean import get_boolean_url_arg
from app_contexts.unit_test_app import unit_test_app as app

class TestCase(BaseTestCase):
    def test_get_boolean_url_arg(self):
        with app.test_client() as c:
            c.get("/")

            request.args = dict(my_bool_1="False")
            self.assertEqual(False, get_boolean_url_arg("my_bool_1", True))

            request.args = dict(my_bool_1="True")
            self.assertEqual(True, get_boolean_url_arg("my_bool_1", True))

            request.args = dict(my_bool_1="Falsadse")
            self.assertEqual(True, get_boolean_url_arg("my_bool_1", True))

            request.args = dict(my_bool_1="42")
            self.assertEqual(False, get_boolean_url_arg("my_bool_1", False))

            request.view_args = dict(my_bool_2="False")
            self.assertEqual(False, get_boolean_url_arg("my_bool_2", True))

            request.view_args = dict(my_bool_2="True")
            self.assertEqual(True, get_boolean_url_arg("my_bool_2", True))

            request.view_args = dict(my_bool_2="Falsadse")
            self.assertEqual(True, get_boolean_url_arg("my_bool_2", True))

            request.view_args = dict(my_bool_2="42")
            self.assertEqual(False, get_boolean_url_arg("my_bool_2", False))
