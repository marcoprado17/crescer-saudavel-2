# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 09/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from functools import wraps

def valid_form(FormClass):
    def real_decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            form = FormClass()
            if form.validate_on_submit():
                if 'form' in func.__code__.co_varnames:
                    return func(*args, form=form, **kwargs)
                else:
                    return func(*args, **kwargs)
            elif "csrf_token" in form.errors:
                return "", 403
            else:
                return "", 400
        return decorated_function
    return real_decorator