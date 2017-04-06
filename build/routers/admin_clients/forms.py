# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 11/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import json

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, IntegerField, SubmitField

from flask_bombril.form_validators.phone_fomat.phone_format import PhoneFormat
from flask_bombril.cep_format.cep_format import CepFormat
from flask_bombril.form_validators import Required
from flask_bombril.form_fields import SelectFieldWithClasses
from models.city import City
from models.state import State
from r import R


class UserForm(FlaskForm):
    email = StringField(label=R.string.email, validators=[Required()])
    email_confirmed = BooleanField(label=R.string.email_confirmed)
    first_name = StringField(label=R.string.first_name, validators=[Required()])
    last_name = StringField(label=R.string.last_name, validators=[Required()])
    state_id = SelectField(label=R.string.state)
    city_id = SelectFieldWithClasses(label=R.string.city)
    address = StringField(label=R.string.address, validators=[Required()])
    address_number = IntegerField(label=R.string.number, validators=[Required()])
    address_complement = StringField(label=R.string.complement)
    cep = StringField(label=R.string.cep, validators=[Required(), CepFormat()])
    tel = StringField(label=R.string.telephone, validators=[Required(), PhoneFormat()])

    def __init__(self, user=None, edit=False, **kwargs):
        super(UserForm, self).__init__(**kwargs)

        self.state_id.choices = State.get_choices(include_undefined=not edit)
        self.city_id.choices = City.get_choices(include_undefined=not edit)

        if user is not None:
            self.email.data = user.email
            self.email_confirmed.data = user.email_confirmed

            self.first_name.data = user.first_name
            self.last_name.data = user.last_name
            self.state_id.data = str(user.state.id) if user.state else str(0)
            self.city_id.data = str(user.city.id) if user.city else str(0)
            self.address.data = user.address
            self.address_number.data = user.address_number
            self.address_complement.data = user.address_complement
            self.cep.data = user.cep
            self.tel.data = user.tel

        dependent_choices = {}
        for state in State.get_all():
            choices = []
            for city in state.cities:
                choices.append((str(city.id), city.name))
            dependent_choices[str(state.id)] = choices
        if not edit:
            dependent_choices[str(0)] = [(str(0), R.string.undefined_feminine)]

        self.city_id.render_kw = dict(
            depends_on="state_id",
            dependent_choices=json.dumps(dependent_choices)
        )

        if edit:
            self.city_id.classes = "dynamic"


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
