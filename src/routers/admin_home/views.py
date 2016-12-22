# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template
from routers.admin_home import admin_home_blueprint


@admin_home_blueprint.route("/")
def index():
    return render_template("admin_home/index.html")
