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
from routers.admin_blog.data_providers.posts import admin_posts_data_provider
from routers.admin_blog.forms import AddBlogPostForm
from flask_bombril.r import R as bombril_R
from wrappers.base.decorators import valid_form
from wrappers.base.forms import SubmitForm


@admin_blog_blueprint.route("/posts")
def posts():
    return render_template("admin_blog/posts.html", data=admin_posts_data_provider.get_data())


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


@admin_blog_blueprint.route("/editar-post/<int:blog_post_id>", methods=["GET", "POST"])
def edit_post(blog_post_id):
    return "", 200
    # product = Product.get(product_id=product_id)
    # if not product:
    #     return "", 404
    #
    # if request.method == "GET":
    #     return render_template("admin_products/edit_product.html",
    #                            data=admin_edit_product_data_provider.get_data_when_get(
    #                                product=product))
    # else:
    #     edit_product_form = EditProductForm()
    #
    #     if edit_product_form.validate_on_submit():
    #         product.update_from_form(product=product,
    #                                  product_form=edit_product_form)
    #         flash(R.string.product_successful_edited(product.title),
    #               bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.success))
    #         return redirect(url_for("admin_products.index"))
    #     else:
    #         return render_template("admin_products/edit_product.html",
    #                                data=admin_edit_product_data_provider.get_data_when_post(
    #                                    edit_product_form=edit_product_form))



@admin_blog_blueprint.route("/desabilitar-post/<int:blog_post_id>", methods=["POST"])
@valid_form(FormClass=SubmitForm)
def disable_post(blog_post_id):
    BlogPost.update(blog_post_id=blog_post_id, active=False)
    return "", 200

@admin_blog_blueprint.route("/ativar-post/<int:blog_post_id>", methods=["POST"])
@valid_form(FormClass=SubmitForm)
def to_activate_post(blog_post_id):
    BlogPost.update(blog_post_id=blog_post_id, active=True)
    return "", 200
