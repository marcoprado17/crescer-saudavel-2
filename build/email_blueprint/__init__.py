# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import Blueprint

from email_manager import EmailManager


email_blueprint = Blueprint("email", __name__, static_folder="static", template_folder="templates")
email_manager = EmailManager()
