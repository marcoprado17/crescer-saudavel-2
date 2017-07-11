# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import json

from flask import flash
from flask import redirect
from flask import render_template
from flask import url_for
from flask_bombril.url_args import get_boolean_url_arg
from flask_bombril.url_args import get_valid_integer
from flask_bombril.url_args import get_valid_model_id
from models.product.product import Product
from proj_decorators import login_or_anonymous, valid_form, protect_against_csrf
from proj_forms import SubmitForm
from r import R
from routes.cart import cart_blueprint
from flask_bombril.r import R as bombril_R


@cart_blueprint.route("/")
@login_or_anonymous
def cart(user):
    breadcumb = [(R.string.home, url_for("home.home")), R.string.my_cart]
    return render_template(
        "cart/cart.html",
        breadcumb=breadcumb,
        cart_data=user.get_cart_data(),
        products_total=user.get_cart_products_total(),
        freight=user.get_freight(),
        total=user.get_total()
    )


@cart_blueprint.route("/adicionar-ao-carrinho", methods=["POST"])
@login_or_anonymous
@protect_against_csrf
def add_to_cart(user):
    product_id = get_valid_model_id(model=Product, arg_name=R.string.product_id_arg_name, include_zero=False,
                                    default=None)
    redirect_to_cart = get_boolean_url_arg(arg_name=R.string.redirect_to_cart_arg_name, default=True)
    if product_id == None:
        if redirect_to_cart:
            flash(R.string.add_cart_fail_invalid_product,
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.error))
            return redirect(url_for("cart.cart"))
        else:
            return "", 400
    amount = get_valid_integer(arg_name=R.string.amount_arg_name, default=1)
    add_product_to_cart_result, amount_added = user.add_product_to_cart(product_id=product_id, amount=amount)
    if redirect_to_cart:
        product = Product.get(product_id)
        if add_product_to_cart_result == R.id.ADD_TO_CART_NOT_EXCEEDED_STOCK:
            flash(
                R.string.product_added_to_cart_without_stock_overflow(amount=amount_added, product_title=product.title),
                bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.success))
        elif add_product_to_cart_result == R.id.ADD_TO_CART_EXCEEDED_STOCK:
            flash(R.string.product_added_to_cart_with_stock_overflow(amount=amount_added, product_title=product.title),
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.warning))
        return redirect(url_for("cart.cart"))
    else:
        return "", 200


@cart_blueprint.route("/remover-do-carrinho", methods=["POST"])
@login_or_anonymous
@protect_against_csrf
def remove_from_cart(user):
    product_id = get_valid_model_id(model=Product, arg_name=R.string.product_id_arg_name, include_zero=False,
                                    default=None)
    if product_id == None:
        return json.dumps(dict(error_msg=R.string.add_to_cart_error_msg_invalid_product_id)), 400
    amount = get_valid_integer(arg_name=R.string.amount_arg_name, default=1)
    user.remove_from_cart(product_id=product_id, amount=amount)
    return "", 200


@cart_blueprint.route("/remover-produto-do-carrinho", methods=["POST"])
@login_or_anonymous
@protect_against_csrf
def delete_product_from_cart(user):
    product_id = get_valid_model_id(model=Product, arg_name=R.string.product_id_arg_name, include_zero=False,
                                    default=None)
    user.delete_product_from_cart(product_id=product_id)
    product = Product.get(product_id)
    if product is not None:
        flash(R.string.product_removed_from_cart(product.title),
              bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.info))
    return redirect(url_for("cart.cart"))


@cart_blueprint.route("/limpar-carrinho", methods=["POST"])
@login_or_anonymous
@protect_against_csrf
def clear_cart(user):
    user.clear_cart()
    flash(R.string.cart_cleared,
          bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.info))
    return redirect(url_for("cart.cart"))
