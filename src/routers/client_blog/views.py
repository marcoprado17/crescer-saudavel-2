# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template
from routers.client_blog import client_blog_blueprint
from routers.client_blog.data_providers.blog import blog_data_provider


@client_blog_blueprint.route("/")
def blog():
    return render_template("client_blog/blog.html", data=blog_data_provider.get_data())


@client_blog_blueprint.route("/post/<int:blog_post_id>")
def blog_post(blog_post_id):
    return "Blog post #" + str(blog_post_id)
