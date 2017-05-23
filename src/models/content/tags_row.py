# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 28/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 13/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from proj_exceptions import InconsistentDataBaseError
from proj_extensions import db
from models.base import BaseModel
from r import R


class TagsRow(BaseModel):
    __tablename__ = "tags_row"

    tag_1_image = db.Column(db.Text, default="", nullable=False)
    tag_1_title = db.Column(db.String(R.dimen.tag_title_max_length), default="", nullable=False)
    tag_1_subtitle = db.Column(db.String(R.dimen.tag_subtitle_max_length), default="", nullable=False)

    tag_2_image = db.Column(db.Text, default="", nullable=False)
    tag_2_title = db.Column(db.String(R.dimen.tag_title_max_length), default="", nullable=False)
    tag_2_subtitle = db.Column(db.String(R.dimen.tag_subtitle_max_length), default="", nullable=False)

    tag_3_image = db.Column(db.Text, default="", nullable=False)
    tag_3_title = db.Column(db.String(R.dimen.tag_title_max_length), default="", nullable=False)
    tag_3_subtitle = db.Column(db.String(R.dimen.tag_subtitle_max_length), default="", nullable=False)

    @staticmethod
    def get():
        tags_rows = TagsRow.query.all()
        if len(tags_rows) != 1:
            raise InconsistentDataBaseError
        return tags_rows[0]

    @staticmethod
    def get_attrs_from_form(form):
        return dict(
            tag_1_image=form.tag_1_image.data,
            tag_1_title=form.tag_1_title.data,
            tag_1_subtitle=form.tag_1_subtitle.data,

            tag_2_image=form.tag_2_image.data,
            tag_2_title=form.tag_2_title.data,
            tag_2_subtitle=form.tag_2_subtitle.data,

            tag_3_image=form.tag_3_image.data,
            tag_3_title=form.tag_3_title.data,
            tag_3_subtitle=form.tag_3_subtitle.data
        )
