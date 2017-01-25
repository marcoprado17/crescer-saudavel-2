# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 16/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from proj_exceptions import InconsistentDataBaseError
from proj_extensions import db
from models.base import BaseModel


class Faq(BaseModel):
    content = db.Column(db.UnicodeText)

    @staticmethod
    def get():
        faqs = Faq.query.all()
        if len(faqs) != 1:
            raise InconsistentDataBaseError
        return faqs[0]

    @staticmethod
    def get_attrs_from_form(form):
        return dict(
            content=form.content.data
        )
