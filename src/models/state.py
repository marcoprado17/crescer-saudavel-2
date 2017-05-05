# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 10/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from sqlalchemy import asc
from sqlalchemy.orm import relationship
from proj_extensions import db
from models.base import BaseModel, ProjBaseView
from models.city import City
from r import R


class State(BaseModel):
    __tablename__ = "state"

    name = db.Column(db.String(R.dimen.state_name_max_length), nullable=False)
    cities = relationship("City", order_by=City.name, back_populates="state")

    def __repr__(self):
        return self.name

    @staticmethod
    def get_choices(include_undefined=False, include_all=False):
        assert not(include_undefined and include_all)
        choices = []
        if include_undefined:
            choices.append((str(0), R.string.undefined_masculine))
        if include_all:
            choices.append((str(0), R.string.all_in_masculine))
        for state in State.query.order_by(asc(State.name)).all():
            choices.append((str(state.id), state.name))
        return choices
