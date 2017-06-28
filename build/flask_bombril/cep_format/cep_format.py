# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 19/02/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import re

from wtforms.validators import Regexp, ValidationError, StopValidation
from flask_bombril.r import R
from flask_bombril.utils import raise_with_stop

class CepFormat(Regexp):
    def __init__(self, stop=True, can_be_empty=False):
        self.message = R.string.invalid_cep_format
        self.stop = stop
        self.can_be_empty = can_be_empty
        super(CepFormat, self).__init__(r"^\d{5}-\d{3}$", re.IGNORECASE, self.message)

    def __call__(self, form, field, message=None):
        if self.can_be_empty and ( field.data == None or field.data == ""):
            return
        try:
            super(CepFormat, self).__call__(form, field)
        except (ValidationError, StopValidation):
            raise_with_stop(self)
