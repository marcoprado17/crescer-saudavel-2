# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.client_blog import client_blog_blueprint


@client_blog_blueprint.route("/")
def blog():
    return "Blog."


@client_blog_blueprint.route("/post/<int:blog_post_id>")
def blog_post(blog_post_id):
    return "Blog post #" + str(blog_post_id)
