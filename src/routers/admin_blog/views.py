# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 24/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template
from flask import request

from routers.admin_blog import admin_blog_blueprint
from routers.admin_blog.data_providers.add_post import admin_add_blog_post_data_provider


@admin_blog_blueprint.route("/posts")
def posts():
    return "Blog posts."


@admin_blog_blueprint.route("/adicionar-post", methods=["GET", "POST"])
def add_post():
    if request.method == "GET":
        return render_template("admin_blog/add_post.html", data=admin_add_blog_post_data_provider.get_data())
    else:
        return "", 200
        # add_product_form = AddProductForm()
        #
        # if add_product_form.validate_on_submit():
        #     Product.create_from_form(product_form=add_product_form)
        #     flash(R.string.product_sent_successfully(add_product_form.title.data),
        #           bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.success))
        #     return redirect(url_for("admin_products.add_product"))
        # else:
        #     return render_template("admin_products/add_product.html",
        #                            data=admin_add_product_data_provider.get_data(add_product_form=add_product_form))
