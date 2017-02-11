# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 11/02/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from decimal import Decimal
from sqlalchemy import JSON
from models.base import BaseModel
from models.product import Product
from proj_exceptions import InvalidIdError, AmountExceededStock
from proj_extensions import db, login_manager
from r import R



class BaseUser(BaseModel):
    __abstract__ = True

    _cart_amount_by_product_id = db.Column(JSON, default={}, nullable=False)

    def add_product_to_cart(self, product_id, amount=1):
        product = Product.get(product_id)
        if product is None:
            raise InvalidIdError

        if amount > product.available:
            raise AmountExceededStock

        if self._cart_amount_by_product_id is None:
            self._cart_amount_by_product_id = {}

        if product_id in self._cart_amount_by_product_id.keys():
            self._cart_amount_by_product_id[product_id] += amount
        else:
            self._cart_amount_by_product_id[product_id] = amount
        db.session.add(self)
        db.session.commit()

    def get_cart_data(self):
        products = db.session.query(Product).filter(Product.id.in_(self._cart_amount_by_product_id.keys())).all()
        cart_data = []
        for product in products:
            cart_data.append((product, self._cart_amount_by_product_id[product.id]))
        return cart_data

    def get_cart_products_total(self):
        cart_data = self.get_cart_data()
        products_total = Decimal("0.00")
        for product, amount in cart_data:
            products_total += product.get_price(n_units=amount)
        return products_total

    def get_cart_products_total_as_string(self, include_rs=False):
        return R.string.decimal_price_as_string(price_as_decimal=self.get_cart_products_total(), include_rs=include_rs)

    def get_freight(self):
        raise NotImplementedError

    def get_freight_as_string(self, include_rs=False):
        raise NotImplementedError

    @login_manager.user_loader
    def load_user(user_id):
        return BaseUser.get(user_id)
