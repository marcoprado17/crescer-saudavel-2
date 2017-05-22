# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 12/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import os
import sys
import shutil
import datetime

sys.path.append("/vagrant")
sys.path.append("/vagrant/build")

from app_contexts.app import app
from proj_extensions import db
from models.state import State
from models.about_us import AboutUs
from models.contact import Contact
from models.dispatch import Dispatch
from models.exchanges_and_returns import ExchangesAndReturns
from models.faq import Faq
from models.footer import Footer
from models.header import Header
from models.home_content import HomeContent
from models.newsletter_emails import NewsletterEmails
from models.payment import Payment
from models.tags_row import TagsRow
from models.user import User


def restart_db():
    with app.app_context():
        whoosh_base_full_path = app.config['WHOOSH_BASE']
        if os.path.isdir(whoosh_base_full_path):
            shutil.rmtree(whoosh_base_full_path)

        db.drop_all()
        db.create_all()

        create_states()
        create_home_content()
        create_newsletter_emails()
        create_tags_row()
        create_contact()
        create_about_us()
        create_faq()
        create_payment()
        create_dispatch()
        create_exchanges_and_returns()
        create_header()
        create_footer()

        if app.config["DEBUG"]:
            create_admin_user()

        print "Db restarted."


def create_states():
    db.session.add(State(name="SP"))
    db.session.add(State(name="RJ"))
    db.session.add(State(name="MG"))
    db.session.add(State(name="GO"))
    db.session.add(State(name="AC"))
    db.session.add(State(name="AL"))
    db.session.add(State(name="AP"))
    db.session.add(State(name="AM"))
    db.session.add(State(name="BA"))
    db.session.add(State(name="CE"))
    db.session.add(State(name="DF"))
    db.session.add(State(name="ES"))
    db.session.add(State(name="MA"))
    db.session.add(State(name="MT"))
    db.session.add(State(name="MS"))
    db.session.add(State(name="PA"))
    db.session.add(State(name="PB"))
    db.session.add(State(name="PR"))
    db.session.add(State(name="PE"))
    db.session.add(State(name="PI"))
    db.session.add(State(name="RN"))
    db.session.add(State(name="RS"))
    db.session.add(State(name="RO"))
    db.session.add(State(name="RR"))
    db.session.add(State(name="SC"))
    db.session.add(State(name="SE"))
    db.session.add(State(name="TO"))
    db.session.commit()
    print "States created."


def create_home_content():
    home_content = HomeContent()
    db.session.add(home_content)
    db.session.commit()
    print "Home content created."
    return home_content


def create_newsletter_emails():
    newsletter_emails = NewsletterEmails()
    db.session.add(newsletter_emails)
    db.session.commit()
    print "Newsletter emails created."
    return newsletter_emails


def create_tags_row():
    tags_row = TagsRow()
    db.session.add(tags_row)
    db.session.commit()
    print "Tags row created."
    return tags_row


def create_contact():
    contact = Contact()
    db.session.add(contact)
    db.session.commit()
    print "Contact created."
    return contact


def create_about_us():
    about_us = AboutUs()
    db.session.add(about_us)
    db.session.commit()
    print "AboutUs created."
    return about_us


def create_faq():
    faq = Faq()
    db.session.add(faq)
    db.session.commit()
    print "Faq created."
    return faq


def create_payment():
    payment = Payment()
    db.session.add(payment)
    db.session.commit()
    print "Payment created."
    return payment


def create_dispatch():
    dispatch = Dispatch()
    db.session.add(dispatch)
    db.session.commit()
    print "Dispatch created."
    return dispatch


def create_exchanges_and_returns():
    exchanges_and_returns = ExchangesAndReturns()
    db.session.add(exchanges_and_returns)
    db.session.commit()
    print "ExchangesAndReturns created."
    return exchanges_and_returns


def create_header():
    header = Header()
    db.session.add(header)
    db.session.commit()
    print "Header created."
    return header


def create_footer():
    footer = Footer()
    db.session.add(footer)
    db.session.commit()
    print "Footer created."
    return footer


def create_admin_user():
    user = User(
        email=app.config["ADMIN_MAIL"],
        password="aaaaaa",
        email_confirmed=True,
        register_datetime=datetime.datetime.now(),
    )
    db.session.add(user)
    db.session.commit()
    print "Admin user created."
    return user


if __name__ == "__main__":
    restart_db()
