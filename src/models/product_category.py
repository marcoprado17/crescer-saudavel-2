# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from sqlalchemy import asc
from sqlalchemy import desc
from sqlalchemy.orm import relationship
from models.base import BaseModel
from proj_extensions import db
from models.product import Product
from models.product_subcategory import ProductSubcategory
from proj_utils import SortMethodMap
from r import R


class ProductCategory(BaseModel):
    __tablename__ = "product_category"

    name = db.Column(db.String(R.dimen.product_category_name_max_length), nullable=False)
    priority = db.Column(db.Integer, default=R.dimen.default_product_category_priority, nullable=False)
    active = db.Column(db.Boolean, default=False, nullable=False)
    product_subcategories = relationship("ProductSubcategory", order_by=ProductSubcategory.name, back_populates="product_category")
    products = relationship("Product", order_by=Product.title, back_populates="category")

    sort_method_map = SortMethodMap([
        (R.id.SORT_METHOD_ID, R.string.id, asc("id")),
        (R.id.SORT_METHOD_NAME, R.string.category_name, asc(name)),
        (R.id.SORT_METHOD_PRIORITY, R.string.priority, desc(priority)),
    ])

    def __repr__(self):
        return self.name

    @staticmethod
    def get_attrs_from_form(form):
        return dict(
            name=form.category_name.data,
            priority=int(form.priority.data),
            active=form.active.data
        )

    @staticmethod
    def get_choices(include_all, include_none=False, only_active=False):
        assert not (include_all and include_none)

        choices = []

        if include_all:
            choices.append((str(0), R.string.all))

        if include_none:
            choices.append((str(0), R.string.none_in_female))

        for category in ProductCategory.query.order_by(asc(ProductCategory.name)).all():
            if not only_active or (only_active and category.active):
                choices.append((str(category.id), category.name))

        return choices

    def disable(self):
        self.active = False
        db.session.add(self)
        db.session.commit()

    def to_activate(self):
        self.active = True
        db.session.add(self)
        db.session.commit()

    def get_n_active_products(self):
        n = 0
        for product in self.products:
            if product.active:
                n += 1
        return n
