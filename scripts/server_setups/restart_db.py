# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 12/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import os
import sys

import shutil

sys.path.append("/vagrant")
sys.path.append("/vagrant/build")

from app_contexts.app import app
from proj_extensions import db
from models.utils import create_states, create_home_content, create_contact, create_about_us, create_faq, create_footer, create_header, \
    create_payment, create_dispatch, create_exchanges_and_returns, create_newsletter_emails


def restart_db():
    with app.app_context():
        whoosh_base_path = app.config['WHOOSH_BASE']
        if os.path.isdir(whoosh_base_path):
            shutil.rmtree(whoosh_base_path)

        db.drop_all()
        db.create_all()

        create_states()
        create_home_content()
        create_newsletter_emails()
        create_contact()
        create_about_us()
        create_faq()
        create_payment()
        create_dispatch()
        create_exchanges_and_returns()
        create_header()
        create_footer()
        print "Db restarted."

if __name__ == "__main__":
    restart_db()
