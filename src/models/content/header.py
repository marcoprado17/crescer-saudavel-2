# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.content.base_content import BaseContent
from proj_extensions import db
from r import R


class HeaderContent(BaseContent):
    __tablename__ = "header_content"

    n_visible_categories = db.Column(db.Integer, nullable=False)
    logo_image_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)
    blog_menu_icon_image_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)

    def get_logo_img_src(self):
        return self.get_img_src(self.logo_image_filename, R.string.default_logo_image_filename)

    def get_blog_menu_icon_img_src(self):
        return self.get_img_src(self.blog_menu_icon_image_filename, R.string.default_menu_icon_filename)

    def has_blog_icon_img(self):
        return self.has_image(self.blog_menu_icon_image_filename)
