# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 06/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from wtforms import SelectFieldBase
from wtforms import widgets
from wtforms.compat import text_type

class SelectFieldWithClasses(SelectFieldBase):
    widget = widgets.Select()

    def __init__(self, label=None, validators=None, coerce=text_type, choices=None, classes="", **kwargs):
        super(SelectFieldWithClasses, self).__init__(label, validators, **kwargs)
        self.coerce = coerce
        self.choices = choices
        self.classes = classes

    def iter_choices(self):
        for value, label in self.choices:
            yield (value, label, self.coerce(value) == self.data)

    def process_data(self, value):
        try:
            self.data = self.coerce(value)
        except (ValueError, TypeError):
            self.data = None

    def process_formdata(self, valuelist):
        if valuelist:
            try:
                self.data = self.coerce(valuelist[0])
            except ValueError:
                raise ValueError(self.gettext('Invalid Choice: could not coerce'))

    def pre_validate(self, form):
        for v, _ in self.choices:
            if self.data == v:
                break
        else:
            raise ValueError(self.gettext('Not a valid choice'))
