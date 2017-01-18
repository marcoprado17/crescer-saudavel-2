# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 14/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from extensions import db
from r import R
from wrappers.base.utils import safe_string


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    address = db.Column(db.String(R.dimen.contact_address_max_length))
    tel = db.Column(db.String(R.dimen.tel_max_length))
    email = db.Column(db.String(R.dimen.email_max_length))

    facebook_active = db.Column(db.Boolean, default=False, nullable=False)
    facebook_link = db.Column(db.Text)

    youtube_active = db.Column(db.Boolean, default=False, nullable=False)
    youtube_link = db.Column(db.Text)

    twitter_active = db.Column(db.Boolean, default=False, nullable=False)
    twitter_link = db.Column(db.Text)

    googleplus_active = db.Column(db.Boolean, default=False, nullable=False)
    googleplus_link = db.Column(db.Text)

    pintrest_active = db.Column(db.Boolean, default=False, nullable=False)
    pintrest_link = db.Column(db.Text)

    @staticmethod
    def get():
        contacts = Contact.query.all()
        assert len(contacts)
        return contacts[0]

    @staticmethod
    def set_values_from_form(contact_form):
        contact = Contact.get()

        contact.address = contact_form.address.data
        contact.tel = contact_form.tel.data
        contact.email = contact_form.email.data

        contact.facebook_active = contact_form.facebook_active.data
        contact.facebook_link = safe_string(contact_form.facebook_link.data)

        contact.youtube_active = contact_form.youtube_active.data
        contact.youtube_link = safe_string(contact_form.youtube_link.data)

        contact.twitter_active = contact_form.twitter_active.data
        contact.twitter_link = safe_string(contact_form.twitter_link.data)

        contact.googleplus_active = contact_form.googleplus_active.data
        contact.googleplus_link = safe_string(contact_form.googleplus_link.data)

        contact.pintrest_active = contact_form.pintrest_active.data
        contact.pintrest_link = safe_string(contact_form.pintrest_link.data)

        db.session.add(contact)
        db.session.commit()
