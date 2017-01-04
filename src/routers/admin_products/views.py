# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.product_category import ProductCategory
from r import R
from routers.admin_products import admin_products_blueprint
from flask import render_template, request, flash, redirect, url_for
from data_providers import add_product_category_data_provider
from routers.admin_products.forms import AddProductCategoryForm
from flask_bombril.r import R as bombril_R


@admin_products_blueprint.route("/")
def index():
    return "Produtos."


@admin_products_blueprint.route("/adicionar-produto")
def add_product():
    return "Adicionar novo produto."


@admin_products_blueprint.route("/categorias-de-produto")
def categories():
    return "Categorias de produto."


@admin_products_blueprint.route("/adicionar-categoria-de-produto", methods=["GET", "POST"])
def add_category():
    if request.method == "GET":
        return render_template("admin_products/add_category.html", data=add_product_category_data_provider.get_data())
    else:
        add_product_category_form = AddProductCategoryForm()

        if add_product_category_form.validate_on_submit():
            ProductCategory.add_from_form(add_product_category_form=add_product_category_form)
            flash(R.string.product_category_sent_successfully(add_product_category_form.category_name.data), bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.success))
            return redirect(url_for("admin_products.add_category"))
        else:
            return render_template("admin_products/add_category.html", data=add_product_category_data_provider.get_data(
                add_product_category_form=add_product_category_form))


@admin_products_blueprint.route("/subcategorias-de-produto")
def subcategories():
    return "Subcategorias de produto."


@admin_products_blueprint.route("/adicionar-subcategoria-de-produto")
def add_subcategory():
    return "Adicionar nova subcategoria de produto."
