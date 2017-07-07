# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template

from models.content.home_content import HomeContent
from routes.home import home_blueprint


@home_blueprint.route("/")
def home():
    return render_template(
        "home/home.html",
        content=HomeContent.get()
    )
