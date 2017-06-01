# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 16/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.content.base_content import BaseContent
from proj_extensions import db


class Footer(BaseContent):
    __tablename__ = "footer"

    lower_text_markdown = db.Column(db.UnicodeText, default="")
    lower_text_html = db.Column(db.UnicodeText, default="")
