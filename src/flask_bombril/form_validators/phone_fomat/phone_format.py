# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 14/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import re

from wtforms.validators import Regexp, HostnameValidation, ValidationError, StopValidation
from flask_bombril.r import R
from flask_bombril.form_validators.utils import raise_with_stop


class PhoneFormat(Regexp):
    def __init__(self, stop=True):
        self.message = R.string.invalid_phone_format
        self.stop = stop
        super(PhoneFormat, self).__init__(r"^\(\d\d\) \d\d\d\d{1,2}-\d\d\d\d$", re.IGNORECASE, self.message)

    def __call__(self, form, field, message=None):
        try:
            super(PhoneFormat, self).__call__(form, field)
        except (ValidationError, StopValidation):
            raise_with_stop(self)
