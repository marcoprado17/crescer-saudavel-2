# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 11/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask.ext.wtf import FlaskForm
from wtforms import SelectField, StringField, BooleanField, SubmitField

from flask_bombril.form_validators import Length
from flask_bombril.form_validators import Required
from models.state import State
from r import R


class CityForm(FlaskForm):
    state_id = SelectField(
        label=R.string.state,
        validators=[
            Required()
        ]
    )
    city_name = StringField(label=R.string.city_name, validators=[
        Required(),
        Length(max_length=R.dimen.city_name_max_length)
    ])
    active = BooleanField(
        label=R.string.active_in_female,
        default=True
    )

    def __init__(self, **kwargs):
        super(CityForm, self).__init__(**kwargs)
        self.state_id.choices = State.get_choices()


class AddCityForm(CityForm):
    submit = SubmitField(label=R.string.add)


class EditCityForm(CityForm):
    submit = SubmitField(label=R.string.edit)

    def set_values(self, city):
        self.state_id.data = str(city.state_id)
        self.city_name.data = city.name
        self.active.data = city.active
