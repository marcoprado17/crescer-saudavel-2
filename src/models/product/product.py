# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from decimal import Decimal
from flask import url_for
from markupsafe import Markup
from sqlalchemy import ForeignKey, exists, false
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from models.base import BaseModel
from models.product.product_category import ProductCategory
from models.product.product_subcategory import ProductSubcategory
from proj_extensions import db
from r import R
from flask_bombril.utils.utils import clamp_integer
from sqlalchemy import case, and_
from sqlalchemy import func


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
        return self.get_img_src(self.get_image_n_filename(n), R.string.product_default_filename)

    def get_imgs_src(self):
        imgs_src = []
        for i in range(1, R.dimen.max_n_product_img + 1):
            if self.has_image(self.get_image_n_filename(i)):
                imgs_src.append(self.get_image_n_src(i))
        if len(imgs_src) == 0:
            imgs_src.append(self.get_image_n_src(1))
        return imgs_src

    def get_main_img_src(self):
        for i in range(1, R.dimen.max_n_product_img + 1):
            if self.has_image(self.get_image_n_filename(i)):
                return self.get_image_n_src(i)
        return self.get_image_n_src(1)

    def get_tab_n_active(self, n):
        return getattr(self, "tab_" + str(n) + "_active")

    def get_tab_n_title(self, n):
        return getattr(self, "tab_" + str(n) + "_title")

    def get_tab_n_content_html(self, n):
        return getattr(self, "tab_" + str(n) + "_content_html")

    def get_price(self, n_units=1):
        return n_units * self.price

    def get_price_with_discount(self, n_units=1):
        return n_units * self.price_with_discount

    def get_href(self):
        return url_for("products.product", **{R.string.product_id_arg_name: self.id})

    def get_active_tabs(self):
        active_tabs = []
        for i in range(1, R.dimen.max_n_product_tabs + 1):
            if self.get_tab_n_active(i):
                active_tabs.append(i)
        return active_tabs

    def has_active_tab(self):
        return len(self.get_active_tabs()) > 0

    def has_description(self):
        return self.summary_html

    @hybrid_property
    def price_with_discount(self):
        if not self.has_discount:
            return self.price
        discount_percentage = clamp_integer(self.discount_percentage, 0, 100)
        return (self.price * Decimal(str((100.0 - discount_percentage) / 100.0))).quantize(Decimal("0.01"))

    @price_with_discount.expression
    def price_with_discount(cls):
        discount_percentage = case([(cls.discount_percentage > 100,
            100)],
        else_=
            case([(cls.discount_percentage < 0,
                0)],
            else_=
                cls.discount_percentage))
        return case([(cls.has_discount,
                func.round(cls.price * ((100-discount_percentage)/100.0), 2))],
            else_=
                cls.price)

    @hybrid_property
    def n_units_available(self):
        if self.stock is not None and self.reserved is not None:
            return self.stock - self.reserved
        else:
            return None

    @hybrid_property
    def is_available_to_client(self):
        if self.active is not None and self.n_units_available is not None and self.min_available is not None:
            if self.active is True and (self.n_units_available > self.min_available):
                if self.category is not None:
                    if self.subcategory is not None:
                        return self.subcategory.active and self.category.active
                    else:
                        return self.category.active
                else:
                    return True
            else:
                return False
        else:
            return False

    @is_available_to_client.expression
    def is_available_to_client(cls):
        return \
            case([(exists().where(and_(
                ProductCategory.id == cls.category_id,
                ProductCategory.active == False)),
                   False)],
                else_=
                case([(exists().where(and_(
                    ProductSubcategory.id == cls.subcategory_id,
                    ProductSubcategory.active == False)),
                       False)],
                    else_=
                    and_(cls.active, (cls.n_units_available > cls.min_available))))

    @hybrid_property
    def category_active(self):
        return self.category.active

    @category_active.expression
    def category_active(cls):
        return \
            case([(exists().where(and_(
                ProductCategory.id == cls.category_id,
                ProductCategory.active == False)),
                   False)],
                else_=
                True)

    @hybrid_property
    def subcategory_active(self):
        if self.subcategory is not None:
            return self.subcategory.active
        return True

    @subcategory_active.expression
    def subcategory_active(cls):
        return \
            case([(exists().where(and_(
                ProductSubcategory.id == cls.subcategory_id,
                ProductSubcategory.active == False)),
                   False)],
                else_=
                True)
