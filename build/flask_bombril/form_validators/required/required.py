# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from wtforms.validators import InputRequired
from flask_bombril.r import R


class Required(InputRequired):
    def __init__(self):
        self.message = R.string.required_field
        super(Required, self).__init__(message=self.message)
