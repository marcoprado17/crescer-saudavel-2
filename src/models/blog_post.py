# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 13/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from extensions import db
from r import R


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    active = db.Column(db.Boolean, default=False, nullable=False)
    title = db.Column(db.String(R.dimen.blog_post_title_max_length), nullable=False)
    date = db.Column(db.Date, nullable=False)
    thumbnail = db.Column(db.Text, nullable=False)
    summary = db.Column(db.UnicodeText, nullable=False)
    content = db.Column(db.UnicodeText, nullable=False)


    @staticmethod
    def get_choices(include_none=False):
        blog_post_choices = []
        if include_none:
            blog_post_choices = [(str(0), R.string.none_in_masculine)]

        for id_title in BlogPost.query.order_by(BlogPost.title).with_entities(BlogPost.id, BlogPost.title).all():
            blog_post_choices.append((str(id_title[0]), id_title[1]))

        return blog_post_choices

    @staticmethod
    def get_attrs_from_form(blog_post_form):
        return dict(
            active=blog_post_form.active.data,
            date=blog_post_form.date.data,
            title = blog_post_form.title.data,
            thumbnail = blog_post_form.thumbnail.data,
            summary = blog_post_form.summary.data,
            content = blog_post_form.content.data
        )

    @staticmethod
    def create_from_form(blog_post_form):
        blog_post = BlogPost(
            **BlogPost.get_attrs_from_form(blog_post_form)
        )
        db.session.add(blog_post)
        db.session.commit()
