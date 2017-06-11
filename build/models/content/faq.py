# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 16/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from proj_extensions import db
from models.base import BaseModel


class FaqContent(BaseModel):
    __tablename__ = "faq_content"

    content_markdown = db.Column(db.UnicodeText, default="")
    content_html = db.Column(db.UnicodeText, default="")
