# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 05/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import re
from wtforms.validators import Regexp, ValidationError
from flask_bombril import R
from flask_bombril.form_validators.utils import raise_with_stop


class Price(Regexp):
    def __init__(self, message=R.string.invalid_price_format, stop=True):
        self.message = message
        self.stop = stop
        super(Price, self).__init__(r'^\d{1,10}[,.]\d\d$', re.IGNORECASE, self.message)

    def __call__(self, form, field):
        if callable(self.message):
            self.message = self.message()

        try:
            super(Price, self).__call__(form, field, self.message)
        except ValidationError:
            raise_with_stop(self)
