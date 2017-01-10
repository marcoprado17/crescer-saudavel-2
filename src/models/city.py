# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 10/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from extensions import db
from r import R


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(R.dimen.city_name_max_length))
    active = db.Column(db.Boolean, default=False, nullable=False)
    state_id = db.Column(db.Integer, ForeignKey("state.id"), nullable=False)
    state = relationship("State", back_populates="cities")
