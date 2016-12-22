# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
import unittest

from utils import get_test_suite_from_test_suites, get_test_suite_from_test_cases
from jinja_filters import TestCase as JinjaFiltersTestCase
from form_validators import test_suite as form_validators_test_suite

test_suite = get_test_suite_from_test_suites([
    get_test_suite_from_test_cases([JinjaFiltersTestCase]),
    form_validators_test_suite
])

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(test_suite)
