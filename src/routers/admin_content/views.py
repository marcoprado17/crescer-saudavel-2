# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 24/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template

from routers.admin_content import admin_content_blueprint
from routers.admin_content.data_providers.home import admin_content_home_data_provider


@admin_content_blueprint.route("/home")
def home():
    return render_template("admin_content/home.html", data=admin_content_home_data_provider.get_data())


@admin_content_blueprint.route("/contato")
def contact():
    return "Contato."


@admin_content_blueprint.route("/sobre-nos")
def about_us():
    return "Sobre-nós."


@admin_content_blueprint.route("/faq")
def faq():
    return "FAQ."
