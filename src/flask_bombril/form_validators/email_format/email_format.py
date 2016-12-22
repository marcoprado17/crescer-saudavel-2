# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
import re

from wtforms.validators import Regexp, HostnameValidation, ValidationError, StopValidation
from flask_bombril.r import R
from flask_bombril.form_validators.utils import raise_with_stop


class EmailFormat(Regexp):
    def __init__(self, stop=True):
        self.message = R.string.validators.invalid_email_format
        self.stop = stop
        self.validate_hostname = HostnameValidation(
            require_tld=True,
        )
        super(EmailFormat, self).__init__(r"^.+@([^.@][^@]+)$", re.IGNORECASE, self.message)

    def __call__(self, form, field, message=None):
        try:
            match = super(EmailFormat, self).__call__(form, field)
            if not self.validate_hostname(match.group(1)):
                raise_with_stop(self)
        except (ValidationError, StopValidation):
            raise_with_stop(self)