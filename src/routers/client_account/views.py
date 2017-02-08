# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template
from flask import request
from flask_login import login_required
from flask_bombril.url_args import get_boolean_url_arg
from r import R
from routers.client_account import client_account_blueprint
from routers.client_account.data_providers.my_account import client_my_account_data_provider


@client_account_blueprint.route("/", methods=["GET", "POST"])
@login_required
def my_account():
    if request.method == "GET":
        edit=get_boolean_url_arg(R.string.edit_arg_name, default=False)
        return render_template("client_account/my_account.html", data=client_my_account_data_provider.get_data_when_get(edit=edit))
    else:
        return ""
