# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from sqlalchemy import asc
from sqlalchemy.orm import relationship
from proj_exceptions import InvalidIdError
from extensions import db
from models.product import Product
from models.product_subcategory import ProductSubcategory
from r import R


class ProductCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(R.dimen.product_category_name_max_length))
    active = db.Column(db.Boolean, default=False, nullable=False)
    subcategories = relationship("ProductSubcategory", order_by=ProductSubcategory.name, back_populates="category")
    products = relationship("Product", order_by=Product.title, back_populates="category")
    editable = db.Column(db.Boolean, default=True, nullable=False)

    @staticmethod
    def create_from_form(add_product_category_form):
        product_category = ProductCategory(
            name=add_product_category_form.category_name.data,
            active=add_product_category_form.active.data
        )
        db.session.add(product_category)
        db.session.commit()

    @staticmethod
    def get(category_id):
        return ProductCategory.query.filter_by(id=category_id).one_or_none()

    @staticmethod
    def get_all():
        return ProductCategory.query.all()

    @staticmethod
    def update_from_form(product_category, edit_product_category_form):
        assert product_category.editable
        product_category.name = edit_product_category_form.category_name.data,
        product_category.active = edit_product_category_form.active.data
        db.session.add(product_category)
        db.session.commit()

    @staticmethod
    def update(product_category_id, **kw):
        product_category = ProductCategory.get(product_category_id)
        assert product_category != None
        assert product_category.editable
        for key, val in kw.iteritems():
            setattr(product_category, key, val)
        db.session.add(product_category)
        db.session.commit()
        return product_category

    @staticmethod
    def get_choices(include_all):
        choices = []

        if include_all:
            choices.append((str(0), R.string.all))

        for category in ProductCategory.query.order_by(asc(ProductCategory.name)).all():
            choices.append((str(category.id), category.name))

        return choices
