# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 05/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask_bombril.utils import raise_with_stop
from flask_bombril import R


class NotNegativeInteger(object):
    def __init__(self, message=R.string.invalid_not_negative_integer, stop=True):
        self.message = message
        self.stop = stop

    def __call__(self, form, field):
        if callable(self.message):
            self.message = self.message()

        try:
            data_as_int = int(field.data)
            assert data_as_int >= 0
        except:
            raise_with_stop(self)
