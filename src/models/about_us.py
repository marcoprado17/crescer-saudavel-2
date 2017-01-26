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


class AboutUs(BaseModel):
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
        all_about_us = AboutUs.query.all()
        if len(all_about_us) != 1:
            raise InconsistentDataBaseError
        return all_about_us[0]

    @staticmethod
    def get_attrs_from_form(form):
        return dict(
            content_markdown=form.content.data
        )
