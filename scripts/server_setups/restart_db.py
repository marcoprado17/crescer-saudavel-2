# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 12/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import datetime
import os
import shutil
import sys

sys.path.append("/vagrant")
sys.path.append("/vagrant/build")
sys.path.append("/vagrant/build/flask-admin")

from app_contexts.app import app
from proj_extensions import db
from models.state import State
from models.content.about_us import AboutUsContent
from models.content.contact import Contact
from models.content.dispatch import DispatchContent
from models.content.exchanges_and_returns import ExchangesAndReturnsContent
from models.content.faq import FaqContent
from models.content.footer import Footer
from models.content.header import HeaderContent
from models.content.home_content import HomeContent
from models.newsletter_emails import NewsletterEmails
from models.content.payment import PaymentContent
from models.content.tags_row import TagsRow
from models.user.user import User
from models.content.blog import BlogContent
from r import R


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
        create_blog_content()

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
    about_us = AboutUsContent()
    db.session.add(about_us)
    db.session.commit()
    print "AboutUs created."
    return about_us


def create_faq():
    faq = FaqContent()
    db.session.add(faq)
    db.session.commit()
    print "Faq created."
    return faq


def create_payment():
    payment = PaymentContent()
    db.session.add(payment)
    db.session.commit()
    print "Payment created."
    return payment


def create_dispatch():
    dispatch = DispatchContent()
    db.session.add(dispatch)
    db.session.commit()
    print "Dispatch created."
    return dispatch


def create_exchanges_and_returns():
    exchanges_and_returns = ExchangesAndReturnsContent()
    db.session.add(exchanges_and_returns)
    db.session.commit()
    print "ExchangesAndReturns created."
    return exchanges_and_returns


def create_header():
    header = HeaderContent()
    header.n_visible_categories = R.dimen.default_n_visible_categories
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


def create_blog_content():
    blog_content = BlogContent()
    db.session.add(blog_content)
    db.session.commit()
    print "BlogContent created."
    return blog_content


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
