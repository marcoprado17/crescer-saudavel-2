# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import request
from flask_bombril.form_validators.utils import raise_with_stop
from flask_bombril.r import R


class AllowedFileFormat(object):
    def __init__(self, input_file_name, allowed_extensions, message=R.string.invalid_file_extension,
                 stop=True):
        self.input_file_name = input_file_name
        self.allowed_extensions = allowed_extensions
        self.message = message
        self.stop = stop

    def __call__(self, form, field):
        if callable(self.message):
            self.message = self.message()

        current_file = request.files[self.input_file_name]
        filename = current_file.filename
        allowed_file = '.' in filename and filename.rsplit('.', 1)[1] in self.allowed_extensions

        if not allowed_file:
            raise_with_stop(self)
