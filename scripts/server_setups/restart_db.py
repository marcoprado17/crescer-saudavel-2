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
from models.state import State


def restart_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        create_states()

def create_states():
    db.session.add(State(name="SP", active=True))
    db.session.add(State(name="RJ", active=True))
    db.session.add(State(name="MG", active=True))
    db.session.add(State(name="GO", active=True))
    db.session.add(State(name="AC", active=True))
    db.session.add(State(name="AL", active=True))
    db.session.add(State(name="AP", active=True))
    db.session.add(State(name="AM", active=True))
    db.session.add(State(name="BA", active=True))
    db.session.add(State(name="CE", active=True))
    db.session.add(State(name="DF", active=True))
    db.session.add(State(name="ES", active=True))
    db.session.add(State(name="MA", active=True))
    db.session.add(State(name="MT", active=True))
    db.session.add(State(name="MS", active=True))
    db.session.add(State(name="PA", active=True))
    db.session.add(State(name="PB", active=True))
    db.session.add(State(name="PR", active=True))
    db.session.add(State(name="PE", active=True))
    db.session.add(State(name="PI", active=True))
    db.session.add(State(name="RN", active=True))
    db.session.add(State(name="RS", active=True))
    db.session.add(State(name="RO", active=True))
    db.session.add(State(name="RR", active=True))
    db.session.add(State(name="SC", active=True))
    db.session.add(State(name="SE", active=True))
    db.session.add(State(name="TO", active=True))

    db.session.commit()

    print "Db restarted."

if __name__ == "__main__":
    restart_db()
