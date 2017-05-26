# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from markupsafe import Markup
from sqlalchemy.orm import relationship
from models.associations import home_content_more_categories_section_category_1_association_table, \
    home_content_more_categories_section_category_2_association_table, \
    home_content_more_categories_section_category_3_association_table, \
    home_content_more_categories_section_category_4_association_table, \
    home_content_more_categories_section_category_5_association_table, \
    home_content_more_categories_section_category_6_association_table
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
    product_subcategories = relationship("ProductSubcategory", order_by=ProductSubcategory.name,
                                         back_populates="product_category")
    products = relationship("Product", order_by=Product.title, back_populates="category")

    home_content_more_categories_section_category_1 = \
        relationship("HomeContent",
                     secondary=home_content_more_categories_section_category_1_association_table,
                     back_populates="more_categories_section_category_1")
    home_content_more_categories_section_category_2 = \
        relationship("HomeContent",
                     secondary=home_content_more_categories_section_category_2_association_table,
                     back_populates="more_categories_section_category_2")
    home_content_more_categories_section_category_3 = \
        relationship("HomeContent",
                     secondary=home_content_more_categories_section_category_3_association_table,
                     back_populates="more_categories_section_category_3")
    home_content_more_categories_section_category_4 = \
        relationship("HomeContent",
                     secondary=home_content_more_categories_section_category_4_association_table,
                     back_populates="more_categories_section_category_4")
    home_content_more_categories_section_category_5 = \
        relationship("HomeContent",
                     secondary=home_content_more_categories_section_category_5_association_table,
                     back_populates="more_categories_section_category_5")
    home_content_more_categories_section_category_6 = \
        relationship("HomeContent",
                     secondary=home_content_more_categories_section_category_6_association_table,
                     back_populates="more_categories_section_category_6")

    def __repr__(self):
        s = ""
        s += "<b><searchable>#%s</searchable></b> | <searchable>%s</searchable>" % (self.id, self.name)
        return Markup(s)
