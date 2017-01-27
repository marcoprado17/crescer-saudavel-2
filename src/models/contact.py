# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 14/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from proj_exceptions import InconsistentDataBaseError
from proj_extensions import db
from models.base import BaseModel
from r import R
from proj_utils import safe_string


class Contact(BaseModel):
    address = db.Column(db.String(R.dimen.contact_address_max_length), default="")
    tel = db.Column(db.String(R.dimen.tel_max_length), default="")
    email = db.Column(db.String(R.dimen.email_max_length), default="")

    facebook_active = db.Column(db.Boolean, default=False, nullable=False)
    facebook_link = db.Column(db.Text, default="#")

    youtube_active = db.Column(db.Boolean, default=False, nullable=False)
    youtube_link = db.Column(db.Text, default="#")

    twitter_active = db.Column(db.Boolean, default=False, nullable=False)
    twitter_link = db.Column(db.Text, default="#")

    googleplus_active = db.Column(db.Boolean, default=False, nullable=False)
    googleplus_link = db.Column(db.Text, default="#")

    pintrest_active = db.Column(db.Boolean, default=False, nullable=False)
    pintrest_link = db.Column(db.Text, default="#")

    @staticmethod
    def get():
        contacts = Contact.query.all()
        if len(contacts) != 1:
            raise InconsistentDataBaseError
        return contacts[0]

    @staticmethod
    def get_attrs_from_form(form):
        return dict(
            address=form.address.data,
            tel=form.tel.data,
            email=form.email.data,

            facebook_active=form.facebook_active.data,
            facebook_link=safe_string(form.facebook_link.data),

            youtube_active=form.youtube_active.data,
            youtube_link=safe_string(form.youtube_link.data),

            twitter_active=form.twitter_active.data,
            twitter_link=safe_string(form.twitter_link.data),

            googleplus_active=form.googleplus_active.data,
            googleplus_link=safe_string(form.googleplus_link.data),

            pintrest_active=form.pintrest_active.data,
            pintrest_link=safe_string(form.pintrest_link.data),
        )
