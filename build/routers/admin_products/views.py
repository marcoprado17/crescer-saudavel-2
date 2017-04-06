# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import json

from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required
from data_providers import admin_add_product_category_data_provider, admin_product_categories_data_provider
from proj_decorators import valid_form, safe_id_to_model_elem, admin_required
from flask_bombril.r import R as bombril_R
from proj_forms import SubmitForm
from models.product import Product
from models.product_category import ProductCategory
from models.product_subcategory import ProductSubcategory
from r import R
from routers.admin_products import admin_products_blueprint
from routers.admin_products.data_providers.add_product import admin_add_product_data_provider
from routers.admin_products.data_providers.add_subcategory import admin_add_product_subcategory_data_provider
from routers.admin_products.data_providers.edit_category import admin_edit_product_category_data_provider
from routers.admin_products.data_providers.edit_product import admin_edit_product_data_provider
from routers.admin_products.data_providers.edit_subcategory import admin_edit_product_subcategory_data_provider
from routers.admin_products.data_providers.products import admin_products_data_provider
from routers.admin_products.data_providers.subcategories import admin_product_subcategories_data_provider
from routers.admin_products.forms import AddProductCategoryForm, EditProductCategoryForm, AddProductSubcategoryForm, \
    EditProductSubcategoryForm, AddProductForm, AddToStockForm, RemoveFromStockForm, UpdateStockForm, EditProductForm
from routers.client_products.data_providers.product import client_product_data_provider
from decimal import Decimal


@admin_products_blueprint.route("/")
@login_required
@admin_required
def products():
    return render_template("admin_products/products.html", data=admin_products_data_provider.get_data())


@admin_products_blueprint.route("/adicionar-produto", methods=["GET", "POST"])
@login_required
@admin_required
def add_product():
    if request.method == "GET":
        return render_template("admin_products/add_product.html", data=admin_add_product_data_provider.get_data_when_get())
    else:
        add_product_form = AddProductForm()
        if add_product_form.validate_on_submit():
            product = Product.create_from_form(form=add_product_form)
            flash(R.string.product_sent_successfully(product),
                  bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.success))
            flash(R.string.product_sent_successfully(product),
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.success))
            return redirect(url_for("admin_products.add_product"))
        else:
            print "###"
            print "erro"
            print add_product_form.errors
            print add_product_form.discount_percentage.data
            flash(R.string.add_edit_form_error,
                  bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.error))
            return render_template("admin_products/add_product.html",
                                   data=admin_add_product_data_provider.get_data_when_post(add_product_form=add_product_form))


# noinspection PyUnresolvedReferences
@admin_products_blueprint.route("/editar-produto/<int:product_id>", methods=["GET", "POST"])
@login_required
@admin_required
@safe_id_to_model_elem(model=Product)
def edit_product(product):
    if request.method == "GET":
        return render_template("admin_products/edit_product.html",
                               data=admin_edit_product_data_provider.get_data_when_get(
                                   product=product))
    else:
        edit_product_form = EditProductForm()
        if edit_product_form.validate_on_submit():
            product.update_from_form(form=edit_product_form)
            flash(R.string.product_successful_edited(product),
                  bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.success))
            return redirect(url_for("admin_products.products"))
        else:
            flash(R.string.add_edit_form_error,
                  bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.error))
            return render_template("admin_products/edit_product.html",
                                   data=admin_edit_product_data_provider.get_data_when_post(
                                       edit_product_form=edit_product_form))


# noinspection PyUnresolvedReferences
@admin_products_blueprint.route("/pre-visualizacao-de-produto/<int:product_id>")
@login_required
@admin_required
@safe_id_to_model_elem(model=Product)
def product_preview(product):
    return render_template("client_products/product.html", data=client_product_data_provider.get_data(product))


# noinspection PyUnresolvedReferences
@admin_products_blueprint.route("/desabilitar-produto/<int:product_id>", methods=["POST"])
@login_required
@admin_required
@valid_form(FormClass=SubmitForm)
@safe_id_to_model_elem(model=Product)
def disable_product(product, form):
    product.disable()
    return "", 200


# noinspection PyUnresolvedReferences
@admin_products_blueprint.route("/ativar-produto/<int:product_id>", methods=["POST"])
@login_required
@admin_required
@valid_form(FormClass=SubmitForm)
@safe_id_to_model_elem(model=Product)
def to_activate_product(product, form):
    product.to_activate()
    return "", 200


# noinspection PyUnresolvedReferences
@admin_products_blueprint.route("/aumentar-estoque-do-produto/<int:product_id>", methods=["POST"])
@login_required
@admin_required
@valid_form(FormClass=AddToStockForm)
@safe_id_to_model_elem(model=Product)
def product_stock_addition(product, form):
    product.add_to_stock(form.value.data)
    return json.dumps(dict(stock=product.stock, available=product.available)), 200


# noinspection PyUnresolvedReferences
@admin_products_blueprint.route("/diminuir-estoque-do-produto/<int:product_id>", methods=["POST"])
@login_required
@admin_required
@valid_form(FormClass=RemoveFromStockForm)
@safe_id_to_model_elem(model=Product)
def product_stock_removal(product, form):
    product.remove_from_stock(form.value.data)
    return json.dumps(dict(stock=product.stock, available=product.available)), 200


# noinspection PyUnresolvedReferences
@admin_products_blueprint.route("/atualizar-estoque-do-produto/<int:product_id>", methods=["POST"])
@login_required
@admin_required
@valid_form(FormClass=UpdateStockForm)
@safe_id_to_model_elem(model=Product)
def product_stock_update(product, form):
    product.update_stock(form.value.data)
    return json.dumps(dict(stock=product.stock, available=product.available)), 200


@admin_products_blueprint.route("/categorias-de-produto")
@login_required
@admin_required
def categories():
    return render_template("admin_products/categories.html", data=admin_product_categories_data_provider.get_data())


@admin_products_blueprint.route("/adicionar-categoria-de-produto", methods=["GET", "POST"])
@login_required
@admin_required
def add_category():
    if request.method == "GET":
        return render_template("admin_products/add_category.html",
                               data=admin_add_product_category_data_provider.get_data_when_get())
    else:
        add_product_category_form = AddProductCategoryForm()
        if add_product_category_form.validate_on_submit():
            product_category = ProductCategory.create_from_form(form=add_product_category_form)
            flash(R.string.product_category_sent_successfully(product_category),
                  bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.success))
            flash(R.string.product_category_sent_successfully(product_category),
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.success))
            return redirect(url_for("admin_products.add_category"))
        else:
            flash(R.string.add_edit_form_error,
                  bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.error))
            return render_template("admin_products/add_category.html",
                                   data=admin_add_product_category_data_provider.get_data_when_post(
                                       add_product_category_form=add_product_category_form))


# noinspection PyUnresolvedReferences
@admin_products_blueprint.route("/editar-categoria-de-produto/<int:product_category_id>", methods=["GET", "POST"])
@login_required
@admin_required
@safe_id_to_model_elem(model=ProductCategory)
def edit_category(product_category):
    if request.method == "GET":
        return render_template("admin_products/edit_category.html",
                               data=admin_edit_product_category_data_provider.get_data_when_get(
                                   product_category=product_category))
    else:
        edit_product_category_form = EditProductCategoryForm()
        if edit_product_category_form.validate_on_submit():
            product_category.update_from_form(form=edit_product_category_form)
            flash(R.string.product_category_successful_edited(product_category),
                  bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.success))
            return redirect(url_for("admin_products.categories"))
        else:
            flash(R.string.add_edit_form_error,
                  bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.error))
            return render_template("admin_products/edit_category.html",
                                   data=admin_edit_product_category_data_provider.get_data_when_post(
                                       edit_product_category_form=edit_product_category_form))


# noinspection PyUnresolvedReferences
@admin_products_blueprint.route("/desabilitar-categoria-de-produto/<int:product_category_id>", methods=["POST"])
@login_required
@admin_required
@valid_form(FormClass=SubmitForm)
@safe_id_to_model_elem(model=ProductCategory)
def disable_category(product_category, form):
    product_category.disable()
    return "", 200


# noinspection PyUnresolvedReferences
@admin_products_blueprint.route("/ativar-categoria-de-produto/<int:product_category_id>", methods=["POST"])
@login_required
@admin_required
@valid_form(FormClass=SubmitForm)
@safe_id_to_model_elem(model=ProductCategory)
def to_activate_category(product_category, form):
    product_category.to_activate()
    return "", 200


@admin_products_blueprint.route("/subcategorias-de-produto")
@login_required
@admin_required
def subcategories():
    return render_template("admin_products/subcategories.html",
                           data=admin_product_subcategories_data_provider.get_data())


@admin_products_blueprint.route("/adicionar-subcategoria-de-produto", methods=["GET", "POST"])
@login_required
@admin_required
def add_subcategory():
    if request.method == "GET":
        return render_template("admin_products/add_subcategory.html",
                               data=admin_add_product_subcategory_data_provider.get_data())
    else:
        add_product_subcategory_form = AddProductSubcategoryForm()
        if add_product_subcategory_form.validate_on_submit():
            product_subcategory = ProductSubcategory.create_from_form(form=add_product_subcategory_form)
            flash(R.string.product_subcategory_sent_successfully(product_subcategory),
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.success))
            flash(R.string.product_subcategory_sent_successfully(product_subcategory),
                  bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.success))
            return redirect(url_for("admin_products.add_subcategory"))
        flash(R.string.add_edit_form_error,
              bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.error))
        return render_template("admin_products/add_subcategory.html",
                               data=admin_add_product_subcategory_data_provider.get_data(
                                   add_product_subcategory_form=add_product_subcategory_form))


# noinspection PyUnresolvedReferences
@admin_products_blueprint.route("/editar-subcategoria-de-produto/<int:product_subcategory_id>", methods=["GET", "POST"])
@login_required
@admin_required
@safe_id_to_model_elem(model=ProductSubcategory)
def edit_subcategory(product_subcategory):
    if request.method == "GET":
        return render_template("admin_products/edit_subcategory.html",
                               data=admin_edit_product_subcategory_data_provider.get_data_when_get(
                                   product_subcategory=product_subcategory))
    else:
        edit_product_subcategory_form = EditProductSubcategoryForm()
        if edit_product_subcategory_form.validate_on_submit():
            product_subcategory.update_from_form(form=edit_product_subcategory_form)
            flash(R.string.product_subcategory_successful_edited(product_subcategory),
                  bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.success))
            return redirect(url_for("admin_products.subcategories"))
        else:
            flash(R.string.add_edit_form_error,
                  bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.error))
            return render_template("admin_products/edit_subcategory.html",
                                   data=admin_edit_product_subcategory_data_provider.get_data_when_post(
                                       edit_product_subcategory_form=edit_product_subcategory_form))


# noinspection PyUnresolvedReferences
@admin_products_blueprint.route("/desabilitar-subcategoria-de-produto/<int:product_subcategory_id>", methods=["POST"])
@login_required
@admin_required
@valid_form(FormClass=SubmitForm)
@safe_id_to_model_elem(model=ProductSubcategory)
def disable_subcategory(product_subcategory, form):
    product_subcategory.disable()
    return "", 200


# noinspection PyUnresolvedReferences
@admin_products_blueprint.route("/ativar-subcategoria-de-produto/<int:product_subcategory_id>", methods=["POST"])
@login_required
@admin_required
@valid_form(FormClass=SubmitForm)
@safe_id_to_model_elem(model=ProductSubcategory)
def to_activate_subcategory(product_subcategory, form):
    product_subcategory.to_activate()
    return "", 200


@admin_products_blueprint.route("/calcular-preco-com-desconto", methods=["POST"])
def calculate_price_with_discount():
    try:
        price = Decimal(request.form["price"].replace(',','.'))
        discount_percentage = int(request.form["discount_percentage"])
        price_with_discount = Product.calculate_price_with_discount(price=price, discount_percentage=discount_percentage)
        return json.dumps(dict(price_with_discount=R.string.decimal_price_as_string(price_as_decimal=price_with_discount, include_rs=True))), 200
    except:
        return "", 400
