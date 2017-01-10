# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 10/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from sqlalchemy.orm import relationship
from extensions import db
from models.city import City
from r import R


class State(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(R.dimen.state_name_max_length))
    active = db.Column(db.Boolean, default=False, nullable=False)
    cities = relationship("City", order_by=City.name, back_populates="state")
