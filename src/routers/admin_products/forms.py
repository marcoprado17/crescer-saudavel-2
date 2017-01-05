# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField
from flask_bombril.form_validators import Length
from flask_bombril.form_validators import Required
from models.product_category import ProductCategory
from r import R

# ======================================================================================================================
#
#
# Product Category
#
#
# ======================================================================================================================
class ProductCategoryForm(FlaskForm):
    category_name = StringField(label=R.string.product_category_name, validators=[
        Required(),
        Length(max_length=R.dimen.product_category_max_length)
    ])
    active = BooleanField(label=R.string.active_in_female, default=True)


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

# ======================================================================================================================
#
#
# Product Subcategory
#
#
# ======================================================================================================================
class ProductSubcategoryForm(FlaskForm):
    category_id = SelectField(
        label=R.string.category
    )
    subcategory_name = StringField(label=R.string.product_subcategory_name, validators=[
        Required(),
        Length(max_length=R.dimen.product_subcategory_max_length)
    ])
    active = BooleanField(label=R.string.active_in_female, default=True)

    def __init__(self, **kwargs):
        super(ProductSubcategoryForm, self).__init__(**kwargs)
        self.category_id.choices=ProductCategory.get_choices(include_all=False)


class AddProductSubcategoryForm(ProductSubcategoryForm):
    submit = SubmitField(label=R.string.add)


class EditProductSubcategoryForm(ProductSubcategoryForm):
    submit = SubmitField(label=R.string.edit)

    def set_values(self, product_subcategory):
        self.category_id.data = str(product_subcategory.category_id)
        self.subcategory_name.data = product_subcategory.name
        self.active.data = product_subcategory.active


class ProductSubcategoryFilterForm(FlaskForm):
    category_id = SelectField(
        label=R.string.category
    )
    active = SelectField(
        label=R.string.subcategory_status,
        choices=[(str(True), R.string.active_in_female), (str(False), R.string.inactive_in_female)]
    )
    filter = SubmitField(label=R.string.filter)

    def __init__(self, **kwargs):
        super(ProductSubcategoryFilterForm, self).__init__(**kwargs)
        self.category_id.choices=ProductCategory.get_choices(include_all=True)

    def set_values(self, category_id, active):
        self.category_id.data = str(category_id)
        self.active.data = str(active)
