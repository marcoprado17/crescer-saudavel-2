# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from sqlalchemy import ForeignKey
from sqlalchemy import asc
from sqlalchemy.orm import relationship

from flask_bombril.utils.utils import merge_dicts
from proj_extensions import db
from models.base import BaseModel, ProjBaseView
from models.product import Product
from proj_utils import SortMethodMap
from r import R


class ProductSubcategoryView(ProjBaseView):
    column_labels = merge_dicts(ProjBaseView.column_labels, dict(active=R.string.active_in_female))
    column_list = ['active', 'name', 'product_category']
    column_filters = ['active', 'product_category']
    column_editable_list = ['name', 'product_category', 'active']
    form_excluded_columns = ['products']

    def __init__(self, *args, **kwargs):
        kwargs["name"] = R.string.product_subcategories
        kwargs["endpoint"] = R.string.product_subcategories.lower().replace(' ', '-')
        kwargs["category"] = R.string.products
        super(ProductSubcategoryView, self).__init__(*args, **kwargs)


class ProductSubcategory(BaseModel):
    __tablename__ = "product_subcategory"

    name = db.Column(db.String(R.dimen.product_subcategory_name_max_length), nullable=False)
    active = db.Column(db.Boolean, default=False, nullable=False)
    product_category_id = db.Column(db.Integer, ForeignKey("product_category.id"), nullable=False)
    product_category = relationship("ProductCategory", back_populates="product_subcategories")
    products = relationship("Product", order_by=Product.title, back_populates="subcategory")

    sort_method_map = SortMethodMap([
        (R.id.SORT_METHOD_ID, R.string.id, asc("id")),
        (R.id.SORT_METHOD_NAME, R.string.category_name, asc(name)),
    ])

    def __repr__(self):
        return self.name

    @staticmethod
    def get_attrs_from_form(form):
        return dict(
            category_id=form.category_id.data,
            name=form.subcategory_name.data,
            active=form.active.data,
        )

    @staticmethod
    def get_choices(include_all=False, include_none=False, only_active=False):
        assert not(include_all and include_none)

        choices = []

        if include_all:
            choices.append((str(0), R.string.all))
        if include_none:
            choices.append((str(0), R.string.none_in_female))

        for subcategory in ProductSubcategory.query.order_by(asc(ProductSubcategory.name)).all():
            if not only_active or (only_active and subcategory.active):
                choices.append((str(subcategory.id), subcategory.name))

        return choices

    def disable(self):
        self.active = False
        db.session.add(self)
        db.session.commit()

    def to_activate(self):
        self.active = True
        db.session.add(self)
        db.session.commit()
