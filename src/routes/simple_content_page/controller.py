# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 25/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template
from models.content.about_us import AboutUsContent
from r import R
from routes.simple_content_page import simple_content_page_blueprint


@simple_content_page_blueprint.route("/sobre-nos")
def about_us():
    return render_template(
        "simple_content_page/main.html",
        title=R.string.about_us,
        content_html=AboutUsContent.get().content_html
    )
