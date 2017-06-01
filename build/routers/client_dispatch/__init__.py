# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import Blueprint

client_dispatch_blueprint = Blueprint("client_dispatch", __name__, static_folder="static", template_folder="templates")

import views
