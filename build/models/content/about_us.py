# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 16/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.content.base_content import BaseContent
from proj_extensions import db


class AboutUs(BaseContent):
    __tablename__ = "about_us"

    summary_markdown = db.Column(db.UnicodeText, default="")
    summary_html = db.Column(db.UnicodeText, default="")
    content_markdown = db.Column(db.UnicodeText, default="")
    content_html = db.Column(db.UnicodeText, default="")
