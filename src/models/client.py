# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 10/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import current_app
from sqlalchemy import ForeignKey
from sqlalchemy import asc
from sqlalchemy import desc
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from proj_extensions import db, bcrypt
from models.base import BaseModel
from r import R
from routers.admin_clients.forms import ClientForm


class Client(BaseModel):
    email = db.Column(db.String(R.dimen.email_max_length), unique=True, nullable=False)
    _password = db.Column(db.Text, nullable=False)
    email_confirmed = db.Column(db.Boolean, default=False, nullable=False)
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

    sort_method_ids = [
        R.id.SORT_METHOD_CLIENT_NAME,
        R.id.SORT_METHOD_CLIENT_EMAIL,
        R.id.SORT_METHOD_NEWEST,
        R.id.SORT_METHOD_OLDER
    ]
    sort_method_names = [
        R.string.client_name,
        R.string.client_email,
        R.string.newest_register,
        R.string.older_register
    ]
    sort_method_by_id = {
        R.id.SORT_METHOD_CLIENT_NAME: asc(first_name),
        R.id.SORT_METHOD_CLIENT_EMAIL: asc(email),
        R.id.SORT_METHOD_NEWEST: desc(register_datetime),
        R.id.SORT_METHOD_OLDER: asc(register_datetime)
    }

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

    def get_form(self, include_undefined_in_choices=False):
        client_form = ClientForm()
        client_form.set_state_choices(include_undefined=include_undefined_in_choices)
        client_form.set_city_choices(include_undefined=include_undefined_in_choices)
        client_form.set_values(self)
        return client_form

    def get_freight(self):
        return R.dimen.freight

    @staticmethod
    def get(client_email):
        return Client.query.filter_by(email=client_email).one_or_none()

    def get_formatted_register_datetime(self):
        return R.string.formatted_datetime(self.register_datetime)
