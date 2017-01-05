# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 05/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask_bombril.utils import get_url_arg


def get_valid_model_id(model, arg_name, include_zero, default):
    try:
        model_id = int(get_url_arg(arg_name))
        assert model.query.filter_by(id=model_id).one_or_none() != None or (model_id == 0 and include_zero)
        return model_id
    except:
        return default
