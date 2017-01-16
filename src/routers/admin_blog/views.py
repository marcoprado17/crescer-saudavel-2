# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 24/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from models.blog_post import BlogPost
from r import R
from routers.admin_blog import admin_blog_blueprint
from routers.admin_blog.data_providers.add_post import admin_add_blog_post_data_provider
from routers.admin_blog.forms import AddBlogPostForm
from flask_bombril.r import R as bombril_R


@admin_blog_blueprint.route("/posts")
def posts():
    return "Blog posts."


@admin_blog_blueprint.route("/adicionar-post", methods=["GET", "POST"])
def add_post():
    if request.method == "GET":
        return render_template("admin_blog/add_post.html", data=admin_add_blog_post_data_provider.get_data())
    else:
        add_blog_post_form = AddBlogPostForm()

        if add_blog_post_form.validate_on_submit():
            BlogPost.create_from_form(add_blog_post_form)
            flash(R.string.blog_post_sent_successfully(add_blog_post_form.title.data),
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.success))
            return redirect(url_for("admin_blog.add_post"))
        else:
            return render_template("admin_blog/add_post.html",
                                   data=admin_add_blog_post_data_provider.get_data(add_blog_post_form=add_blog_post_form))
