# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.admin_products import admin_products_blueprint


@admin_products_blueprint.route("/")
def index():
    return "Produtos."


@admin_products_blueprint.route("/adicionar-produto")
def add_product():
    return "Adicionar novo produto."


@admin_products_blueprint.route("/categorias-de-produto")
def categories():
    return "Categorias de produto."


@admin_products_blueprint.route("/adicionar-categoria-de-produto")
def add_category():
    return "Adicionar nova categoria de produto."


@admin_products_blueprint.route("/subcategorias-de-produto")
def subcategories():
    return "Subcategorias de produto."


@admin_products_blueprint.route("/adicionar-subcategoria-de-produto")
def add_subcategory():
    return "Adicionar nova subcategoria de produto."
