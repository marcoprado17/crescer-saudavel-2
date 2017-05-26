# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 10/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from proj_extensions import db
from models.base import BaseModel
from r import R


class City(BaseModel):
    __tablename__ = "city"

    name = db.Column(db.String(R.dimen.city_name_max_length), nullable=False)
    active = db.Column(db.Boolean, default=False, nullable=False)
    state_id = db.Column(db.Integer, ForeignKey("state.id"), nullable=False)
    state = relationship("State", uselist=False)
