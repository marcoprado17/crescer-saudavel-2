# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template
from sqlalchemy import desc
from flask_bombril.utils.utils import get_int_request_arg
from models.blog.blog_post import BlogPost
from models.blog.blog_tag import BlogTag
from proj_decorators import safe_id_to_model_elem
from r import R
from routers.blog import blog_blueprint
from routers.blog.data_providers.blog_post import client_blog_post_data_provider


@blog_blueprint.route("/")
def blog():
    page = get_int_request_arg(R.string.page_arg_name, 1)
    tag_id = get_int_request_arg(R.string.tag_id_arg_name, 0)

    recent_blog_posts = BlogPost.query.order_by(desc(BlogPost.date), BlogPost.id).filter_by(active=True).limit(2).all()

    previous_posts_query = BlogPost.query.order_by(desc(BlogPost.date)).filter_by(active=True)
    if len(recent_blog_posts) > 0:
        previous_posts_query = previous_posts_query.filter(BlogPost.id != recent_blog_posts[0].id)
    if len(recent_blog_posts) > 1:
        previous_posts_query = previous_posts_query.filter(BlogPost.id != recent_blog_posts[1].id)

    if tag_id != 0:
        previous_posts_query = previous_posts_query.filter(BlogPost.tags.any(BlogTag.id == tag_id))

    previous_posts_pagination = previous_posts_query.paginate(page=page, per_page=R.dimen.n_blog_posts_per_page)

    blog_tags = BlogTag.query.filter_by(active=True).all()

    return render_template(
        "blog/blog.html",
        recent_blog_posts=recent_blog_posts,
        previous_posts_pagination=previous_posts_pagination,
        blog_tags=blog_tags,
        current_tag_id=tag_id
    )


# noinspection PyUnresolvedReferences
@blog_blueprint.route("/post/<int:blog_post_id>")
@safe_id_to_model_elem(model=BlogPost)
def blog_post(blog_post):
    return render_template("blog/blog_post.html", data=client_blog_post_data_provider.get_data(blog_post=blog_post))
