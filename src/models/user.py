# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 10/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from decimal import Decimal
from pprint import pprint

from flask import current_app
from flask_login import login_user
from sqlalchemy import ForeignKey
from sqlalchemy import asc
from sqlalchemy import desc
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from sqlalchemy.orm.attributes import flag_modified

from models.base import BaseModel
from models.product import Product
from proj_exceptions import InvalidIdError, AmountExceededStock
from proj_extensions import db, bcrypt, login_manager
from proj_utils import SortMethodMap
from r import R
from routers.admin_clients.forms import UserForm


class User(BaseModel):
    email = db.Column(db.String(R.dimen.email_max_length), unique=True, nullable=False)
    _password = db.Column(db.Text, nullable=False)
    email_confirmed = db.Column(db.Boolean, default=False, nullable=False)
    authenticated = db.Column(db.Boolean, default=False, nullable=False)
    register_datetime = db.Column(db.DateTime, nullable=False)
    _cart_amount_by_product_id = db.Column(db.JSON, default={}, nullable=False)

    orders = relationship("Order", order_by="desc(Order.paid_datetime)", back_populates="client")

    first_name = db.Column(db.String(R.dimen.first_name_max_length))
    last_name = db.Column(db.String(R.dimen.last_name_max_length))
    state_id = db.Column(db.Integer, ForeignKey("state.id"))
    state = relationship("State")
    city_id = db.Column(db.Integer, ForeignKey("city.id"))
    city = relationship("City")
    address = db.Column(db.String(R.dimen.address_max_length))
    address_number = db.Column(db.Integer)
    address_complement = db.Column(db.String(R.dimen.address_complement_max_length))
    cep = db.Column(db.String(R.dimen.cep_max_length))
    tel = db.Column(db.String(R.dimen.tel_max_length))

    sort_method_map = SortMethodMap([
        (R.id.SORT_METHOD_CLIENT_NAME,      R.string.client_name,       asc(first_name)),
        (R.id.SORT_METHOD_CLIENT_EMAIL,     R.string.client_email,      asc(email)),
        (R.id.SORT_METHOD_NEWEST,           R.string.newest_register,   desc(register_datetime)),
        (R.id.SORT_METHOD_OLDER,            R.string.older_register,    asc(register_datetime)),
    ])

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext):
        # TODO: Remove in production
        if current_app.config["DEBUG"]:
            self._password = plaintext
        else:
            self._password = bcrypt.generate_password_hash(plaintext)

    def is_correct_password(self, plaintext):
        # TODO: Remove in production
        if current_app.config["DEBUG"]:
            return self._password == plaintext
        else:
            return bcrypt.check_password_hash(self._password, plaintext)

    def is_active(self):
        return True

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    @staticmethod
    def get_attrs_from_form(form):
        return dict(
            email=form.email.data,
            password=form.password.data
        )

    def get_form(self, edit=False):
        return UserForm(user=self, edit=edit)

    def get_freight(self):
        return R.dimen.freight

    def get_freight_as_string(self, include_rs=False):
        return R.string.decimal_price_as_string(price_as_decimal=self.get_freight(), include_rs=include_rs)

    @staticmethod
    def get_by_email(client_email):
        return User.query.filter_by(email=client_email).one_or_none()

    def get_formatted_register_datetime(self):
        return self.register_datetime.strftime(R.string.default_datetime_format)

    def mark_email_as_confirmed(self):
        self.email_confirmed = True
        db.session.add(self)
        db.session.commit()

    def login_danger_danger(self):
        self.authenticated = True
        db.session.add(self)
        db.session.commit()
        login_user(self)

    def change_password(self, new_password):
        self.password = new_password
        db.session.add(self)
        db.session.commit()

    def add_product_to_cart(self, product_id, amount=1):
        product = Product.get(product_id)
        if product is None:
            raise InvalidIdError

        if amount > product.available:
            raise AmountExceededStock

        if self._cart_amount_by_product_id is None:
            self._cart_amount_by_product_id = {}

        if str(product_id) in self._cart_amount_by_product_id.keys():
            self._cart_amount_by_product_id[str(product_id)] += amount
        else:
            self._cart_amount_by_product_id[str(product_id)] = amount

        flag_modified(self, "_cart_amount_by_product_id")
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
