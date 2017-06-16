# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import random
import unittest
import math
import urlparse
import re

from datetime import datetime
from unittest import TestSuite
from flask import request
from wtforms.validators import StopValidation, ValidationError
from flask_bombril.r import R
from proj_extensions import db
from urllib import urlencode


class TestUser(db.Model):
    email = db.Column(db.String(), primary_key=True, unique=True)


class AlwaysError(object):
    def __init__(self):
        pass

    def __call__(self, form, field):
        raise ValidationError(R.string.always_error)


def raise_with_stop(validator, message=None):
    if validator.stop:
        if message:
            raise StopValidation(message)
        else:
            raise StopValidation(validator.message)
    else:
        if message:
            raise ValidationError(message)
        else:
            raise ValidationError(validator.message)


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
    elif default is not None:
        return default
    return None


def get_page_range(curr_page, per_page, min_page):
    first = (curr_page - min_page) * per_page
    last_plus_one = first + per_page
    return first, last_plus_one


def camel_case_to_snake_case(camel_case_word):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_case_word)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def get_random_sublist(original_list, n):
    if len(original_list) == 0 or n <= 0:
        return []
    random_sublist = []
    possible_indexes = range(0, len(original_list))
    random.shuffle(possible_indexes)
    count = 0
    for index in possible_indexes:
        random_sublist.append(original_list[index])
        count += 1
        if count == n:
            break
    return random_sublist


def merge_dicts(*dict_args):
    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


def clamp_integer(n, min_value, max_value):
    returned_value = n
    returned_value = min(returned_value, max_value)
    returned_value = max(min_value, returned_value)
    return returned_value


def current_url(query_params={}, fragment=None):
    url = request.url
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(query_params)
    url_parts[4] = urlencode(query)
    if fragment:
        url_parts[5] = fragment
    return urlparse.urlunparse(url_parts)


def get_int_from_request_arg(arg_name, default=None):
    try:
        return int(request.args.get(arg_name))
    except:
        return default


def get_string_from_request_arg(arg_name, default=None):
    try:
        value = request.args.get(arg_name)
        assert(value is not None)
        return str(value)
    except:
        return default


def get_datetime_from_request_arg_as_unix_ms_timestamp(arg_name, default=None):
    try:
        return datetime.fromtimestamp(int(request.args.get(arg_name))/1000)
    except:
        return default
