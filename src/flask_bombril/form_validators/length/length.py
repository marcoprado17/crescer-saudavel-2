# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
import gettext

from flask_bombril.form_validators.utils import raise_with_stop
from flask_bombril.r import R


class Length(object):
    def __init__(self, min_length=-1, max_length=-1, message=None, stop=True):
        assert min_length >= -1 and max_length >= -1
        assert min_length != -1 or max_length != -1
        assert max_length == -1 or min_length <= max_length
        self.min = min_length
        self.max = max_length
        self.message = message
        self.stop = stop

    def __call__(self, form, field):
        if callable(self.message):
            self.message = self.message()

        l = field.data and len(field.data) or 0
        if l < self.min or self.max != -1 and l > self.max:
            message = self.message
            if message is None:
                if self.max == -1:
                    message = gettext.ngettext(
                        R.string.validators.field_min_length_singular,
                        R.string.validators.field_min_length_plural,
                        self.min) % dict(min_length=self.min)
                elif self.min == -1:
                    message = gettext.ngettext(
                        R.string.validators.field_max_length_singular,
                        R.string.validators.field_max_length_plural,
                        self.max) % dict(max_length=self.max)
                else:
                    message = R.string.validators.field_length_range % dict(min_length=self.min, max_length=self.max)

            raise_with_stop(self, message=message)
