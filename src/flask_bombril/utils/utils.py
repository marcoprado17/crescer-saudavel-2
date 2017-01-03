# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import unittest
import math
from unittest import TestSuite

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
