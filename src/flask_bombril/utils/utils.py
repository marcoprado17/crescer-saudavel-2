# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import unittest
import math
from unittest import TestSuite

import re
from flask import request

from flask_bombril.r import R


def get_test_suite_from_test_cases(test_cases):
    suite = TestSuite()
    for test_class in test_cases:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite


def get_test_suite_from_test_suites(suites):
    return unittest.TestSuite(suites)


def stringfy_list(l):
    stringfied_list = ""
    first_idx = 0
    last_idx = len(l) - 1
    for idx, elem in enumerate(l):
        if idx == first_idx:
            stringfied_list = str(elem)
        elif idx == last_idx:
            stringfied_list += " " + R.string.and_word + " " + str(elem)
        else:
            stringfied_list += R.string.comma + " " + str(elem)
    return stringfied_list


def n_pages(per_page, n_items):
    if n_items == 0:
        return 1
    return int(math.ceil(float(n_items)/per_page))


def slice_items(items, page, per_page):
    first = (page-1)*per_page
    last = min(first+per_page, len(items)+1)
    return items[first:last]


def get_url_args():
    request_args = {}
    if request.args and len(request.args) > 0:
        request_args = request.args
    request_view_args = {}
    if request.view_args and len(request.view_args) > 0:
        request_view_args = request.view_args
    url_args = {}
    for key, val in request_args.iteritems():
        url_args[key] = val
    for key, val in request_view_args.iteritems():
        url_args[key] = val
    return url_args

def get_url_arg(arg_name, default=None):
    url_args = get_url_args()
    if arg_name in url_args:
        return url_args[arg_name]
    elif default != None:
        return default
    return None

def get_page_range(curr_page, per_page, min_page):
    first = (curr_page - min_page) * per_page
    last_plus_one = first + per_page
    return (first, last_plus_one)

def camel_case_to_snake_case(camel_case_word):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_case_word)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
