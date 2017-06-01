# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 06/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask_bombril.utils import get_url_arg


def get_valid_enum(arg_name, enum, default, possible_values):
    try:
        arg = enum(int(get_url_arg(arg_name)))
        assert arg in possible_values
        return arg
    except:
        return default
