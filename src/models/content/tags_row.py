# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 28/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.content.base_content import BaseContent
from proj_extensions import db
from r import R


class TagsRow(BaseContent):
    __tablename__ = "tags_row"

    tag_1_active = db.Column(db.Boolean, default=True, nullable=False)
    tag_1_image_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)
    tag_1_title = db.Column(db.String(R.dimen.tag_title_max_length), default="", nullable=False)
    tag_1_subtitle = db.Column(db.String(R.dimen.tag_subtitle_max_length), default="", nullable=False)

    tag_2_active = db.Column(db.Boolean, default=True, nullable=False)
    tag_2_image_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)
    tag_2_title = db.Column(db.String(R.dimen.tag_title_max_length), default="", nullable=False)
    tag_2_subtitle = db.Column(db.String(R.dimen.tag_subtitle_max_length), default="", nullable=False)

    tag_3_active = db.Column(db.Boolean, default=True, nullable=False)
    tag_3_image_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)
    tag_3_title = db.Column(db.String(R.dimen.tag_title_max_length), default="", nullable=False)
    tag_3_subtitle = db.Column(db.String(R.dimen.tag_subtitle_max_length), default="", nullable=False)

    tag_4_active = db.Column(db.Boolean, default=True, nullable=False)
    tag_4_image_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)
    tag_4_title = db.Column(db.String(R.dimen.tag_title_max_length), default="", nullable=False)
    tag_4_subtitle = db.Column(db.String(R.dimen.tag_subtitle_max_length), default="", nullable=False)

    def get_tag_n_image_filename(self, n):
        return getattr(self, "tag_" + str(n) + "_image_filename")

    def get_tag_n_image_src(self, n):
        return self.get_img_src(self.get_tag_n_image_filename(n), R.string.tag_default_filename)

    def active_tags(self):
        l = []
        if self.tag_1_active:
            l.append(1)
        if self.tag_2_active:
            l.append(2)
        if self.tag_3_active:
            l.append(3)
        if self.tag_4_active:
            l.append(4)
        return l

    def get_tag_n_title(self, n):
        return getattr(self, "tag_" + str(n) + "_title")

    def get_tag_n_subtitle(self, n):
        return getattr(self, "tag_" + str(n) + "_subtitle")

    def has_tag_active(self):
        return self.tag_1_active or self.tag_2_active or self.tag_3_active or self.tag_4_active
