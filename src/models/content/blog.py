# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 28/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.content.base_content import BaseContent
from proj_extensions import db
from r import R


class BlogContent(BaseContent):
    __tablename__ = "blog_content"

    main_image_active = db.Column(db.Boolean, default=True, nullable=False)
    main_image_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)

    def get_main_image_src(self):
        return self.get_img_src(self.main_image_filename, R.string.blog_main_image_default_filename)
