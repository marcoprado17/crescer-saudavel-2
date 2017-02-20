# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 13/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import url_for
from sqlalchemy import asc
from sqlalchemy import desc
from sqlalchemy.ext.hybrid import hybrid_property
from proj_extensions import db
from models.base import BaseModel
from proj_utils import SortMethodMap, parse_markdown
from r import R


class BlogPost(BaseModel):
    active = db.Column(db.Boolean, default=False, nullable=False)
    title = db.Column(db.String(R.dimen.blog_post_title_max_length), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    thumbnail = db.Column(db.Text)
    _summary_markdown = db.Column(db.UnicodeText, nullable=False)
    summary_html = db.Column(db.UnicodeText, nullable=False)
    _content_markdown = db.Column(db.UnicodeText, nullable=False)
    content_html = db.Column(db.UnicodeText, nullable=False)

    sort_method_map = SortMethodMap([
        (R.id.SORT_METHOD_ID, R.string.id, asc("id")),
        (R.id.SORT_METHOD_TITLE, R.string.title, asc(title)),
        (R.id.SORT_METHOD_NEWEST, R.string.newest, desc(datetime)),
        (R.id.SORT_METHOD_OLDER, R.string.older, asc(datetime)),
    ])

    @hybrid_property
    def summary_markdown(self):
        return self._summary_markdown

    @summary_markdown.setter
    def summary_markdown(self, value):
        self._summary_markdown = value
        self.summary_html = parse_markdown(value)

    @hybrid_property
    def content_markdown(self):
        return self._content_markdown

    @content_markdown.setter
    def content_markdown(self, value):
        self._content_markdown = value
        self.content_html = parse_markdown(value)

    @staticmethod
    def get_choices(include_none=False, only_active=True):
        blog_post_choices = []

        if include_none:
            blog_post_choices = [(str(0), R.string.none_in_masculine)]

        for (id, title, active) in BlogPost.query.order_by(BlogPost.title).with_entities(BlogPost.id, BlogPost.title, BlogPost.active).all():
            if not only_active or (only_active and active):
                blog_post_choices.append((str(id), title))

        return blog_post_choices

    @staticmethod
    def get_attrs_from_form(form):
        return dict(
            active=form.active.data,
            datetime=form.datetime.data,
            title=form.title.data,
            thumbnail=form.thumbnail.data,
            summary_markdown=form.summary.data,
            content_markdown=form.content.data
        )

    def get_formatted_datetime(self):
        return self.datetime.strftime(R.string.default_date_format)

    def disable(self):
        self.active = False
        db.session.add(self)
        db.session.commit()

    def to_activate(self):
        self.active = True
        db.session.add(self)
        db.session.commit()

    def get_img_src_of_thumbnail(self):
        thumbnail_name = self.thumbnail
        if thumbnail_name is None or thumbnail_name == "":
            thumbnail_name = R.string.default_blog_post_thumbnail_name
        return url_for("static", filename="imgs/blog_thumbnails/" + thumbnail_name)

    def get_day(self):
        return self.datetime.strftime(R.string.day_format)

    def get_month(self):
        return self.datetime.strftime(R.string.month_format)

    def get_href(self):
        return url_for("client_blog.blog_post", **{R.string.blog_post_id_arg_name: self.id})
