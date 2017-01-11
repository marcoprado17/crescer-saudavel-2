# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 11/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import json

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, IntegerField, SubmitField
from flask_bombril.form_fields import SelectFieldWithClasses
from models.city import City
from models.state import State
from r import R


class ClientForm(FlaskForm):
    email = StringField(label=R.string.email)
    email_confirmed = BooleanField(label=R.string.email_confirmed)
    first_name = StringField(label=R.string.first_name)
    last_name = StringField(label=R.string.last_name)
    state = SelectField(label=R.string.state)
    city = SelectField(label=R.string.city)
    address = StringField(label=R.string.address)
    address_number = IntegerField(label=R.string.number)
    address_complement = StringField(label=R.string.complement)
    cep = StringField(label=R.string.cep)
    tel = StringField(label=R.string.telephone)

    def __init__(self, **kwargs):
        super(ClientForm, self).__init__(**kwargs)

    def set_state_choices(self, include_undefined=False):
        self.state.choices = State.get_choices(include_undefined=include_undefined)

    def set_city_choices(self, include_undefined=False):
        self.city.choices = City.get_choices(include_undefined=include_undefined)

    def set_values(self, client):
        self.email.data = client.email
        self.email_confirmed.data = client.email_confirmed

        self.first_name.data = client.first_name
        self.last_name.data = client.last_name
        self.state.data = str(client.state.id) if client.state else str(0)
        self.city.data = str(client.city.id) if client.city else str(0)
        self.address.data = client.address
        self.address_number.data = client.address_number
        self.address_complement.data = client.address_complement
        self.cep.data = client.cep
        self.tel.data = client.tel


class AdminClientFilterForm(FlaskForm):
    state_id = SelectField(
        label=R.string.state
    )
    city_id = SelectFieldWithClasses(
        label=R.string.city,
        classes="dynamic"
    )
    filter = SubmitField(label=R.string.filter)

    def __init__(self, **kwargs):
        super(AdminClientFilterForm, self).__init__(**kwargs)
        self.state_id.choices = State.get_choices(include_all=True)
        self.city_id.choices = City.get_choices(include_all=True)
        dependent_choices = {}
        dependent_choices[str(0)] = [(str(0), R.string.all)]
        for state in State.get_all():
            choices = []
            choices.append((str(0), R.string.all))
            for city in state.cities:
                choices.append((str(city.id), city.name))
            dependent_choices[str(state.id)] = choices
        self.city_id.render_kw = dict(
            depends_on="state_id",
            dependent_choices=json.dumps(dependent_choices)
        )

    def set_values(self, state_id, city_id):
        self.state_id.data = str(state_id)
        self.city_id.data = str(city_id)
