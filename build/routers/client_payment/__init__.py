# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import Blueprint

client_payment_blueprint = Blueprint("client_payment", __name__, static_folder="static", template_folder="templates")

import views
