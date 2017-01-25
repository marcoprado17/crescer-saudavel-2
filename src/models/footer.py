# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 16/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from proj_exceptions import InconsistentDataBaseError
from proj_extensions import db
from models.base import BaseModel
from r import R


class Footer(BaseModel):
    lower_text = db.Column(db.String(R.dimen.footer_lower_text_max_length))

    @staticmethod
    def get():
        footers = Footer.query.all()
        if len(footers) != 1:
            raise InconsistentDataBaseError
        return footers[0]

    @staticmethod
    def get_attrs_from_form(form):
        return dict(
            lower_text=form.lower_text.data
        )
