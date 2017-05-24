# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 14/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.content.base_content import BaseContent
from proj_extensions import db
from r import R


class Contact(BaseContent):
    __tablename__ = "contact"

    address_markdown = db.Column(db.UnicodeText, default="")
    address_html = db.Column(db.UnicodeText, default=u"")
    tel = db.Column(db.String(R.dimen.tel_max_length), default="")
    email = db.Column(db.String(R.dimen.email_max_length), default="")

    facebook_active = db.Column(db.Boolean, default=False, nullable=False)
    facebook_link = db.Column(db.String(R.dimen.link_max_length), default="#")

    youtube_active = db.Column(db.Boolean, default=False, nullable=False)
    youtube_link = db.Column(db.String(R.dimen.link_max_length), default="#")

    twitter_active = db.Column(db.Boolean, default=False, nullable=False)
    twitter_link = db.Column(db.String(R.dimen.link_max_length), default="#")

    googleplus_active = db.Column(db.Boolean, default=False, nullable=False)
    googleplus_link = db.Column(db.String(R.dimen.link_max_length), default="#")

    pintrest_active = db.Column(db.Boolean, default=False, nullable=False)
    pintrest_link = db.Column(db.String(R.dimen.link_max_length), default="#")
