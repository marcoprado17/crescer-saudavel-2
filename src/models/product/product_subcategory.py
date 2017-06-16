# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import url_for
from markupsafe import Markup
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from proj_extensions import db
from models.base import BaseModel
from r import R


class ProductSubcategory(BaseModel):
    __tablename__ = "product_subcategory"

    name = db.Column(db.String(R.dimen.product_subcategory_name_max_length), nullable=False)
    active = db.Column(db.Boolean, default=False, nullable=False)
    product_category_id = db.Column(db.Integer, ForeignKey("product_category.id"), nullable=False)
    product_category = relationship("ProductCategory", back_populates="product_subcategories")
    products = relationship("Product", back_populates="subcategory")

    def __repr__(self):
        return Markup("<b><searchable>#%s</searchable></b> | <searchable>%s</searchable>" % (self.id, self.name))

    def get_href(self):
        return url_for("products.products", **{R.string.subcategory_id_arg_name: self.id})
