# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 12/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import sys

sys.path.append("/vagrant")
sys.path.append("/vagrant/build")

from app_contexts.app import app
from extensions import db
from models.utils import create_states, create_home_content, create_contact, create_about_us, create_faq, create_footer


def restart_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        create_states()
        create_home_content()
        create_contact()
        create_about_us()
        create_faq()
        create_footer()
        print "Db restarted."

if __name__ == "__main__":
    restart_db()
