# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 25/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import Blueprint

simple_content_page_blueprint = Blueprint("simple_content_page", __name__, static_folder="static", template_folder="templates")

import controller
