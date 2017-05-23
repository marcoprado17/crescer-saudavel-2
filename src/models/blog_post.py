# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 13/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from os.path import isfile, join
from proj_extensions import db
from models.base import BaseModel
from r import R
from configs import default_app_config as config


class BlogPost(BaseModel):
    __tablename__ = "blog_post"

    __searchable__ = [
        "title",
        "summary_html",
        "content_html"
    ]

    active = db.Column(db.Boolean, default=False, nullable=False)
    title = db.Column(db.String(R.dimen.blog_post_title_max_length), nullable=False)
    date = db.Column(db.Date, nullable=False)
    thumbnail_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)
    summary_markdown = db.Column(db.UnicodeText, nullable=False, default="")
    summary_html = db.Column(db.UnicodeText, nullable=False, default="")
    content_markdown = db.Column(db.UnicodeText, nullable=False, default="")
    content_html = db.Column(db.UnicodeText, nullable=False, default="")

    def get_thumbnail_src(self):
        if self.thumbnail_filename is not None and isfile(join(config.BLOG_THUMBNAIL_IMAGES_FULL_PATH, self.thumbnail_filename)):
            return join("/", config.BLOG_THUMBNAIL_IMAGES_FROM_STATIC_PATH, self.thumbnail_filename)
        else:
            return join("/", config.IMAGES_FROM_STATIC_PATH, R.string.blog_thumbnail_default_filename)

    def get_href(self):
        return None
