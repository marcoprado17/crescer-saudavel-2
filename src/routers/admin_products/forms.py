# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField
from flask_bombril.form_validators import Length
from flask_bombril.form_validators import Required
from r import R


class AddProductCategoryForm(FlaskForm):
    category_name = StringField(label=R.string.product_category_name, validators=[
        Required(),
        Length(max_length=R.dimen.product_category_max_length)
    ])
    active = BooleanField(label=R.string.active_in_female)
    submit = SubmitField(label=R.string.add)

class ProductCategoryFilterForm(FlaskForm):
    active = SelectField(
        label=R.string.category_status,
        choices=[(str(True), R.string.active_in_female), (str(False), R.string.inactive_in_female)]
    )
    filter = SubmitField(label=R.string.filter)

    def set_values(self, active):
        self.active.data = str(active)
