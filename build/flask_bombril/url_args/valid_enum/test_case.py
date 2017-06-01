# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 06/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from unittest import TestCase as BaseTestCase

from enum import unique, Enum
from flask import request
from app_contexts.unit_test_app import unit_test_app as app
from valid_enum import get_valid_enum

@unique
class test_enum(Enum):
    DEFAULT = 0
    A = 1
    B = 2
    C = 3

class TestCase(BaseTestCase):
    def test_get_valid_enum(self):
        with app.test_client() as c:
            c.get("/")

            request.args = dict(arg_name="1")
            self.assertEqual(test_enum.A, get_valid_enum(arg_name="arg_name", enum=test_enum, default=test_enum.DEFAULT, possible_values=[test_enum.A, test_enum.B, test_enum.C]))

            request.args = dict(arg_name="2")
            self.assertEqual(test_enum.B, get_valid_enum(arg_name="arg_name", enum=test_enum, default=test_enum.DEFAULT,
                                                         possible_values=[test_enum.A, test_enum.B, test_enum.C]))

            request.args = dict(arg_name="3")
            self.assertEqual(test_enum.C, get_valid_enum(arg_name="arg_name", enum=test_enum, default=test_enum.DEFAULT,
                                                         possible_values=[test_enum.A, test_enum.B, test_enum.C]))

            request.args = dict(arg_name="4")
            self.assertEqual(test_enum.DEFAULT, get_valid_enum(arg_name="arg_name", enum=test_enum, default=test_enum.DEFAULT,
                                                         possible_values=[test_enum.A, test_enum.B, test_enum.C]))

            request.args = dict(arg_name="42")
            self.assertEqual(test_enum.DEFAULT, get_valid_enum(arg_name="arg_name", enum=test_enum, default=test_enum.DEFAULT,
                                                         possible_values=[test_enum.A, test_enum.B, test_enum.C]))

            request.args = dict(arg_name="0")
            self.assertEqual(test_enum.DEFAULT, get_valid_enum(arg_name="arg_name", enum=test_enum, default=test_enum.DEFAULT,
                                                         possible_values=[test_enum.A, test_enum.B, test_enum.C]))

            request.args = dict(arg_name="1")
            self.assertEqual(test_enum.DEFAULT,
                             get_valid_enum(arg_name="arg_name", enum=test_enum, default=test_enum.DEFAULT,
                                            possible_values=[test_enum.B, test_enum.C]))

            request.args = dict(arg_name="2")
            self.assertEqual(test_enum.DEFAULT,
                             get_valid_enum(arg_name="arg_name", enum=test_enum, default=test_enum.DEFAULT,
                                            possible_values=[test_enum.A, test_enum.C]))

            request.args = dict(arg_name="3")
            self.assertEqual(test_enum.DEFAULT,
                             get_valid_enum(arg_name="arg_name", enum=test_enum, default=test_enum.DEFAULT,
                                            possible_values=[test_enum.B, test_enum.A]))
