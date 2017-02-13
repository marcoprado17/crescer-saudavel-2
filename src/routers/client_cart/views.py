# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import json
from pprint import pprint

from flask import render_template
from flask.ext.login import current_user
from flask.ext.login import login_required

from flask_bombril.url_args import get_valid_integer
from flask_bombril.url_args import get_valid_model_id
from models.product import Product
from proj_decorators import login_or_anonymous
from proj_exceptions import AmountExceededStock
from r import R
from routers.client_cart import client_cart_blueprint
from routers.client_cart.data_providers.cart import client_cart_data_provider


@client_cart_blueprint.route("/")
@login_or_anonymous
def cart(base_user):
    return render_template("client_cart/cart.html", data=client_cart_data_provider.get_data(base_user=base_user))


@client_cart_blueprint.route("/remover-tudo", methods=["POST"])
def remove_all():
    print("Remove all items of cart!!!")
    return "", 200


# TODO: Validate SubmitForm
@client_cart_blueprint.route("/adicionar-ao-carrinho", methods=["POST"])
@login_or_anonymous
def add_to_cart(base_user):
    product_id = get_valid_model_id(model=Product, arg_name=R.string.product_id_arg_name, include_zero=False, default=None)
    if product_id == None:
        return json.dumps(dict(error_msg=R.string.add_to_cart_error_msg_invalid_product_id)), 400
    amount = get_valid_integer(arg_name=R.string.amount_arg_name, default=1)
    try:
        base_user.add_product_to_cart(product_id=product_id, amount=amount)
    except AmountExceededStock:
        product = Product.get(product_id)
        return json.dumps(dict(error_msg=R.string.add_to_cart_error_msg_amount_exceeded_stock(product=product, amount=amount))), 400
    return "", 200


# TODO: Validate SubmitForm
@client_cart_blueprint.route("/remover-do-carrinho", methods=["POST"])
@login_or_anonymous
def remove_from_cart(base_user):
    product_id = get_valid_model_id(model=Product, arg_name=R.string.product_id_arg_name, include_zero=False, default=None)
    if product_id == None:
        return json.dumps(dict(error_msg=R.string.add_to_cart_error_msg_invalid_product_id)), 400
    amount = get_valid_integer(arg_name=R.string.amount_arg_name, default=1)
    # try:
    #     base_user.add_product_to_cart(product_id=product_id, amount=amount)
    # except AmountExceededStock:
    #     product = Product.get(product_id)
    #     return json.dumps(dict(error_msg=R.string.add_to_cart_error_msg_amount_exceeded_stock(product=product, amount=amount))), 400
    return "", 200


# TODO: Validate SubmitForm
@client_cart_blueprint.route("/remover-produto-do-carrinho", methods=["POST"])
@login_or_anonymous
def delete_product_from_cart(base_user):
    product_id = get_valid_model_id(model=Product, arg_name=R.string.product_id_arg_name, include_zero=False, default=None)
    if product_id == None:
        return json.dumps(dict(error_msg=R.string.add_to_cart_error_msg_invalid_product_id)), 400
    # try:
    #     base_user.add_product_to_cart(product_id=product_id, amount=amount)
    # except AmountExceededStock:
    #     product = Product.get(product_id)
    #     return json.dumps(dict(error_msg=R.string.add_to_cart_error_msg_amount_exceeded_stock(product=product, amount=amount))), 400
    return "", 200
