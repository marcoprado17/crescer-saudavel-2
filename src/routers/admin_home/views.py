# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template
from routers.admin_home import admin_home_blueprint
from routers.admin_home.data_providers.home import admin_home_data_provider


@admin_home_blueprint.route("/")
def home():
    return render_template("admin_home/home.html", data=admin_home_data_provider.get_data())
