# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.content.base_content import BaseContent
from proj_extensions import db


class Header(BaseContent):
    __tablename__ = "header"

    n_visible_categories = db.Column(db.Integer, nullable=False)
