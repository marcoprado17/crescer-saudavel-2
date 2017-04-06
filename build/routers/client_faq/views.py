# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 25/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template
from routers.client_faq import client_faq_blueprint
from routers.client_faq.data_providers.faq import client_faq_data_provider


@client_faq_blueprint.route("/")
def faq():
    return render_template("client_faq/faq.html", data=client_faq_data_provider.get_data())
