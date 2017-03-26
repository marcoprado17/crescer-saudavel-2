# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_login import current_user
from flask_login import login_required
from flask_bombril.url_args import get_valid_integer
from r import R
from routers.admin_clients.forms import UserForm
from routers.client_checkout import client_checkout_blueprint
from routers.client_checkout.data_providers.checkout import client_checkout_data_provider
from flask_bombril.r import R as bombril_R


@client_checkout_blueprint.route("/", methods=["GET", "POST"])
@login_required
def checkout():
    step = get_valid_integer(arg_name=R.string.step_arg_name, default=1)
    if request.method == "GET":
        return render_template("client_checkout/checkout.html", data=client_checkout_data_provider.get_data(step=step))
    else:
        if step == 1:
            user_form = UserForm(edit=True)
            if not user_form.validate_on_submit():
                flash(R.string.fix_form_errors_before_proceed,
                      bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.error))
                return render_template("client_checkout/checkout.html",
                                       data=client_checkout_data_provider.get_data_when_post(step=1, user_form=user_form))
            else:
                current_user.update_from_form(form=user_form)
                return redirect(url_for("client_checkout.checkout", **{R.string.step_arg_name: 2}))
