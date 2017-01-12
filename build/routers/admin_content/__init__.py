# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import Blueprint

admin_content_blueprint = Blueprint("admin_content", __name__, static_folder="static", template_folder="templates")

import views
