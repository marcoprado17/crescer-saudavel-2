# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 06/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from unittest import TestCase as BaseTestCase
from flask import request
from app_contexts.unit_test_app import unit_test_app as app
from valid_integer import get_valid_integer


class TestCase(BaseTestCase):
    def test_get_integer(self):
        with app.test_client() as c:
            c.get("/")

            request.args = dict(arg_name="0")
            self.assertEqual(0, get_valid_integer(arg_name="arg_name", default=2))

            request.args = dict(arg_name="3")
            self.assertEqual(3, get_valid_integer(arg_name="arg_name", default=2))

            request.args = dict(arg_name="-3")
            self.assertEqual(-3, get_valid_integer(arg_name="arg_name", default=2))

            request.args = dict(arg_name="abc")
            self.assertEqual(42, get_valid_integer(arg_name="arg_name", default=42))

            request.args = dict(arg_name="3")
            self.assertEqual(42, get_valid_integer(arg_name="arg_name", default=42, possible_values=[]))

            request.args = dict(arg_name="3")
            self.assertEqual(3, get_valid_integer(arg_name="arg_name", default=42, possible_values=[3]))

            request.args = dict(arg_name="3")
            self.assertEqual(42, get_valid_integer(arg_name="arg_name", default=42, possible_values=[1, 2, -10]))

            request.args = dict(arg_name="5")
            self.assertEqual(5, get_valid_integer(arg_name="arg_name", default=42, possible_values=[1, 5, 2, -10]))
