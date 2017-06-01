# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import ast
from flask_bombril.utils import get_url_arg

def get_boolean_url_arg(arg_name, default):
    assert isinstance(default, bool)
    try:
        arg = get_url_arg(arg_name)
        arg = ast.literal_eval(arg)
        assert isinstance(arg, bool)
        return arg
    except:
        return default
