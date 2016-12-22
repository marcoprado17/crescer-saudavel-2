# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from flask_bombril.jinja_filters.filters import assert_defined, assert_callable, call, if_filter, is_static, is_toast, \
    get_level
from unittest import TestCase as BaseTestCase
from jinja2.runtime import Undefined

from flask_bombril.r import R


class TestCase(BaseTestCase):
    def test_assert_defined(self):
        with self.assertRaises(AssertionError):
            assert_defined(Undefined())

        value = R.string.test_message
        returned_value = assert_defined(value)
        self.assertEqual(value, returned_value)

        value = R.dimen.test_int
        returned_value = assert_defined(value)
        self.assertEqual(value, returned_value)

    def test_assert_callable(self):
        value = R.string.test_message
        with self.assertRaises(AssertionError):
            assert_callable(value)

        value = R.dimen.test_int
        with self.assertRaises(AssertionError):
            assert_callable(value)

        def func():
            return R.string.test_message

        returned_func = assert_callable(func)
        self.assertEqual(func, returned_func)
        self.assertEqual(func(), returned_func())

        def func():
            return R.dimen.test_int

        returned_func = assert_callable(func)
        self.assertEqual(func, returned_func)
        self.assertEqual(func(), returned_func())

    def test_call(self):
        def func():
            return R.string.test_message

        returned_value = call(func)
        self.assertEqual(R.string.test_message, returned_value)

        def func():
            return R.dimen.test_int

        returned_value = call(func)
        self.assertEqual(R.dimen.test_int, returned_value)

        def add(a, b):
            return a + b

        returned_value = call(add, 3, 7)
        self.assertEqual(10, returned_value)
        returned_value = call(add, 3, b=7)
        self.assertEqual(10, returned_value)
        returned_value = call(add, a=3, b=7)
        self.assertEqual(10, returned_value)

    def test_if_filter(self):
        value = R.string.test_message
        condition = True
        else_value = R.string.test_message_2

        self.assertEqual(if_filter(value=value, condition=condition, else_value=else_value), value)

        condition = False
        self.assertEqual(if_filter(value=value, condition=condition, else_value=else_value), else_value)

        value = R.dimen.test_int
        condition = True
        else_value = R.dimen.test_int_2

        self.assertEqual(if_filter(value=value, condition=condition, else_value=else_value), value)

        condition = False
        self.assertEqual(if_filter(value=value, condition=condition, else_value=else_value), else_value)

    def test_is_static(self):
        value = "static-warning"
        self.assertTrue(is_static(value))

        value = "static-info"
        self.assertTrue(is_static(value))

        value = "static-success"
        self.assertTrue(is_static(value))

        value = "static-error"
        self.assertTrue(is_static(value))

        value = "toast-warning"
        self.assertFalse(is_static(value))

        value = "toast-info"
        self.assertFalse(is_static(value))

    def test_is_toast(self):
        value = "static-warning"
        self.assertFalse(is_toast(value))

        value = "static-info"
        self.assertFalse(is_toast(value))

        value = "static-success"
        self.assertFalse(is_toast(value))

        value = "static-error"
        self.assertFalse(is_toast(value))

        value = "toast-warning"
        self.assertTrue(is_toast(value))

        value = "toast-info"
        self.assertTrue(is_toast(value))

    def test_get_level(self):
        value = "static-warning"
        self.assertEqual(get_level(value), "warning")

        value = "static-info"
        self.assertEqual(get_level(value), "info")

        value = "static-success"
        self.assertEqual(get_level(value), "success")

        value = "static-error"
        self.assertEqual(get_level(value), "error")

        value = "toast-warning"
        self.assertEqual(get_level(value), "warning")

        value = "toast-info"
        self.assertEqual(get_level(value), "info")
