# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import Blueprint

flask_bombril_macros_blueprint = Blueprint("flask_bombril_macros", __name__, static_folder="static", template_folder="templates")
