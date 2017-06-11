# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.content.base_content import BaseContent
from proj_extensions import db


class ExchangesAndReturnsContent(BaseContent):
    __tablename__ = "exchanges_and_returns_content"

    content_markdown = db.Column(db.UnicodeText, default="")
    content_html = db.Column(db.UnicodeText, default="")
