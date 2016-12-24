# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 24/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.admin_blog import admin_blog_blueprint


@admin_blog_blueprint.route("/posts")
def posts():
    return "Blog posts."


@admin_blog_blueprint.route("/adicionar-post")
def add_post():
    return "Adicionar blog post."
