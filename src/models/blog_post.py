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
    datetime = db.Column(db.DateTime, nullable=False)
    thumbnail = db.Column(db.Text, nullable=False)
    summary = db.Column(db.UnicodeText, nullable=False)
    content = db.Column(db.UnicodeText, nullable=False)
    editable = db.Column(db.Boolean, default=True, nullable=False)

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
            datetime=blog_post_form.datetime.data,
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

    @staticmethod
    def update_from_form(blog_post, blog_post_form):
        assert blog_post.editable
        attrs_dict = BlogPost.get_attrs_from_form(blog_post_form)
        for key, val in attrs_dict.iteritems():
            setattr(blog_post, key, val)
        db.session.add(blog_post)
        db.session.commit()

    def get_formatted_datetime(self):
        return self.datetime.strftime(R.string.default_datetime_format)

    @staticmethod
    def get(blog_post_id):
        return BlogPost.query.filter_by(id=blog_post_id).one_or_none()

    @staticmethod
    def update(blog_post_id, **kw):
        blog_post = BlogPost.get(blog_post_id)
        assert blog_post != None
        assert blog_post.editable
        for key, val in kw.iteritems():
            setattr(blog_post, key, val)
        db.session.add(blog_post)
        db.session.commit()
        return blog_post
