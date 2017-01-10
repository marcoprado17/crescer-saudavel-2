# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import json
import os

from flask import current_app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField, IntegerField, TextAreaField

from flask_bombril.form_fields import SelectFieldWithClasses
from flask_bombril.form_validators import MarkdownValidator
from flask_bombril.form_validators import NotNegativeInteger
from flask_bombril.form_validators import Price
from flask_bombril.form_validators import Length
from flask_bombril.form_validators import Required
from models.product_category import ProductCategory
from models.product_subcategory import ProductSubcategory
from r import R


# ======================================================================================================================
#
#
# Product Category
#
#
# ======================================================================================================================
class ProductCategoryForm(FlaskForm):
    category_name = StringField(
        label=R.string.product_category_name,
        validators=[
            Required(),
            Length(max_length=R.dimen.product_category_name_max_length)
        ]
    )
    active = BooleanField(
        label=R.string.active_in_female,
        default=True
    )


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
        label=R.string.category,
        validators=[
            Required()
        ]
    )
    subcategory_name = StringField(label=R.string.product_subcategory_name, validators=[
        Required(),
        Length(max_length=R.dimen.product_subcategory_name_max_length)
    ])
    active = BooleanField(
        label=R.string.active_in_female,
        default=True
    )

    def __init__(self, **kwargs):
        super(ProductSubcategoryForm, self).__init__(**kwargs)
        self.category_id.choices = ProductCategory.get_choices(include_all=False)


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
        self.category_id.choices = ProductCategory.get_choices(include_all=True)

    def set_values(self, category_id, active):
        self.category_id.data = str(category_id)
        self.active.data = str(active)


# ======================================================================================================================
#
#
# Product Subcategory
#
#
# ======================================================================================================================


def get_tab_title(n):
    return StringField(
    label=R.string.n_tab_title(n),
    validators=[
        Length(max_length=R.dimen.tab_title_max_length)
    ])


def get_tab_content(n):
    return TextAreaField(
    label=R.string.n_tab_content(n),
    validators=[
        MarkdownValidator()
    ])


class ProductForm(FlaskForm):
    title = StringField(
        label=R.string.title,
        validators=[
            Required(),
            Length(max_length=R.dimen.product_title_max_length)
        ])
    active = BooleanField(
        label=R.string.active,
        default=True
    )
    category_id = SelectField(
        label=R.string.category,
        validators=[
            Required()
        ]
    )
    subcategory_id = SelectField(
        label=R.string.subcategory,
        validators=[
            Required()
        ]
    )
    price = StringField(
        label=R.string.price,
        validators=[
            Required(),
            Price(),
        ],
        render_kw=dict(
            tooltip=R.string.price_in_real
        )
    )
    stock = IntegerField(
        label=R.string.stock_quantity,
        validators=[
            Required(),
            NotNegativeInteger(),
        ])
    min_stock = IntegerField(
        label=R.string.min_stock,
        validators=[
            Required(),
            NotNegativeInteger(),
        ],
        render_kw=dict(
            tooltip=R.string.min_stock_tooltip
        )
    )
    summary = TextAreaField(
        label=R.string.summary,
        validators=[
            Required(),
            MarkdownValidator()
        ])

    image_1 = SelectField(
        label=R.string.n_image(1),
        validators=[
            Required()
        ]
    )
    image_2 = SelectField(label=R.string.n_image(2))
    image_3 = SelectField(label=R.string.n_image(3))
    image_4 = SelectField(label=R.string.n_image(4))
    image_5 = SelectField(label=R.string.n_image(5))
    image_6 = SelectField(label=R.string.n_image(6))
    image_7 = SelectField(label=R.string.n_image(7))
    image_8 = SelectField(label=R.string.n_image(8))
    image_9 = SelectField(label=R.string.n_image(9))
    image_10 = SelectField(label=R.string.n_image(10))

    tab_1_title = get_tab_title(1)
    tab_1_content = get_tab_content(1)
    tab_2_title = get_tab_title(2)
    tab_2_content = get_tab_content(2)
    tab_3_title = get_tab_title(3)
    tab_3_content = get_tab_content(3)
    tab_4_title = get_tab_title(4)
    tab_4_content = get_tab_content(4)
    tab_5_title = get_tab_title(5)
    tab_5_content = get_tab_content(5)
    tab_6_title = get_tab_title(6)
    tab_6_content = get_tab_content(6)
    tab_7_title = get_tab_title(7)
    tab_7_content = get_tab_content(7)
    tab_8_title = get_tab_title(8)
    tab_8_content = get_tab_content(8)
    tab_9_title = get_tab_title(9)
    tab_9_content = get_tab_content(9)
    tab_10_title = get_tab_title(10)
    tab_10_content = get_tab_content(10)

    def __init__(self, **kwargs):
        super(ProductForm, self).__init__(**kwargs)

        self.category_id.choices = ProductCategory.get_choices(include_all=False)
        self.subcategory_id.choices = ProductSubcategory.get_choices(include_all=False, include_none=True)
        dependent_choices = {}
        for category in ProductCategory.get_all():
            choices = []
            choices.append((str(0), R.string.none_in_female))
            for subcategory in category.subcategories:
                choices.append((str(subcategory.id), subcategory.name))
            dependent_choices[str(category.id)] = choices
        self.subcategory_id.render_kw = dict(
            depends_on="category_id",
            dependent_choices=json.dumps(dependent_choices)
        )

        images_name = os.listdir(current_app.config["UPLOADED_IMAGES_FOLDER_FULL_PATH"])
        images_name.sort()
        image_choices = []
        for image_name in images_name:
            image_choices.append((image_name, image_name))
        self.image_1.choices = image_choices
        image_choices = [("", R.string.none_in_female)] + image_choices
        self.image_2.choices = image_choices
        self.image_3.choices = image_choices
        self.image_4.choices = image_choices
        self.image_5.choices = image_choices
        self.image_6.choices = image_choices
        self.image_7.choices = image_choices
        self.image_8.choices = image_choices
        self.image_9.choices = image_choices
        self.image_10.choices = image_choices


class AddProductForm(ProductForm):
    submit = SubmitField(label=R.string.add)


class EditProductForm(ProductForm):
    submit = SubmitField(label=R.string.edit)

    def set_values(self, product):
        self.title.data = product.title
        self.active.data = product.active
        self.category_id.data = str(product.category_id)
        self.subcategory_id.data = str(product.subcategory_id)
        self.price.data = str(product.price).replace(".", ",")
        self.stock.data = product.stock
        self.min_stock.data = product.min_stock
        self.summary.data = product.summary

        self.image_1.data = product.image_1
        self.image_2.data = product.image_2
        self.image_3.data = product.image_3
        self.image_4.data = product.image_4
        self.image_5.data = product.image_5
        self.image_6.data = product.image_6
        self.image_7.data = product.image_7
        self.image_8.data = product.image_8
        self.image_9.data = product.image_9
        self.image_10.data = product.image_10

        self.tab_1_title.data = product.tab_1_title
        self.tab_1_content.data = product.tab_1_content
        self.tab_2_title.data = product.tab_2_title
        self.tab_2_content.data = product.tab_2_content
        self.tab_3_title.data = product.tab_3_title
        self.tab_3_content.data = product.tab_3_content
        self.tab_4_title.data = product.tab_4_title
        self.tab_4_content.data = product.tab_4_content
        self.tab_5_title.data = product.tab_5_title
        self.tab_5_content.data = product.tab_5_content
        self.tab_6_title.data = product.tab_6_title
        self.tab_6_content.data = product.tab_6_content
        self.tab_7_title.data = product.tab_7_title
        self.tab_7_content.data = product.tab_7_content
        self.tab_8_title.data = product.tab_8_title
        self.tab_8_content.data = product.tab_8_content
        self.tab_9_title.data = product.tab_9_title
        self.tab_9_content.data = product.tab_9_content
        self.tab_10_title.data = product.tab_10_title
        self.tab_10_content.data = product.tab_10_content


class ProductFilterForm(FlaskForm):
    category_id = SelectField(
        label=R.string.category
    )
    subcategory_id = SelectFieldWithClasses(
        label=R.string.subcategory,
        classes="dynamic"
    )
    active = SelectField(
        label=R.string.product_status,
        choices=[(str(True), R.string.active), (str(False), R.string.inactive)]
    )
    filter = SubmitField(label=R.string.filter)

    def __init__(self, **kwargs):
        super(ProductFilterForm, self).__init__(**kwargs)
        self.category_id.choices = ProductCategory.get_choices(include_all=True)
        self.subcategory_id.choices = ProductSubcategory.get_choices(include_all=True)
        dependent_choices = {}
        dependent_choices[str(0)] = [(str(0), R.string.all)]
        for category in ProductCategory.get_all():
            choices = []
            choices.append((str(0), R.string.all))
            for subcategory in category.subcategories:
                choices.append((str(subcategory.id), subcategory.name))
            dependent_choices[str(category.id)] = choices
        self.subcategory_id.render_kw = dict(
            depends_on="category_id",
            dependent_choices=json.dumps(dependent_choices)
        )

    def set_values(self, category_id, subcategory_id, active):
        self.category_id.data = str(category_id)
        self.subcategory_id.data = str(subcategory_id)
        self.active.data = str(active)


class AddToStockForm(FlaskForm):
    value = IntegerField(
        label=R.string.example_42,
        validators=[
            Required(),
            NotNegativeInteger(),
        ]
    )
    submit = SubmitField(label=R.string.add_to_stock)


class RemoveFromStockForm(FlaskForm):
    value = IntegerField(
        label=R.string.example_42,
        validators=[
            Required(),
            NotNegativeInteger(),
        ]
    )
    submit = SubmitField(label=R.string.remove_from_stock)


class UpdateStockForm(FlaskForm):
    value = IntegerField(
        label=R.string.example_42,
        validators=[
            Required(),
            NotNegativeInteger(),
        ]
    )
    submit = SubmitField(label=R.string.update_stock)
