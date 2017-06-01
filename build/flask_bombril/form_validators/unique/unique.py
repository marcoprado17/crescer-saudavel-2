# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask_bombril.r import R
from flask_bombril.utils import raise_with_stop


class Unique(object):
    def __init__(self, model, field, message=R.string.unique_field, stop=True, data_key=None):
        self.message = message
        self.model = model
        self.field = field
        self.stop = stop
        self.data_key = data_key

    def __call__(self, form, field):
        if callable(self.message):
            self.message = self.message()

        if self.data_key is None:
            check = self.model.query.filter(self.field == field.data).first()
        else:
            check = self.model.query.filter(self.field == getattr(field.data, self.data_key)).first()
        print "###"
        print "__call__"
        from pprint import pprint
        pprint(check)
        pprint(self.data_key)
        pprint(self.model)
        pprint(self.field)
        if self.data_key is not None:
            pprint(getattr(field.data, self.data_key))
        if check:
            raise_with_stop(self)
