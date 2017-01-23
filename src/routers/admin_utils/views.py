# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 05/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import json
from flask import request

from routers.admin_utils import admin_utils_blueprint
from proj_utils import parse_markdown


@admin_utils_blueprint.route("/traduzir-markdown", methods=["POST"])
def markdown_parse():
    markdown_text = request.get_json()["markdown_text"]
    return json.dumps(dict(markdown_html=parse_markdown(markdown_text)))
