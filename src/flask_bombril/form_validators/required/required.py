# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from wtforms.validators import InputRequired
from flask_bombril.r import R


class Required(InputRequired):
    def __init__(self):
        self.message = R.string.validators.required_field
        super(Required, self).__init__(message=self.message)
