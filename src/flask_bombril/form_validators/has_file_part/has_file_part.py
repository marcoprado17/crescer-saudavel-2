# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 25/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import request
from flask_bombril.form_validators.utils import raise_with_stop
from flask_bombril.r import R


class HasFilePart(object):
    def __init__(self, input_file_name, message=R.string.file_part_not_found, stop=True):
        self.input_file_name = input_file_name
        self.message = message
        self.stop = stop

    def __call__(self, form, field):
        if callable(self.message):
            self.message = self.message()

        has_file_part = self.input_file_name in request.files

        if not has_file_part:
            raise_with_stop(self)

        current_file = request.files[self.input_file_name]
        valid_filename = current_file.filename != ''

        if not valid_filename:
            raise_with_stop(self)
