# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from decimal import Decimal

from sqlalchemy import ForeignKey
from sqlalchemy import asc
from sqlalchemy import desc
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from extensions import db
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
    _stock = db.Column(db.Integer, nullable=False)
    _available = db.Column(db.Integer, nullable=False)
    _reserved = db.Column(db.Integer, default=0, nullable=False)
    min_available = db.Column(db.Integer, nullable=False)
    summary = db.Column(db.UnicodeText, nullable=False)
    sales_number = db.Column(db.Integer, default=0)

    image_1 = db.Column(db.Text)
    image_2 = db.Column(db.Text)
    image_3 = db.Column(db.Text)
    image_4 = db.Column(db.Text)
    image_5 = db.Column(db.Text)
    image_6 = db.Column(db.Text)
    image_7 = db.Column(db.Text)
    image_8 = db.Column(db.Text)
    image_9 = db.Column(db.Text)
    image_10 = db.Column(db.Text)

    tab_1_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_1_title = db.Column(db.String(R.dimen.tab_title_max_length))
    tab_1_content = db.Column(db.UnicodeText)
    tab_2_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_2_title = db.Column(db.String(R.dimen.tab_title_max_length))
    tab_2_content = db.Column(db.UnicodeText)
    tab_3_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_3_title = db.Column(db.String(R.dimen.tab_title_max_length))
    tab_3_content = db.Column(db.UnicodeText)
    tab_4_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_4_title = db.Column(db.String(R.dimen.tab_title_max_length))
    tab_4_content = db.Column(db.UnicodeText)
    tab_5_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_5_title = db.Column(db.String(R.dimen.tab_title_max_length))
    tab_5_content = db.Column(db.UnicodeText)
    tab_6_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_6_title = db.Column(db.String(R.dimen.tab_title_max_length))
    tab_6_content = db.Column(db.UnicodeText)
    tab_7_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_7_title = db.Column(db.String(R.dimen.tab_title_max_length))
    tab_7_content = db.Column(db.UnicodeText)
    tab_8_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_8_title = db.Column(db.String(R.dimen.tab_title_max_length))
    tab_8_content = db.Column(db.UnicodeText)
    tab_9_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_9_title = db.Column(db.String(R.dimen.tab_title_max_length))
    tab_9_content = db.Column(db.UnicodeText)
    tab_10_active = db.Column(db.Boolean, default=False, nullable=False)
    tab_10_title = db.Column(db.String(R.dimen.tab_title_max_length))
    tab_10_content = db.Column(db.UnicodeText)

    @hybrid_property
    def available(self):
        return self._available

    @hybrid_property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, new_stock):
        self._stock = new_stock
        self.update_available()

    @hybrid_property
    def reserved(self):
        return self._reserved

    @reserved.setter
    def reserved(self, new_reserved):
        self._reserved = new_reserved
        self.update_available()

    def update_available(self):
        if self._reserved == None:
            self._reserved = 0
        self._available = self._stock - self._reserved

    sort_method_ids = [
        R.id.SORT_METHOD_ID,
        R.id.SORT_METHOD_TITLE,
        R.id.SORT_METHOD_LOWEST_PRICE,
        R.id.SORT_METHOD_HIGHER_PRICE,
        R.id.SORT_METHOD_LOWEST_STOCK,
        R.id.SORT_METHOD_HIGHER_STOCK,
        R.id.SORT_METHOD_LOWEST_AVAILABLE,
        R.id.SORT_METHOD_HIGHER_AVAILABLE,
        R.id.SORT_METHOD_LOWEST_RESERVED,
        R.id.SORT_METHOD_HIGHER_RESERVED,
        R.id.SORT_METHOD_BEST_SELLER,
        R.id.SORT_METHOD_LESS_SOLD
    ]
    sort_method_names = [
        R.string.id,
        R.string.title,
        R.string.lowest_price,
        R.string.higher_price,
        R.string.lowest_stock,
        R.string.higher_stock,
        R.string.lowest_available,
        R.string.higher_available,
        R.string.lowest_reserved,
        R.string.higher_reserved,
        R.string.best_seller,
        R.string.less_sold
    ]
    sort_method_by_id = {
        R.id.SORT_METHOD_ID: asc(id),
        R.id.SORT_METHOD_TITLE: asc(title),
        R.id.SORT_METHOD_LOWEST_PRICE: asc(price),
        R.id.SORT_METHOD_HIGHER_PRICE: desc(price),
        R.id.SORT_METHOD_LOWEST_STOCK: asc(_stock),
        R.id.SORT_METHOD_HIGHER_STOCK: desc(_stock),
        R.id.SORT_METHOD_LOWEST_AVAILABLE: asc(_available),
        R.id.SORT_METHOD_HIGHER_AVAILABLE: desc(_available),
        R.id.SORT_METHOD_LOWEST_RESERVED: asc(_reserved),
        R.id.SORT_METHOD_HIGHER_RESERVED: desc(_reserved),
        R.id.SORT_METHOD_BEST_SELLER: desc(sales_number),
        R.id.SORT_METHOD_LESS_SOLD: asc(sales_number)
    }

    @staticmethod
    def get_attrs_from_form(product_form):
        return dict(
            title=product_form.title.data,
            active=product_form.active.data,
            category_id=int(product_form.category_id.data),
            subcategory_id=int(product_form.subcategory_id.data) if int(product_form.subcategory_id.data) != 0 else None,
            price=Decimal(product_form.price.data.replace(',', '.')),
            stock=int(product_form.stock.data),
            min_available=int(product_form.min_available.data),
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

            tab_1_active=product_form.tab_1_active.data,
            tab_1_title=product_form.tab_1_title.data,
            tab_1_content=parse_markdown(product_form.tab_1_content.data),
            tab_2_active=product_form.tab_2_active.data,
            tab_2_title=product_form.tab_2_title.data,
            tab_2_content=parse_markdown(product_form.tab_2_content.data),
            tab_3_active=product_form.tab_3_active.data,
            tab_3_title=product_form.tab_3_title.data,
            tab_3_content=parse_markdown(product_form.tab_3_content.data),
            tab_4_active=product_form.tab_4_active.data,
            tab_4_title=product_form.tab_4_title.data,
            tab_4_content=parse_markdown(product_form.tab_4_content.data),
            tab_5_active=product_form.tab_5_active.data,
            tab_5_title=product_form.tab_5_title.data,
            tab_5_content=parse_markdown(product_form.tab_5_content.data),
            tab_6_active=product_form.tab_6_active.data,
            tab_6_title=product_form.tab_6_title.data,
            tab_6_content=parse_markdown(product_form.tab_6_content.data),
            tab_7_active=product_form.tab_7_active.data,
            tab_7_title=product_form.tab_7_title.data,
            tab_7_content=parse_markdown(product_form.tab_7_content.data),
            tab_8_active=product_form.tab_8_active.data,
            tab_8_title=product_form.tab_8_title.data,
            tab_8_content=parse_markdown(product_form.tab_8_content.data),
            tab_9_active=product_form.tab_9_active.data,
            tab_9_title=product_form.tab_9_title.data,
            tab_9_content=parse_markdown(product_form.tab_9_content.data),
            tab_10_active=product_form.tab_10_active.data,
            tab_10_title=product_form.tab_10_title.data,
            tab_10_content=parse_markdown(product_form.tab_10_content.data)
        )

    @staticmethod
    def create_from_form(product_form):
        product = Product(
            **Product.get_attrs_from_form(product_form)
        )
        product.available = product.stock.data
        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def update_from_form(product, product_form):
        attrs_dict = Product.get_attrs_from_form(product_form)
        for key, val in attrs_dict.iteritems():
            setattr(product, key, val)
        db.session.add(product)
        db.session.commit()

    @staticmethod
    def update(product_id, **kw):
        product = Product.get(product_id)
        assert product != None
        for key, val in kw.iteritems():
            setattr(product, key, val)
        db.session.add(product)
        db.session.commit()
        return product

    def add_to_stock(self, value):
        self.stock += value
        db.session.add(self)
        db.session.commit()

    def remove_from_stock(self, value):
        self.stock -= value
        assert self.stock >= 0
        db.session.add(self)
        db.session.commit()

    def update_stock(self, value):
        self.stock = value
        assert self.stock >= 0
        db.session.add(self)
        db.session.commit()

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
