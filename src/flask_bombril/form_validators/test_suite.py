# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
import unittest
from flask_bombril.utils import get_test_suite_from_test_cases
from email_format import TestCase as EmailFormatTestCase
from equal_to import TestCase as EqualToTestCase
from length import TestCase as LengthTestCase
from required import TestCase as RequiredTestCase
from unique import TestCaseInvalidInputs as UniqueTestCaseInvalidInputs
from unique import TestCaseValidInputs as UniqueTestCaseValidInputs

test_suite = get_test_suite_from_test_cases([
    EmailFormatTestCase,
    EqualToTestCase,
    LengthTestCase,
    RequiredTestCase,
    UniqueTestCaseInvalidInputs,
    UniqueTestCaseValidInputs
])

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(test_suite)
