# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 05/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import markdown

from flask_bombril.form_validators.utils import raise_with_stop
from flask_bombril import R


class MarkdownValidator(object):
    def __init__(self, message=R.string.invalid_markdown_format, stop=True):
        self.message = message
        self.stop = stop

    def __call__(self, form, field):
        if callable(self.message):
            self.message = self.message()

        try:
            markdown.markdown(field.data)
        except Exception:
            raise_with_stop(self)
