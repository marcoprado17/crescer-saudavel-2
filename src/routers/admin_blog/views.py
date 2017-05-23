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
from flask_login import login_required

from flask_bombril.r import R as bombril_R
from models.blog.blog_post import BlogPost
from proj_decorators import valid_form, safe_id_to_model_elem, admin_required
from proj_forms import SubmitForm
from r import R
from routers.admin_blog import admin_blog_blueprint
from routers.admin_blog.data_providers.add_post import admin_add_blog_post_data_provider
from routers.admin_blog.data_providers.edit_post import admin_edit_post_data_provider
from routers.admin_blog.data_providers.posts import admin_posts_data_provider
from routers.admin_blog.forms import AddBlogPostForm, EditBlogPostForm
from routers.client_blog.data_providers.blog_post import client_blog_post_data_provider


@admin_blog_blueprint.route("/posts")
@login_required
@admin_required
def posts():
    return render_template("admin_blog/posts.html", data=admin_posts_data_provider.get_data())


@admin_blog_blueprint.route("/adicionar-post", methods=["GET", "POST"])
@login_required
@admin_required
def add_post():
    if request.method == "GET":
        return render_template("admin_blog/add_post.html", data=admin_add_blog_post_data_provider.get_data_when_get())
    else:
        add_blog_post_form = AddBlogPostForm()
        if add_blog_post_form.validate_on_submit():
            blog_post = BlogPost.create_from_form(form=add_blog_post_form)
            flash(R.string.blog_post_sent_successfully(blog_post),
                  bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.success))
            flash(R.string.blog_post_sent_successfully(blog_post),
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.success))
            return redirect(url_for("admin_blog.add_post"))
        else:
            flash(R.string.add_edit_form_error,
                  bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.error))
            return render_template("admin_blog/add_post.html",
                                   data=admin_add_blog_post_data_provider.get_data_when_post(add_blog_post_form=add_blog_post_form))


# noinspection PyUnresolvedReferences
@admin_blog_blueprint.route("/editar-post/<int:blog_post_id>", methods=["GET", "POST"])
@login_required
@admin_required
@safe_id_to_model_elem(model=BlogPost)
def edit_post(blog_post):
    if request.method == "GET":
        return render_template("admin_blog/edit_post.html",
                               data=admin_edit_post_data_provider.get_data_when_get(
                                   blog_post=blog_post))
    else:
        edit_post_form = EditBlogPostForm()
        if edit_post_form.validate_on_submit():
            blog_post.update_from_form(form=edit_post_form)
            flash(R.string.post_successful_edited(blog_post),
                  bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.success))
            return redirect(url_for("admin_blog.posts"))
        else:
            flash(R.string.add_edit_form_error,
                  bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.error))
            return render_template("admin_blog/edit_post.html",
                                   data=admin_edit_post_data_provider.get_data_when_post(
                                       edit_post_form=edit_post_form))


# noinspection PyUnresolvedReferences
@admin_blog_blueprint.route("/pre-visualizacao-de-post/<int:blog_post_id>")
@login_required
@admin_required
@safe_id_to_model_elem(model=BlogPost)
def post_preview(blog_post):
    return render_template("client_blog/blog_post.html",
                           data=client_blog_post_data_provider.get_data(blog_post=blog_post))


# noinspection PyUnresolvedReferences
@admin_blog_blueprint.route("/desabilitar-post/<int:blog_post_id>", methods=["POST"])
@login_required
@admin_required
@valid_form(FormClass=SubmitForm)
@safe_id_to_model_elem(model=BlogPost)
def disable_post(blog_post, form):
    blog_post.disable()
    return "", 200


# noinspection PyUnresolvedReferences
@admin_blog_blueprint.route("/ativar-post/<int:blog_post_id>", methods=["POST"])
@login_required
@admin_required
@valid_form(FormClass=SubmitForm)
@safe_id_to_model_elem(model=BlogPost)
def to_activate_post(blog_post, form):
    blog_post.to_activate()
    return "", 200
