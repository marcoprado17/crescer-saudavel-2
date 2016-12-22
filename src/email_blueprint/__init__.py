# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from flask import Blueprint

from email_manager import EmailManager


email_blueprint = Blueprint("email", __name__, static_folder="static", template_folder="templates")
email_manager = EmailManager()
