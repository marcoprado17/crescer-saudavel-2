# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from unittest import TestCase as BaseTestCase
from jinja_tests import is_list, is_dict


class TestCase(BaseTestCase):
    def test_is_list(self):
        self.assertTrue(is_list([]))
        self.assertTrue(is_list(["a"]))
        self.assertFalse(is_list({"a": 1}))
        self.assertFalse(is_list("a"))
        self.assertFalse(is_list(42))

    def test_is_dict(self):
        self.assertFalse(is_dict([]))
        self.assertFalse(is_dict(["a"]))
        self.assertTrue(is_dict({"a": 1}))
        self.assertTrue(is_dict({"a": 1, "b": 2}))
        self.assertFalse(is_dict("a"))
        self.assertFalse(is_dict(42))
