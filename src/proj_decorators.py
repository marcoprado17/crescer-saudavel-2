# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 09/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from functools import wraps
from flask_bombril.utils import camel_case_to_snake_case


def valid_form(FormClass):
    def real_decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            form = FormClass()
            if form.validate_on_submit():
                kwargs["form"] = form
                return func(*args, **kwargs)
            elif "csrf_token" in form.errors:
                return "", 403
            else:
                return "", 400
        return decorated_function
    return real_decorator

def safe_id_to_model_elem(model):
    '''
    The name of the variable that represents the id of the model element is the name of the model + "Id" converted to snake_case
    The name of the variable that represents the model element is the name of the model converted to snake_case
    '''
    def real_decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            elem_id_name = camel_case_to_snake_case(model.__name__ + "Id")
            elem_name = camel_case_to_snake_case(model.__name__)
            id = kwargs[elem_id_name]
            model_elem = model.get(id)
            del kwargs[elem_id_name]
            kwargs[elem_name] = model_elem
            if model_elem == None:
                return "", 404
            else:
                return func(*args, **kwargs)
        return decorated_function
    return real_decorator
