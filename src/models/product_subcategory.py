# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from extensions import db
from models.product import Product


class ProductSubcategory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    active = db.Column(db.Boolean, default=True, nullable=False)
    name = db.Column(db.String(64))
    category_id = db.Column(db.Integer, ForeignKey("product_category.id"))
    category = relationship("ProductCategory", back_populates="subcategories")
    products = relationship("Product", order_by=Product.title, back_populates="subcategory")

    @staticmethod
    def create_from_form(add_product_subcategory_form):
        product_subcategory = ProductSubcategory(
            name=add_product_subcategory_form.subcategory_name.data,
            active=add_product_subcategory_form.active.data,
            category_id=int(add_product_subcategory_form.category.data)
        )
        db.session.add(product_subcategory)
        db.session.commit()
