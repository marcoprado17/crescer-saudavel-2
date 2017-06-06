# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_login import current_user
from flask_login import login_required
from flask_bombril.url_args import get_boolean_url_arg
from r import R
from routes.client_account import client_account_blueprint
from routes.client_account.data_providers.my_account import client_my_account_data_provider
from routes.client_account.forms import UserForm


@client_account_blueprint.route("/", methods=["GET", "POST"])
@login_required
def my_account():
    if request.method == "GET":
        edit=get_boolean_url_arg(R.string.edit_arg_name, default=False)
        return render_template("client_account/my_account.html", data=client_my_account_data_provider.get_data_when_get(edit=edit))
    else:
        user_form = UserForm(edit=True)
        if not user_form.validate_on_submit():
            return render_template("client_account/my_account.html",
                                   data=client_my_account_data_provider.get_data_when_post(edit=True, user_form=user_form))
        else:
            current_user.update_from_form(form=user_form)
            return redirect(url_for("client_account.my_account"))
