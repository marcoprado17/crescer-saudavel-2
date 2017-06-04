# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from decimal import Decimal
from markupsafe import Markup
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.base import BaseModel
from proj_extensions import db
from r import R
from os.path import join, isfile
from configs import default_app_config as config
from flask_bombril.utils.utils import clamp_integer


class Product(BaseModel):
    __tablename__ = "product"

    __searchable__ = [
        "title",
        "summary_html",
        "tab_1_content_html",
        "tab_2_content_html",
        "tab_3_content_html",
        "tab_4_content_html",
        "tab_5_content_html",
    ]

    title = db.Column(db.String(R.dimen.product_title_max_length), nullable=False)
    active = db.Column(db.Boolean, default=False, nullable=False)
    category_id = db.Column(db.Integer, ForeignKey("product_category.id"), nullable=False)
    category = relationship("ProductCategory", back_populates="products")
    subcategory_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    subcategory = relationship("ProductSubcategory", back_populates="products")
    price = db.Column(db.Numeric(precision=12, scale=2), nullable=False)
    has_discount = db.Column(db.Boolean, default=False, nullable=False)
    discount_percentage = db.Column(db.Integer, default=0, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    reserved = db.Column(db.Integer, default=0, nullable=False)
    min_available = db.Column(db.Integer, nullable=False)
    summary_markdown = db.Column(db.UnicodeText, nullable=False, default="")
    summary_html = db.Column(db.UnicodeText, nullable=False, default="")
    sales_number = db.Column(db.Integer, default=0)

    image_1_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)
    image_2_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)
    image_3_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)
    image_4_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)

    tab_1_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_1_title = db.Column(db.String(R.dimen.tab_title_max_length), default="", nullable=False)
    tab_1_content_markdown = db.Column(db.UnicodeText, default="", nullable=False)
    tab_1_content_html = db.Column(db.UnicodeText, default="", nullable=False)

    tab_2_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_2_title = db.Column(db.String(R.dimen.tab_title_max_length), default="", nullable=False)
    tab_2_content_markdown = db.Column(db.UnicodeText, default="", nullable=False)
    tab_2_content_html = db.Column(db.UnicodeText, default="", nullable=False)

    tab_3_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_3_title = db.Column(db.String(R.dimen.tab_title_max_length), default="", nullable=False)
    tab_3_content_markdown = db.Column(db.UnicodeText, default="", nullable=False)
    tab_3_content_html = db.Column(db.UnicodeText, default="", nullable=False)

    tab_4_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_4_title = db.Column(db.String(R.dimen.tab_title_max_length), default="", nullable=False)
    tab_4_content_markdown = db.Column(db.UnicodeText, default="", nullable=False)
    tab_4_content_html = db.Column(db.UnicodeText, default="", nullable=False)

    tab_5_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_5_title = db.Column(db.String(R.dimen.tab_title_max_length), default="", nullable=False)
    tab_5_content_markdown = db.Column(db.UnicodeText, default="", nullable=False)
    tab_5_content_html = db.Column(db.UnicodeText, default="", nullable=False)

    def __repr__(self):
        html = [
            "<table>",
            "   <tr>",
            "       <td style='vertical-align: top;'><img src='%s' style='max-width: 48px;'></td>",
            "       <td style='padding-left: 4px;'>",
            "           <b><searchable>#%s</searchable></b><br><searchable>%s</searchable>"
            "       </td>"
            "   </tr>",
            "</table>"
        ]
        return Markup(''.join(html) % (self.get_image_n_src(1), self.id, self.title))

    def get_image_n_filename(self, n):
        return getattr(self, "image_" + str(n) + "_filename")

    def get_image_n_src(self, n):
        return self.get_image_src(self.get_image_n_filename(n), R.string.product_default_filename)

    def get_tab_n_active(self, n):
        return getattr(self, "tab_" + str(n) + "_active")

    def get_tab_n_title(self, n):
        return getattr(self, "tab_" + str(n) + "_title")

    def get_tab_n_content_html(self, n):
        return getattr(self, "tab_" + str(n) + "_content_html")

    def get_price_with_discount(self):
        if not self.has_discount:
            return None
        return Product.calculate_price_with_discount(price=self.price, discount_percentage=self.discount_percentage)

    def get_price(self, n_units):
        return n_units*self.price

    @staticmethod
    def calculate_price_with_discount(price, discount_percentage):
        return (price * Decimal(str((100.0 - clamp_integer(discount_percentage, 0, 100)) / 100.0))).quantize(
            Decimal("0.01"))

    def get_n_units_available(self):
        if self.stock is not None and self.reserved is not None:
            return self.stock - self.reserved
        else:
            return None

    def is_available_to_client(self):
        n_units_available = self.get_n_units_available()
        if self.active is not None and n_units_available is not None and self.min_available is not None:
            if self.active is True and (n_units_available > self.min_available):
                return True
            else:
                return False
        else:
            return None
