# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template

from models.blog.blog_post import BlogPost
from proj_decorators import safe_id_to_model_elem
from routers.client_blog import client_blog_blueprint
from routers.client_blog.data_providers.blog import blog_data_provider
from routers.client_blog.data_providers.blog_post import client_blog_post_data_provider


@client_blog_blueprint.route("/")
def blog():
    return render_template("client_blog/blog.html", data=blog_data_provider.get_data())


# noinspection PyUnresolvedReferences
@client_blog_blueprint.route("/post/<int:blog_post_id>")
@safe_id_to_model_elem(model=BlogPost)
def blog_post(blog_post):
    return render_template("client_blog/blog_post.html", data=client_blog_post_data_provider.get_data(blog_post=blog_post))
