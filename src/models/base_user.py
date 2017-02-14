# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 13/02/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from decimal import Decimal
from pprint import pprint

from sqlalchemy.orm.attributes import flag_modified

from models.base import BaseModel
from models.product import Product
from proj_exceptions import InvalidIdError, AmountExceededStock
from proj_extensions import db
from r import R


class BaseUser(BaseModel):
    __abstract__ = True

    _cart_amount_by_product_id = db.Column(db.JSON, default={}, nullable=False)

    def get_freight(self):
        return Decimal("0.00")

    def get_freight_as_string(self, include_rs=False):
        return R.string.decimal_price_as_string(price_as_decimal=self.get_freight(), include_rs=include_rs)

    def add_product_to_cart(self, product_id, amount=1):
        product = Product.get(product_id)
        if product is None:
            return R.id.ADD_TO_CART_NOT_EXCEEDED_STOCK, 0

        if self._cart_amount_by_product_id is None:
            self._cart_amount_by_product_id = {}

        initial_n_units = 0
        if str(product_id) in self._cart_amount_by_product_id.keys():
            initial_n_units = self._cart_amount_by_product_id[str(product_id)]
            self._cart_amount_by_product_id[str(product_id)] += amount
        else:
            self._cart_amount_by_product_id[str(product_id)] = amount

        return_value = R.id.ADD_TO_CART_NOT_EXCEEDED_STOCK
        if self._cart_amount_by_product_id[str(product_id)] > product.available - product.min_available:
            self._cart_amount_by_product_id[str(product_id)] = product.available - product.min_available
            return_value = R.id.ADD_TO_CART_EXCEEDED_STOCK

        final_n_units = self._cart_amount_by_product_id[str(product_id)]

        flag_modified(self, "_cart_amount_by_product_id")
        db.session.add(self)
        db.session.commit()

        return return_value, (final_n_units-initial_n_units)


    def delete_product_from_cart(self, product_id):
        if str(product_id) in self._cart_amount_by_product_id.keys():
            del self._cart_amount_by_product_id[str(product_id)]
        flag_modified(self, "_cart_amount_by_product_id")
        db.session.add(self)
        db.session.commit()

    def remove_from_cart(self, product_id, amount=1):
        if str(product_id) in self._cart_amount_by_product_id.keys():
            self._cart_amount_by_product_id[str(product_id)] -= amount
            if self._cart_amount_by_product_id[str(product_id)] <= 0:
                del self._cart_amount_by_product_id[str(product_id)]
        flag_modified(self, "_cart_amount_by_product_id")
        db.session.add(self)
        db.session.commit()

    def clear_cart(self):
        self._cart_amount_by_product_id = {}
        flag_modified(self, "_cart_amount_by_product_id")
        db.session.add(self)
        db.session.commit()

    def get_cart_data(self):
        if self._cart_amount_by_product_id is None:
            self._cart_amount_by_product_id = {}

        products = db.session.query(Product).filter(Product.id.in_([int(x) for x in self._cart_amount_by_product_id.keys()])).all()
        cart_data = []
        for product in products:
            cart_data.append((product, self._cart_amount_by_product_id[str(product.id)]))
        return cart_data

    def get_cart_products_total(self):
        cart_data = self.get_cart_data()
        products_total = Decimal("0.00")
        for product, amount in cart_data:
            products_total += product.get_price(n_units=amount)
        return products_total

    def get_cart_products_total_as_string(self, include_rs=False):
        return R.string.decimal_price_as_string(price_as_decimal=self.get_cart_products_total(), include_rs=include_rs)
