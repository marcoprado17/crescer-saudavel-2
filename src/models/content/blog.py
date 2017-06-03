# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 28/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from os.path import isfile, join
from models.content.base_content import BaseContent
from proj_extensions import db
from r import R
from configs import default_app_config as config


class BlogContent(BaseContent):
    __tablename__ = "blog_content"

    main_image_active = db.Column(db.Boolean, default=False, nullable=False)
    main_image_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)

    def get_main_image_src(self):
        if self.main_image_filename is not None and isfile(
                join(config.BLOG_CONTENT_IMAGES_FULL_PATH, self.main_image_filename)):
            return join("/", config.BLOG_CONTENT_IMAGES_FROM_STATIC_PATH, self.main_image_filename)
        else:
            return join("/", config.IMAGES_FROM_STATIC_PATH, R.string.blog_main_image_default_filename)
