# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 10/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from sqlalchemy import ForeignKey
from sqlalchemy import asc
from sqlalchemy.orm import relationship
from extensions import db
from r import R


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(R.dimen.city_name_max_length))
    active = db.Column(db.Boolean, default=False, nullable=False)
    state_id = db.Column(db.Integer, ForeignKey("state.id"), nullable=False)
    state = relationship("State", back_populates="cities")

    @staticmethod
    def get_choices(include_undefined=False, include_all=False):
        assert not(include_undefined and include_all)
        choices = []
        if include_undefined:
            choices.append((str(0), R.string.undefined_feminine))
        if include_all:
            choices.append((str(0), R.string.all))
        for city in City.query.order_by(asc(City.name)).all():
            choices.append((str(city.id), city.name))
        return choices

    @staticmethod
    def create_from_form(add_city_form):
        city = City(
            name=add_city_form.city_name.data,
            active=add_city_form.active.data,
            state_id=int(add_city_form.state_id.data)
        )
        db.session.add(city)
        db.session.commit()
        return city

    @staticmethod
    def get(city_id):
        return City.query.filter_by(id=city_id).one_or_none()

    @staticmethod
    def update(city_id, **kw):
        city = City.get(city_id)
        assert city != None
        for key, val in kw.iteritems():
            setattr(city, key, val)
        db.session.add(city)
        db.session.commit()
        return city

    @staticmethod
    def update_from_form(city, edit_city_form):
        city.name = edit_city_form.city_name.data
        city.active = edit_city_form.active.data
        city.state_id = edit_city_form.state_id.data
        db.session.add(city)
        db.session.commit()
