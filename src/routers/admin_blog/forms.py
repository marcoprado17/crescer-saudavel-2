# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 16/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask_wtf import FlaskForm
from wtforms import DateField, StringField, BooleanField, SelectField, TextAreaField, SubmitField
from flask_bombril.form_validators import MarkdownValidator
from flask_bombril.form_validators import Length
from flask_bombril.form_validators import Required
from r import R
from wrappers.base.utils import get_image_choices


class BlogPostForm(FlaskForm):
    active = BooleanField(
        label=R.string.active,
        default=True
    )
    date = DateField(
        label = R.string.date,
        validators= [
            Required()
        ]
    )
    title = StringField(
        label=R.string.title,
        validators=[
            Required(),
            Length(max_length=R.dimen.blog_post_title_max_length)
        ]
    )
    thumbnail = SelectField(
        label=R.string.thumbnail,
        validators=[
            Required()
        ],
        render_kw=dict(
            tooltip=R.string.thumbnail_tooltip
        )
    )
    summary = TextAreaField(
        label=R.string.summary,
        validators=[
            Required(),
            MarkdownValidator()
        ]
    )
    content = TextAreaField(
        label=R.string.content,
        validators=[
            Required(),
            MarkdownValidator()
        ]
    )

    def __init__(self, **kwargs):
        super(BlogPostForm, self).__init__(**kwargs)
        self.thumbnail.choices = get_image_choices(include_none=False)


class AddBlogPostForm(BlogPostForm):
    submit = SubmitField(label=R.string.add)


class EditBlogPostForm(BlogPostForm):
    submit = SubmitField(label=R.string.edit)

    def set_values(self, blog_post):
        self.active.data = blog_post.active
        self.date.data = blog_post.date
        self.title.data = blog_post.title
        self.thumbnail.data = blog_post.thumbnail
        self.summary.data = blog_post.summary
        self.content.data = blog_post.content