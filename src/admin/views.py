# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 05/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import json
from flask import request
from flask_login import login_required
from proj_decorators import admin_required
from admin import admin_proj_blueprint
from proj_utils import parse_markdown


@admin_proj_blueprint.route("/traduzir-markdown", methods=["POST"])
@login_required
@admin_required
def markdown_parse():
    markdown_text = request.get_json()["markdown_text"]
    return json.dumps(dict(markdown_html=parse_markdown(markdown_text)))
