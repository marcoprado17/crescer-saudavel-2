# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from markupsafe import Markup
from sqlalchemy.orm import relationship
from models.base import BaseModel
from models.product.product import Product
from models.product.product_subcategory import ProductSubcategory
from proj_extensions import db
from r import R


class ProductCategory(BaseModel):
    __tablename__ = "product_category"

    name = db.Column(db.String(R.dimen.product_category_name_max_length), nullable=False)
    priority = db.Column(db.Integer, default=R.dimen.default_product_category_priority, nullable=False)
    active = db.Column(db.Boolean, default=False, nullable=False)
    icon_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)
    product_subcategories = relationship("ProductSubcategory", order_by=ProductSubcategory.name,
                                         back_populates="product_category")
    products = relationship("Product", order_by=Product.title, back_populates="category")

    def __repr__(self):
        return Markup("<b><searchable>#%s</searchable></b> | <searchable>%s</searchable>" % (self.id, self.name))

    # TODO: Get the correct href
    def get_href(self):
        return "#"

    def has_active_subcategory(self):
        has_active_subcategory = ProductSubcategory.query.filter(ProductSubcategory.product_category_id == self.id)\
                   .filter(ProductSubcategory.active == True).count() > 0
        return has_active_subcategory

    def get_menu_icon_image_src(self):
        return self.get_img_src(self.icon_filename, R.string.default_menu_icon_filename)

    def has_menu_icon_image(self):
        return self.has_image(self.icon_filename)
