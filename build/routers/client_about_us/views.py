# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 25/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template
from routers.client_about_us import client_about_us_blueprint
from routers.client_about_us.data_providers.about_us import client_about_us_data_provider


@client_about_us_blueprint.route("/")
def about_us():
    return render_template("client_about_us/about_us.html", data=client_about_us_data_provider.get_data())
