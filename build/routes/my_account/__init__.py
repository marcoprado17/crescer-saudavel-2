# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import Blueprint

my_account_blueprint = Blueprint("my_account", __name__, static_folder="static", template_folder="templates")

import controller
