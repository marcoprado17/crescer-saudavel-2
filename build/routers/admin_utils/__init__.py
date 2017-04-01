# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 05/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import Blueprint

admin_utils_blueprint = Blueprint("admin_utils", __name__, static_folder="static", template_folder="templates")

import views
