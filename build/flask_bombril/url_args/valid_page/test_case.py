# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 03/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from unittest import TestCase as BaseTestCase
from flask_bombril.r import R
from valid_page import get_valid_page
from app_contexts.unit_test_app import unit_test_app as app

class TestCase(BaseTestCase):
    def test_get_valid_page(self):
        with app.test_client() as c:
            self.check(c=c, page_arg_value="1", expected_page=1, per_page=1, n_items=0)
            self.check(c=c, page_arg_value="1", expected_page=1, per_page=1, n_items=1)

            self.check(c=c, page_arg_value="1", expected_page=1, per_page=5, n_items=3)
            self.check(c=c, page_arg_value="1", expected_page=1, per_page=5, n_items=5)
            self.check(c=c, page_arg_value="1", expected_page=1, per_page=5, n_items=6)
            self.check(c=c, page_arg_value="1", expected_page=1, per_page=5, n_items=9)
            self.check(c=c, page_arg_value="1", expected_page=1, per_page=5, n_items=10)
            self.check(c=c, page_arg_value="1", expected_page=1, per_page=5, n_items=11)
            self.check(c=c, page_arg_value="1", expected_page=1, per_page=5, n_items=14)
            self.check(c=c, page_arg_value="1", expected_page=1, per_page=5, n_items=15)
            self.check(c=c, page_arg_value="1", expected_page=1, per_page=5, n_items=16)
            self.check(c=c, page_arg_value="1", expected_page=1, per_page=5, n_items=18)

            self.check(c=c, page_arg_value="2", expected_page=1, per_page=5, n_items=3)
            self.check(c=c, page_arg_value="3", expected_page=1, per_page=5, n_items=5)
            self.check(c=c, page_arg_value="2", expected_page=2, per_page=5, n_items=6)
            self.check(c=c, page_arg_value="7", expected_page=2, per_page=5, n_items=9)
            self.check(c=c, page_arg_value="3", expected_page=2, per_page=5, n_items=10)
            self.check(c=c, page_arg_value="3", expected_page=3, per_page=5, n_items=11)
            self.check(c=c, page_arg_value="12", expected_page=3, per_page=5, n_items=14)
            self.check(c=c, page_arg_value="10", expected_page=3, per_page=5, n_items=15)
            self.check(c=c, page_arg_value="4", expected_page=4, per_page=5, n_items=16)
            self.check(c=c, page_arg_value="42", expected_page=4, per_page=5, n_items=18)

    def check(self, c, page_arg_value, expected_page, per_page, n_items):
        c.get("/?" +
              R.string.page_arg_name + "=" + page_arg_value)
        self.assertEqual(expected_page, get_valid_page(page_arg_name=R.string.page_arg_name, per_page=per_page, n_items=n_items))
