# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from sqlalchemy.ext.hybrid import hybrid_property
from proj_exceptions import InconsistentDataBaseError
from proj_extensions import db
from models.base import BaseModel
from proj_utils import parse_markdown


class Payment(BaseModel):
    __tablename__ = "payment"

    _content_markdown = db.Column(db.UnicodeText, default=u"")
    content_html = db.Column(db.UnicodeText, default=u"")

    @hybrid_property
    def content_markdown(self):
        return self._content_markdown

    @content_markdown.setter
    def content_markdown(self, value):
        self._content_markdown = value
        self.content_html = parse_markdown(value)

    @staticmethod
    def get():
        all_payments = Payment.query.all()
        if len(all_payments) != 1:
            raise InconsistentDataBaseError
        return all_payments[0]

    @staticmethod
    def get_attrs_from_form(form):
        return dict(
            content_markdown=form.content.data
        )
