# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from sqlalchemy import ForeignKey
from sqlalchemy import asc
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from proj_extensions import db
from models.base import BaseModel
from models.product import Product
from proj_exceptions import InvalidIdError
from r import R


class ProductSubcategory(BaseModel):
    name = db.Column(db.String(R.dimen.product_subcategory_name_max_length), nullable=False)
    active = db.Column(db.Boolean, default=False, nullable=False)
    category_id = db.Column(db.Integer, ForeignKey("product_category.id"), nullable=False)
    category = relationship("ProductCategory", back_populates="subcategories")
    products = relationship("Product", order_by=Product.title, back_populates="subcategory")

    sort_method_ids = [
        R.id.SORT_METHOD_ID,
        R.id.SORT_METHOD_NAME,
    ]
    sort_method_names = [
        R.string.id,
        R.string.subcategory_name,
    ]
    sort_method_by_id = {
        R.id.SORT_METHOD_ID: asc(BaseModel.id),
        R.id.SORT_METHOD_NAME: asc(name),
    }

    @staticmethod
    def create_from_form(add_product_subcategory_form):
        product_subcategory = ProductSubcategory(
            name=add_product_subcategory_form.subcategory_name.data,
            active=add_product_subcategory_form.active.data,
            category_id=int(add_product_subcategory_form.category_id.data)
        )
        db.session.add(product_subcategory)
        db.session.commit()
        return product_subcategory

    @staticmethod
    def get(subcategory_id):
        return ProductSubcategory.query.filter_by(id=subcategory_id).one_or_none()

    @staticmethod
    def set_active_value(subcategory_id, active):
        product_subcategory = ProductSubcategory.query.filter_by(id=subcategory_id).one_or_none()
        if not product_subcategory:
            raise InvalidIdError
        product_subcategory.active = active
        db.session.add(product_subcategory)
        db.session.commit()

    @staticmethod
    def update_from_form(product_subcategory, edit_product_subcategory_form):
        product_subcategory.name = edit_product_subcategory_form.subcategory_name.data,
        product_subcategory.active = edit_product_subcategory_form.active.data
        product_subcategory.category_id = edit_product_subcategory_form.category_id.data
        db.session.add(product_subcategory)
        db.session.commit()
        return product_subcategory

    @staticmethod
    def get_choices(include_all=False, include_none=False):
        assert not(include_all and include_none)

        choices = []

        if include_all:
            choices.append((str(0), R.string.all))
        if include_none:
            choices.append((str(0), R.string.none_in_female))

        for subcategory in ProductSubcategory.query.order_by(asc(ProductSubcategory.name)).all():
            choices.append((str(subcategory.id), subcategory.name))

        return choices
