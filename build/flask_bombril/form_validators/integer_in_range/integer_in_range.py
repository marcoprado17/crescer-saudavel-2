# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 23/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask_bombril.utils import raise_with_stop
from flask_bombril import R


class IntegerInRange(object):
    def __init__(self, min_value=R.dimen.integer_in_range_default_min_value, max_value=R.dimen.integer_in_range_default_max_value, message=None, stop=True):
        self.min_value=min_value
        self.max_value=max_value
        if message is not None:
            self.message=message
        else:
            self.message = R.string.integer_in_range_error_message(min_value=min_value, max_value=max_value)
        self.stop = stop

    def __call__(self, form, field):
        if callable(self.message):
            self.message = self.message()

        try:
            data_as_int = int(field.data)
            assert data_as_int >= self.min_value and data_as_int <= self.max_value
        except:
            raise_with_stop(self)
