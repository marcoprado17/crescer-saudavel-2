# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 16/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from sqlalchemy.ext.hybrid import hybrid_property

from proj_exceptions import InconsistentDataBaseError
from proj_extensions import db
from models.base import BaseModel
from proj_utils import parse_markdown
from r import R


class Footer(BaseModel):
    __tablename__ = "footer"

    _lower_text_markdown = db.Column(db.UnicodeText, default=u"")
    lower_text_html = db.Column(db.UnicodeText, default=u"")

    @hybrid_property
    def lower_text_markdown(self):
        return self._lower_text_markdown

    @lower_text_markdown.setter
    def lower_text_markdown(self, value):
        self._lower_text_markdown = value
        self.lower_text_html = parse_markdown(value)

    @staticmethod
    def get():
        footers = Footer.query.all()
        if len(footers) != 1:
            raise InconsistentDataBaseError
        return footers[0]

    @staticmethod
    def get_attrs_from_form(form):
        return dict(
            lower_text_markdown=form.lower_text.data
        )
