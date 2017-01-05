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


class ProductCategoryForm(FlaskForm):
    category_name = StringField(label=R.string.product_category_name, validators=[
        Required(),
        Length(max_length=R.dimen.product_category_max_length)
    ])
    active = BooleanField(label=R.string.active_in_female)


class AddProductCategoryForm(ProductCategoryForm):
    submit = SubmitField(label=R.string.add)


class EditProductCategoryForm(ProductCategoryForm):
    submit = SubmitField(label=R.string.edit)

    def set_values(self, product_category):
        self.category_name.data = product_category.name
        self.active.data = product_category.active


class ProductCategoryFilterForm(FlaskForm):
    active = SelectField(
        label=R.string.category_status,
        choices=[(str(True), R.string.active_in_female), (str(False), R.string.inactive_in_female)]
    )
    filter = SubmitField(label=R.string.filter)

    def set_values(self, active):
        self.active.data = str(active)
