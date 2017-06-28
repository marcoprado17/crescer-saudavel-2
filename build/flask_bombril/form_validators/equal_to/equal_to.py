# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask_bombril.utils import raise_with_stop
from flask_bombril.exceptions import InvalidFieldError
from flask_bombril.r import R


class EqualTo(object):
    def __init__(self, field_name, message=None, stop=True):
        self.field_name = field_name
        self.message = message
        self.stop = stop

    def __call__(self, form, field):
        if callable(self.message):
            self.message = self.message()

        try:
            other = form[self.field_name]
        except KeyError:
            message = R.string.invalid_field_name % dict(field_name=self.field_name)
            raise InvalidFieldError(message)
        if field.data != other.data:
            message = self.message
            if message is None:
                message = R.string.field_must_be_equal_to % dict(other_name=self.field_name)
            raise_with_stop(self, message=message)
