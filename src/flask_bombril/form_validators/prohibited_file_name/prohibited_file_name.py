# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 25/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask_bombril.form_validators.utils import raise_with_stop
from flask_bombril import R


class ProhibitedFileName(object):
    def __init__(self, prohibited_names, message=R.string.prohibited_value, stop=True):
        self.prohibited_values = prohibited_names
        self.message = message
        self.stop = stop

    def __call__(self, form, field):
        message = self.message
        if callable(self.message):
            message = self.message(str(field.data.filename))

        if field.data.filename in self.prohibited_values:
            raise_with_stop(self, message=message)
