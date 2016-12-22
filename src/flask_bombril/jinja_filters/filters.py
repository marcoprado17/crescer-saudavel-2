# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from jinja2.runtime import Undefined

from flask_bombril.r import R


def assert_defined(value):
    assert not isinstance(value, Undefined)
    return value


def assert_callable(value):
    assert callable(value)
    return value


def call(func, *args, **kwargs):
    return func(*args, **kwargs)


def if_filter(value, condition, else_value=""):
    if condition:
        return value
    return else_value

def is_static(value):
    return value.split(R.string.category_separator)[0] == R.string.static

def is_toast(value):
    return value.split(R.string.category_separator)[0] == R.string.toast

def get_level(value):
    return value.split("-")[1]
