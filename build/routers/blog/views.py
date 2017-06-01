# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template
from sqlalchemy import desc

from models.blog.blog_post import BlogPost
from models.blog.blog_tag import BlogTag
from proj_decorators import safe_id_to_model_elem
from routers.blog import blog_blueprint
from routers.blog.data_providers.blog_post import client_blog_post_data_provider


@blog_blueprint.route("/")
def blog():
    recent_blog_posts = BlogPost.query.order_by(desc(BlogPost.date)).filter_by(active=True).limit(2).all()
    previous_posts = BlogPost.query.order_by(desc(BlogPost.date)).filter_by(active=True).offset(2).all()
    blog_tags = BlogTag.query.filter_by(active=True).all()
    return render_template(
        "blog/blog.html",
        recent_blog_posts=recent_blog_posts,
        previous_posts=previous_posts,
        blog_tags=blog_tags
    )


# noinspection PyUnresolvedReferences
@blog_blueprint.route("/post/<int:blog_post_id>")
@safe_id_to_model_elem(model=BlogPost)
def blog_post(blog_post):
    return render_template("blog/blog_post.html", data=client_blog_post_data_provider.get_data(blog_post=blog_post))
