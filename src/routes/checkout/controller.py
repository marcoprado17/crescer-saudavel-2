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
from flask_bombril.url_args import get_valid_integer, get_boolean_url_arg
from r import R
from routes.my_account.forms import UserForm
from routes.checkout import checkout_blueprint
from routes.checkout.data_providers.checkout import client_checkout_data_provider
from flask_bombril.r import R as bombril_R


@checkout_blueprint.route("/confirmar-compra")
@login_required
def confirm_purchase():
    user = current_user
    return render_template(
        "checkout/confirm_purchase.html",
        cart_data=user.get_cart_data(),
        products_total=user.get_cart_products_total(),
        freight=user.get_freight(),
        total=user.get_total()
    )


@checkout_blueprint.route("/confirmar-endereco", methods=["GET", "POST"])
@login_required
def confirm_address():
    user = current_user
    edit = get_boolean_url_arg(R.string.edit_arg_name, default=False)
    if request.method == "GET":
        return render_template(
            "checkout/confirm_address.html",
            edit=edit,
            user_form=user.get_form(edit=edit)
        )
    else:
        user_form = UserForm(edit=True)
        if not user_form.validate_on_submit():
            flash(R.string.there_is_some_data_missing, "static-error")
            return render_template(
                "checkout/confirm_address.html",
                edit=True,
                user_form=user_form
            )
        else:
            user.update_from_form(form=user_form)
            if edit:
                return redirect(url_for("checkout.confirm_address"))
            else:
                return redirect(url_for("checkout.payment"))

@checkout_blueprint.route("/pagamento", methods=["GET", "POST"])
@login_required
def payment():
    return render_template(
        "checkout/payment.html",
    )


# @checkout_blueprint.route("/", methods=["GET", "POST"])
# @login_required
# def checkout():
#     step = get_valid_integer(arg_name=R.string.step_arg_name, default=1)
#     if request.method == "GET":
#         return render_template("checkout/base.html", data=client_checkout_data_provider.get_data(step=step))
#     else:
#         if step == 1:
#             user_form = UserForm(edit=True)
#             if not user_form.validate_on_submit():
#                 flash(R.string.fix_form_errors_before_proceed,
#                       bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.error))
#                 return render_template("checkout/checkout.html",
#                                        data=client_checkout_data_provider.get_data_when_post(step=1, user_form=user_form))
#             else:
#                 current_user.update_from_form(form=user_form)
#                 return redirect(url_for("checkout.checkout", **{R.string.step_arg_name: 2}))
