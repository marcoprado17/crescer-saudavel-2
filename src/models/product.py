# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from decimal import Decimal

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from extensions import db
from r import R


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(R.dimen.product_title_max_length), nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)
    category_id = db.Column(db.Integer, ForeignKey("product_category.id"), nullable=False)
    category = relationship("ProductCategory", back_populates="products")
    subcategory_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    subcategory = relationship("ProductSubcategory", back_populates="products")
    price = db.Column(db.Numeric(precision=12, scale=2), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    min_stock = db.Column(db.Integer, nullable=False)
    summary = db.Column(db.UnicodeText, nullable=False)
    sales_number = db.Column(db.Integer, default=0)

    image_1 = db.Column(db.Text, nullable=False)
    image_2 = db.Column(db.Text)
    image_3 = db.Column(db.Text)
    image_4 = db.Column(db.Text)
    image_5 = db.Column(db.Text)
    image_6 = db.Column(db.Text)
    image_7 = db.Column(db.Text)
    image_8 = db.Column(db.Text)
    image_9 = db.Column(db.Text)
    image_10 = db.Column(db.Text)

    tab_1_title = db.Column(db.String(R.dimen.tab_title_max_length))
    tab_1_content = db.Column(db.UnicodeText)
    tab_2_title = db.Column(db.String(R.dimen.tab_title_max_length))
    tab_2_content = db.Column(db.UnicodeText)
    tab_3_title = db.Column(db.String(R.dimen.tab_title_max_length))
    tab_3_content = db.Column(db.UnicodeText)
    tab_4_title = db.Column(db.String(R.dimen.tab_title_max_length))
    tab_4_content = db.Column(db.UnicodeText)
    tab_5_title = db.Column(db.String(R.dimen.tab_title_max_length))
    tab_5_content = db.Column(db.UnicodeText)
    tab_6_title = db.Column(db.String(R.dimen.tab_title_max_length))
    tab_6_content = db.Column(db.UnicodeText)
    tab_7_title = db.Column(db.String(R.dimen.tab_title_max_length))
    tab_7_content = db.Column(db.UnicodeText)
    tab_8_title = db.Column(db.String(R.dimen.tab_title_max_length))
    tab_8_content = db.Column(db.UnicodeText)
    tab_9_title = db.Column(db.String(R.dimen.tab_title_max_length))
    tab_9_content = db.Column(db.UnicodeText)
    tab_10_title = db.Column(db.String(R.dimen.tab_title_max_length))
    tab_10_content = db.Column(db.UnicodeText)

    @staticmethod
    def create_from_form(add_product_form):
        product = Product(
            title=add_product_form.title.data,
            active=add_product_form.active.data,
            category_id=int(add_product_form.category_id.data),
            subcategory_id=int(add_product_form.subcategory_id.data) if int(add_product_form.subcategory_id.data) != 0 else None,
            price=Decimal(add_product_form.price.data.replace(',', '.')),
            stock=int(add_product_form.stock.data),
            min_stock=int(add_product_form.min_stock.data),
            summary=add_product_form.summary.data,

            image_1=add_product_form.image_1.data,
            image_2=add_product_form.image_2.data,
            image_3=add_product_form.image_3.data,
            image_4=add_product_form.image_4.data,
            image_5=add_product_form.image_5.data,
            image_6=add_product_form.image_6.data,
            image_7=add_product_form.image_7.data,
            image_8=add_product_form.image_8.data,
            image_9=add_product_form.image_9.data,
            image_10=add_product_form.image_10.data,

            tab_1_title=add_product_form.tab_1_title.data,
            tab_1_content=add_product_form.tab_1_content.data,
            tab_2_title=add_product_form.tab_2_title.data,
            tab_2_content=add_product_form.tab_2_content.data,
            tab_3_title=add_product_form.tab_3_title.data,
            tab_3_content=add_product_form.tab_3_content.data,
            tab_4_title=add_product_form.tab_4_title.data,
            tab_4_content=add_product_form.tab_4_content.data,
            tab_5_title=add_product_form.tab_5_title.data,
            tab_5_content=add_product_form.tab_5_content.data,
            tab_6_title=add_product_form.tab_6_title.data,
            tab_6_content=add_product_form.tab_6_content.data,
            tab_7_title=add_product_form.tab_7_title.data,
            tab_7_content=add_product_form.tab_7_content.data,
            tab_8_title=add_product_form.tab_8_title.data,
            tab_8_content=add_product_form.tab_8_content.data,
            tab_9_title=add_product_form.tab_9_title.data,
            tab_9_content=add_product_form.tab_9_content.data,
            tab_10_title=add_product_form.tab_10_title.data,
            tab_10_content=add_product_form.tab_10_content.data,
        )
        db.session.add(product)
        db.session.commit()
