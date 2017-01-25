# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 25/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import Blueprint

client_base_blueprint = Blueprint("client_base", __name__, static_folder="static", template_folder="templates")
