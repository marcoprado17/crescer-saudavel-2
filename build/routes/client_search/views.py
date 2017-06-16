# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 20/02/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template
from flask_bombril.utils import get_url_arg
from r import R
from routes.client_search import client_search_blueprint
from routes.client_search.data_providers.search import client_search_data_provider


@client_search_blueprint.route("/")
def search():
    q = get_url_arg(arg_name=R.string.search_query_arg_name, default="")
    return render_template("client_search/search.html", data=client_search_data_provider.get_data(q=q))
