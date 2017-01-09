# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 05/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import markdown
from flask import json
from flask import request
from routers.admin_utils import admin_utils_blueprint

@admin_utils_blueprint.route("/traduzir-markdown", methods=["POST"])
def markdown_parse():
    markdown_text = request.get_json()["markdown_text"]
    markdown_html = markdown.markdown(markdown_text, extensions=['markdown.extensions.tables'])
    markdown_html = markdown_html.replace("<table>", "<table class='table'>")
    return json.dumps(dict(markdown_html=markdown_html))
