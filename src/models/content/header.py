# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from proj_exceptions import InconsistentDataBaseError
from proj_extensions import db
from models.base import BaseModel
from r import R


class Header(BaseModel):
    __tablename__ = "header"

    n_visible_categories = db.Column(db.Integer, default=R.dimen.default_n_visible_categories)

    @staticmethod
    def get():
        headers = Header.query.all()
        if len(headers) != 1:
            raise InconsistentDataBaseError
        return headers[0]

    @staticmethod
    def get_attrs_from_form(form):
        return dict(
            n_visible_categories=int(form.n_visible_categories.data)
        )
