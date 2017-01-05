# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 03/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask_bombril.utils import get_url_arg
from flask_bombril.utils import n_pages
from flask_bombril.r import R


def get_valid_page(page_arg_name, per_page, n_items):
    try:
        curr_page = int(get_url_arg(page_arg_name))
        assert curr_page >= R.dimen.min_page
    except:
        curr_page = R.dimen.min_page
    max_valid_page = n_pages(per_page=per_page, n_items=n_items)
    min_valid_page = R.dimen.min_page
    page = curr_page
    page = max(page, min_valid_page)
    page = min(page, max_valid_page)
    return page
