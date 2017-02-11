# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 11/02/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from decimal import Decimal

from sqlalchemy import JSON
from models.base import BaseModel
from models.product import Product
from proj_extensions import db


class BaseUser(BaseModel):
    __abstract__ = True

    _cart_amount_by_product_id = db.Column(JSON, default={}, nullable=False)

    def add_product_to_cart(self, product_id, amount=1):
        if product_id in self._cart_amount_by_product_id:
            self._cart_amount_by_product_id[product_id] += amount
        else:
            self._cart_amount_by_product_id[product_id] = amount

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
        products_total = self.get_cart_products_total()
        s = ""
        if include_rs:
            s += "R$ "
        s += str(products_total).replace(".", ",")
        return s

    def get_freight(self):
        raise NotImplementedError

    def get_freight_as_string(self, include_rs=False):
        raise NotImplementedError
