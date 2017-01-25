# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 16/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from proj_exceptions import InconsistentDataBaseError
from proj_extensions import db
from models.base import BaseModel
from proj_utils import parse_markdown


class AboutUs(BaseModel):
    content = db.Column(db.UnicodeText, default="")

    @staticmethod
    def get():
        all_about_us = AboutUs.query.all()
        if len(all_about_us) != 1:
            raise InconsistentDataBaseError
        return all_about_us[0]

    @staticmethod
    def get_attrs_from_form(form):
        return dict(
            content=parse_markdown(form.content.data)
        )
