# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 13/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from sqlalchemy import asc
from sqlalchemy import desc

from proj_extensions import db
from models.base import BaseModel
from proj_utils import SortMethodMap
from r import R


class BlogPost(BaseModel):
    active = db.Column(db.Boolean, default=False, nullable=False)
    title = db.Column(db.String(R.dimen.blog_post_title_max_length), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    thumbnail = db.Column(db.Text, nullable=False)
    summary = db.Column(db.UnicodeText, nullable=False)
    content = db.Column(db.UnicodeText, nullable=False)

    sort_method_map = SortMethodMap([
        (R.id.SORT_METHOD_ID, R.string.id, asc("id")),
        (R.id.SORT_METHOD_TITLE, R.string.title, asc(title)),
        (R.id.SORT_METHOD_NEWEST, R.string.newest, desc(datetime)),
        (R.id.SORT_METHOD_OLDER, R.string.older, asc(datetime)),
    ])

    @staticmethod
    def get_choices(include_none=False):
        blog_post_choices = []
        if include_none:
            blog_post_choices = [(str(0), R.string.none_in_masculine)]

        for id_title in BlogPost.query.order_by(BlogPost.title).with_entities(BlogPost.id, BlogPost.title).all():
            blog_post_choices.append((str(id_title[0]), id_title[1]))

        return blog_post_choices

    @staticmethod
    def get_attrs_from_form(form):
        return dict(
            active=form.active.data,
            datetime=form.datetime.data,
            title = form.title.data,
            thumbnail = form.thumbnail.data,
            summary = form.summary.data,
            content = form.content.data
        )

    def get_formatted_datetime(self):
        return self.datetime.strftime(R.string.default_datetime_format)

    def disable(self):
        self.active = False
        db.session.add(self)
        db.session.commit()

    def to_activate(self):
        self.active = True
        db.session.add(self)
        db.session.commit()
