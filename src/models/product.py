# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from decimal import Decimal

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from extensions import db
from proj_exceptions import InvalidIdError
from r import R
from wrappers.base.utils import parse_markdown


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(R.dimen.product_title_max_length), nullable=False)
    active = db.Column(db.Boolean, default=False, nullable=False)
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
    def get_attrs_from_form(product_form):
        return dict(
            title=product_form.title.data,
            active=product_form.active.data,
            category_id=int(product_form.category_id.data),
            subcategory_id=int(product_form.subcategory_id.data) if int(product_form.subcategory_id.data) != 0 else None,
            price=Decimal(product_form.price.data.replace(',', '.')),
            stock=int(product_form.stock.data),
            min_stock=int(product_form.min_stock.data),
            summary=parse_markdown(product_form.summary.data),

            image_1=product_form.image_1.data,
            image_2=product_form.image_2.data,
            image_3=product_form.image_3.data,
            image_4=product_form.image_4.data,
            image_5=product_form.image_5.data,
            image_6=product_form.image_6.data,
            image_7=product_form.image_7.data,
            image_8=product_form.image_8.data,
            image_9=product_form.image_9.data,
            image_10=product_form.image_10.data,

            tab_1_title=product_form.tab_1_title.data,
            tab_1_content=parse_markdown(product_form.tab_1_content.data),
            tab_2_title=product_form.tab_2_title.data,
            tab_2_content=parse_markdown(product_form.tab_2_content.data),
            tab_3_title=product_form.tab_3_title.data,
            tab_3_content=parse_markdown(product_form.tab_3_content.data),
            tab_4_title=product_form.tab_4_title.data,
            tab_4_content=parse_markdown(product_form.tab_4_content.data),
            tab_5_title=product_form.tab_5_title.data,
            tab_5_content=parse_markdown(product_form.tab_5_content.data),
            tab_6_title=product_form.tab_6_title.data,
            tab_6_content=parse_markdown(product_form.tab_6_content.data),
            tab_7_title=product_form.tab_7_title.data,
            tab_7_content=parse_markdown(product_form.tab_7_content.data),
            tab_8_title=product_form.tab_8_title.data,
            tab_8_content=parse_markdown(product_form.tab_8_content.data),
            tab_9_title=product_form.tab_9_title.data,
            tab_9_content=parse_markdown(product_form.tab_9_content.data),
            tab_10_title=product_form.tab_10_title.data,
            tab_10_content=parse_markdown(product_form.tab_10_content.data)
        )

    @staticmethod
    def create_from_form(product_form):
        product = Product(
            **Product.get_attrs_from_form(product_form)
        )
        db.session.add(product)
        db.session.commit()

    @staticmethod
    def update_from_form(product, product_form):
        attrs_dict = Product.get_attrs_from_form(product_form)
        for key, val in attrs_dict.iteritems():
            setattr(product, key, val)
        db.session.add(product)
        db.session.commit()

    @staticmethod
    def set_active_value(product_id, active):
        product = Product.query.filter_by(id=product_id).one_or_none()
        if not product:
            raise InvalidIdError
        product.active = active
        db.session.add(product)
        db.session.commit()

    @staticmethod
    def add_to_stock(product_id, value):
        product = Product.query.filter_by(id=product_id).one_or_none()
        if not product:
            raise InvalidIdError
        product.stock += value
        db.session.add(product)
        db.session.commit()
        return product.stock

    @staticmethod
    def remove_from_stock(product_id, value):
        product = Product.query.filter_by(id=product_id).one_or_none()
        if not product:
            raise InvalidIdError
        product.stock = max(product.stock - value, 0)
        db.session.add(product)
        db.session.commit()
        return product.stock

    @staticmethod
    def update_stock(product_id, value):
        product = Product.query.filter_by(id=product_id).one_or_none()
        if not product:
            raise InvalidIdError
        product.stock = value
        db.session.add(product)
        db.session.commit()
        return product.stock

    @staticmethod
    def get(product_id):
        return Product.query.filter_by(id=product_id).one_or_none()

    def get_price(self, n_units=1):
        assert isinstance(n_units, int)
        assert n_units >= 0
        return self.price * Decimal(str(n_units))

    def get_formatted_price(self, n_units=1):
        return str(self.get_price(n_units=n_units)).replace(".", ",")

    @staticmethod
    def get_choices(include_none=False):
        product_choices = []
        if include_none:
            product_choices = [(str(0), R.string.none_in_masculine)]

        for id_title in Product.query.order_by(Product.title).with_entities(Product.id, Product.title).all():
            product_choices.append((str(id_title[0]), id_title[1]))

        return product_choices
