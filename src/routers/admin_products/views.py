# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import random
import json

from models.product import Product
from models.product_category import ProductCategory
from models.product_subcategory import ProductSubcategory
from r import R
from routers.admin_products import admin_products_blueprint
from flask import render_template, request, flash, redirect, url_for
from data_providers import admin_add_product_category_data_provider, admin_product_categories_data_provider
from routers.admin_products.data_providers.add_product import admin_add_product_data_provider
from routers.admin_products.data_providers.add_subcategory import admin_add_product_subcategory_data_provider
from routers.admin_products.data_providers.edit_category import admin_edit_product_category_data_provider
from routers.admin_products.data_providers.edit_product import admin_edit_product_data_provider
from routers.admin_products.data_providers.edit_subcategory import admin_edit_product_subcategory_data_provider
from routers.admin_products.data_providers.index import admin_products_data_provider
from routers.admin_products.data_providers.subcategories import admin_product_subcategories_data_provider
from routers.admin_products.forms import AddProductCategoryForm, EditProductCategoryForm, AddProductSubcategoryForm, \
    EditProductSubcategoryForm, AddProductForm, AddToStockForm, RemoveFromStockForm, UpdateStockForm, EditProductForm
from flask_bombril.r import R as bombril_R
from wrappers.base.decorators import valid_form
from wrappers.base.forms import SubmitForm


@admin_products_blueprint.route("/")
def index():
    return render_template("admin_products/index.html", data=admin_products_data_provider.get_data())


@admin_products_blueprint.route("/adicionar-produto", methods=["GET", "POST"])
def add_product():
    if request.method == "GET":
        return render_template("admin_products/add_product.html", data=admin_add_product_data_provider.get_data())
    else:
        add_product_form = AddProductForm()

        if add_product_form.validate_on_submit():
            product = Product.create_from_form(product_form=add_product_form)
            flash(R.string.product_sent_successfully(product),
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.success))
            return redirect(url_for("admin_products.add_product"))
        else:
            return render_template("admin_products/add_product.html",
                                   data=admin_add_product_data_provider.get_data(add_product_form=add_product_form))


@admin_products_blueprint.route("/editar-produto/<int:product_id>", methods=["GET", "POST"])
def edit_product(product_id):
    product = Product.get(product_id=product_id)
    if not product:
        return "", 404

    if request.method == "GET":
        return render_template("admin_products/edit_product.html",
                               data=admin_edit_product_data_provider.get_data_when_get(
                                   product=product))
    else:
        if not product.editable:
            flash(R.string.product_not_editable(product.title),
                  bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.error))
            return redirect(url_for("admin_products.index"))

        edit_product_form = EditProductForm()

        if edit_product_form.validate_on_submit():
            product.update_from_form(product=product,
                                     product_form=edit_product_form)
            flash(R.string.product_successful_edited(product),
                  bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.success))
            return redirect(url_for("admin_products.index"))
        else:
            return render_template("admin_products/edit_product.html",
                                   data=admin_edit_product_data_provider.get_data_when_post(
                                       edit_product_form=edit_product_form))


@admin_products_blueprint.route("/desabilitar-produto/<int:product_id>", methods=["POST"])
@valid_form(FormClass=SubmitForm)
def disable_product(product_id):
    Product.update(product_id=product_id, active=False)
    return "", 200

@admin_products_blueprint.route("/ativar-produto/<int:product_id>", methods=["POST"])
@valid_form(FormClass=SubmitForm)
def to_activate_product(product_id):
    Product.update(product_id=product_id, active=True)
    return "", 200


@admin_products_blueprint.route("/aumentar-estoque-do-produto/<int:product_id>", methods=["POST"])
@valid_form(FormClass=AddToStockForm)
def product_stock_addition(product_id, form):
    try:
        new_stock_value=Product.add_to_stock(product_id=product_id, value=form.value.data)
        return json.dumps(dict(new_stock_value=new_stock_value)), 200
    except:
        return "", 500


@admin_products_blueprint.route("/diminuir-estoque-do-produto/<int:product_id>", methods=["POST"])
@valid_form(FormClass=RemoveFromStockForm)
def product_stock_removal(product_id, form):
    try:
        new_stock_value = Product.remove_from_stock(product_id=product_id, value=form.value.data)
        return json.dumps(dict(new_stock_value=new_stock_value)), 200
    except:
        return "", 500


@admin_products_blueprint.route("/atualizar-estoque-do-produto/<int:product_id>", methods=["POST"])
@valid_form(FormClass=UpdateStockForm)
def product_stock_update(product_id, form):
    try:
        new_stock_value = Product.update_stock(product_id=product_id, value=form.value.data)
        return json.dumps(dict(new_stock_value=new_stock_value)), 200
    except:
        return "", 500


@admin_products_blueprint.route("/categorias-de-produto")
def categories():
    return render_template("admin_products/categories.html", data=admin_product_categories_data_provider.get_data())


@admin_products_blueprint.route("/adicionar-categoria-de-produto", methods=["GET", "POST"])
def add_category():
    if request.method == "GET":
        return render_template("admin_products/add_category.html",
                               data=admin_add_product_category_data_provider.get_data())
    else:
        add_product_category_form = AddProductCategoryForm()

        if add_product_category_form.validate_on_submit():
            product_category = ProductCategory.create_from_form(add_product_category_form=add_product_category_form)
            flash(R.string.product_category_sent_successfully(product_category),
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.success))
            return redirect(url_for("admin_products.add_category"))
        else:
            return render_template("admin_products/add_category.html",
                                   data=admin_add_product_category_data_provider.get_data(
                                       add_product_category_form=add_product_category_form))


@admin_products_blueprint.route("/editar-categoria-de-produto/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    product_category = ProductCategory.get(category_id=category_id)
    if not product_category:
        return "", 404

    if request.method == "GET":
        return render_template("admin_products/edit_category.html",
                               data=admin_edit_product_category_data_provider.get_data_when_get(
                                   product_category=product_category))
    else:
        if not product_category.editable:
            flash(R.string.product_category_not_editable(product_category),
                  bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.error))
            return redirect(url_for("admin_products.categories"))

        edit_product_category_form = EditProductCategoryForm()

        if edit_product_category_form.validate_on_submit():
            ProductCategory.update_from_form(product_category=product_category,
                                             edit_product_category_form=edit_product_category_form)
            flash(R.string.product_category_successful_edited(product_category),
                  bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.success))
            return redirect(url_for("admin_products.categories"))
        else:
            return render_template("admin_products/edit_category.html",
                                   data=admin_edit_product_category_data_provider.get_data_when_post(
                                       edit_product_category_form=edit_product_category_form))


@admin_products_blueprint.route("/desabilitar-categoria-de-produto/<int:category_id>", methods=["POST"])
@valid_form(FormClass=SubmitForm)
def disable_category(category_id):
    ProductCategory.update(product_category_id=category_id, active=False)
    return "", 200


@admin_products_blueprint.route("/ativar-categoria-de-produto/<int:category_id>", methods=["POST"])
@valid_form(FormClass=SubmitForm)
def to_activate_category(category_id):
    ProductCategory.update(product_category_id=category_id, active=True)
    return "", 200


@admin_products_blueprint.route("/subcategorias-de-produto")
def subcategories():
    return render_template("admin_products/subcategories.html",
                           data=admin_product_subcategories_data_provider.get_data())


@admin_products_blueprint.route("/adicionar-subcategoria-de-produto", methods=["GET", "POST"])
def add_subcategory():
    if request.method == "GET":
        return render_template("admin_products/add_subcategory.html",
                               data=admin_add_product_subcategory_data_provider.get_data())

    else:
        add_product_subcategory_form = AddProductSubcategoryForm()

        if add_product_subcategory_form.validate_on_submit():
            product_subcategory = ProductSubcategory.create_from_form(add_product_subcategory_form=add_product_subcategory_form)
            flash(R.string.product_subcategory_sent_successfully(product_subcategory),
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.success))
            return redirect(url_for("admin_products.add_subcategory"))

        return render_template("admin_products/add_subcategory.html",
                               data=admin_add_product_subcategory_data_provider.get_data(
                                   add_product_subcategory_form=add_product_subcategory_form))


@admin_products_blueprint.route("/editar-subcategoria-de-produto/<int:subcategory_id>", methods=["GET", "POST"])
def edit_subcategory(subcategory_id):
    product_subcategory = ProductSubcategory.get(subcategory_id=subcategory_id)
    if not product_subcategory:
        return "", 404

    if request.method == "GET":
        return render_template("admin_products/edit_subcategory.html",
                               data=admin_edit_product_subcategory_data_provider.get_data_when_get(
                                   product_subcategory=product_subcategory))
    else:
        edit_product_subcategory_form = EditProductSubcategoryForm()

        if edit_product_subcategory_form.validate_on_submit():
            ProductSubcategory.update_from_form(product_subcategory=product_subcategory,
                                                edit_product_subcategory_form=edit_product_subcategory_form)
            flash(R.string.product_subcategory_successful_edited(product_subcategory),
                  bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.success))
            return redirect(url_for("admin_products.subcategories"))
        else:
            return render_template("admin_products/edit_subcategory.html",
                                   data=admin_edit_product_subcategory_data_provider.get_data_when_post(
                                       edit_product_subcategory_form=edit_product_subcategory_form))


@admin_products_blueprint.route("/desabilitar-subcategoria-de-produto/<int:subcategory_id>", methods=["POST"])
@valid_form(FormClass=SubmitForm)
def disable_subcategory(subcategory_id):
    ProductSubcategory.set_active_value(subcategory_id=subcategory_id, active=False)
    return "", 200


@admin_products_blueprint.route("/ativar-subcategoria-de-produto/<int:subcategory_id>", methods=["POST"])
@valid_form(FormClass=SubmitForm)
def to_activate_subcategory(subcategory_id):
    ProductSubcategory.set_active_value(subcategory_id=subcategory_id, active=True)
    return "", 200
