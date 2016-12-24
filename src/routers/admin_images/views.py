# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 24/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.admin_images import admin_images_blueprint


@admin_images_blueprint.route("/")
def index():
    return "Imagens."


@admin_images_blueprint.route("/adicionar-imagem")
def add_image():
    return "Adicionar nova imagem."
