# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 24/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template

from routers.admin_images import admin_images_blueprint
from routers.admin_images.data_providers import admin_images_data_provider, admin_add_image_data_provider


@admin_images_blueprint.route("/")
def index():
    return render_template("admin_images/index.html", data=admin_images_data_provider.get_data())


@admin_images_blueprint.route("/adicionar-imagem")
def add_image():
    return render_template("admin_images/add_image.html", data=admin_add_image_data_provider.get_data())
