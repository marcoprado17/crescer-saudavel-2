# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.client_blog import client_blog_blueprint


@client_blog_blueprint.route("/")
def blog():
    return "Blog."


@client_blog_blueprint.route("/post")
def blog_post():
    return "Post do blog."
