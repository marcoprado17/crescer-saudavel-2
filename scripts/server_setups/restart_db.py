# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 12/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from src.app_contexts.app import app
from src.extensions import db

def restart_db():
    with app.app_context():
        db.session.drop_all()
        db.session.create_all()

if __name__ == "__main__":
    restart_db()
