# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 10/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import current_app
from sqlalchemy import ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from extensions import db, bcrypt
from models.order import Order
from r import R


class Client(db.Model):
    email = db.Column(db.String(R.dimen.email_max_length), primary_key=True, unique=True, nullable=False)
    _password = db.Column(db.Text, nullable=False)
    email_confirmed = db.Column(db.Boolean, default=False, nullable=False)
    authenticated = db.Column(db.Boolean, default=False, nullable=False)

    orders = relationship("Order", order_by=Order.paid_datetime, back_populates="client")

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
        return bcrypt.check_password_hash(self._password, plaintext)

    def is_active(self):
        return True

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False
