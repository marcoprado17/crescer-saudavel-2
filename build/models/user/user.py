# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 10/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import random
import string
from datetime import datetime
from flask import current_app
from flask_login import login_user
from sqlalchemy import ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from sqlalchemy.orm.attributes import flag_modified
from models.user.base_user import BaseUser
from proj_extensions import db, bcrypt, login_manager
from r import R
from routers.client_account.forms import UserForm


class User(BaseUser):
    __tablename__ = "user"

    email = db.Column(db.String(R.dimen.email_max_length), unique=True, nullable=False)
    _password = db.Column(db.Text, nullable=False)
    email_confirmed = db.Column(db.Boolean, default=False, nullable=False)
    facebook_login = db.Column(db.Boolean, default=False, nullable=False)
    authenticated = db.Column(db.Boolean, default=False, nullable=False)
    register_datetime = db.Column(db.DateTime, nullable=False)

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

    @hybrid_property
    def name(self):
        if self.first_name is not None:
            return self.first_name
        elif self.email is not None:
            return self.email.split('@')[0]
        else:
            return None

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

    @property
    def is_active(self):
        return True

    def get_id(self):
        return self.id

    @property
    def is_authenticated(self):
        return self.authenticated

    @property
    def is_anonymous(self):
        return False

    # noinspection PyMethodParameters
    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    @classmethod
    def create_from_form(cls, form, other_attrs=None):
        attrs = dict(
            email=form.email.data,
            password=form.password.data
        )
        if other_attrs is not None and isinstance(other_attrs, dict):
            for key, val in other_attrs.iteritems():
                attrs[key] = val
        model_elem = cls(
            **attrs
        )
        db.session.add(model_elem)
        db.session.commit()
        return model_elem

    @classmethod
    def create_user_with_facebook_login(cls, email):
        random_password = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in
                                  range(R.dimen.password_max_length))
        user = User(
            email=email,
            password=random_password,
            email_confirmed=True,
            facebook_login=True,
            register_datetime=datetime.now()
        )
        db.session.add(user)
        db.session.commit()
        return user

    def update_from_form(self, form):
        attrs_dict = dict(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            state_id=int(form.state_id.data),
            city_id=int(form.city_id.data),
            address=form.address.data,
            address_number=form.address_number.data,
            address_complement=form.address_complement.data,
            cep=form.cep.data,
            tel=form.tel.data,
        )
        for key, val in attrs_dict.iteritems():
            setattr(self, key, val)
        db.session.add(self)
        db.session.commit()

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

    def login_danger_danger(self, base_user):
        if base_user.is_anonymous:
            for product, amount in base_user.get_cart_data():
                self.add_product_to_cart_without_commit(product_id=product.id, amount=amount)
            base_user.clear_cart_without_commit()

        self.authenticated = True
        login_user(self)
        flag_modified(self, "_cart_amount_by_product_id")
        db.session.add(self)
        db.session.commit()

    def change_password(self, new_password):
        self.password = new_password
        db.session.add(self)
        db.session.commit()
