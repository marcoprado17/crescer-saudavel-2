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

def restart_db():
    with app.app_context():
        db.drop_all()
        db.create_all()

if __name__ == "__main__":
    restart_db()
