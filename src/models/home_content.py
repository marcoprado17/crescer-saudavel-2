# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 13/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import url_for
from sqlalchemy import ForeignKey

from models.base import BaseModel
from models.blog.blog_post import BlogPost
from models.product import Product
from proj_exceptions import InconsistentDataBaseError
from proj_extensions import db
from proj_utils import safe_id
from r import R


class HomeContent(BaseModel):
    __tablename__ = "home_content"

    carousel_item_1_active = db.Column(db.Boolean, default=False, nullable=False)
    carousel_item_1_title = db.Column(db.String(R.dimen.carousel_title_max_length), default="", nullable=False)
    carousel_item_1_subtitle = db.Column(db.String(R.dimen.carousel_subtitle_max_length), default="", nullable=False)
    carousel_item_1_link = db.Column(db.String(R.dimen.link_max_length), default="", nullable=False)
    carousel_item_1_image = db.Column(db.Text, default="", nullable=False)

    carousel_item_2_active = db.Column(db.Boolean, default=False, nullable=False)
    carousel_item_2_title = db.Column(db.String(R.dimen.carousel_title_max_length))
    carousel_item_2_subtitle = db.Column(db.String(R.dimen.carousel_subtitle_max_length))
    carousel_item_2_link = db.Column(db.String(R.dimen.link_max_length), default="", nullable=False)
    carousel_item_2_image = db.Column(db.Text, default="", nullable=False)

    carousel_item_3_active = db.Column(db.Boolean, default=False, nullable=False)
    carousel_item_3_title = db.Column(db.String(R.dimen.carousel_title_max_length))
    carousel_item_3_subtitle = db.Column(db.String(R.dimen.carousel_subtitle_max_length))
    carousel_item_3_link = db.Column(db.String(R.dimen.link_max_length), default="", nullable=False)
    carousel_item_3_image = db.Column(db.Text, default="", nullable=False)

    product_section_1_active = db.Column(db.Boolean, default=False, nullable=False)
    product_section_1_name = db.Column(db.String(R.dimen.product_section_name_max_length), default="", nullable=False)
    product_section_1_link = db.Column(db.String(R.dimen.link_max_length), default="", nullable=False)
    product_section_1_product_1_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_1_product_2_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_1_product_3_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_1_product_4_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_1_product_5_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_1_product_6_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_1_product_7_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_1_product_8_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_1_product_9_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_1_product_10_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_1_product_11_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_1_product_12_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_1_product_13_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_1_product_14_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_1_product_15_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_1_product_16_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_1_product_17_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_1_product_18_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_1_product_19_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_1_product_20_id = db.Column(db.Integer, ForeignKey("product.id"))

    product_section_2_active = db.Column(db.Boolean, default=False, nullable=False)
    product_section_2_name = db.Column(db.String(R.dimen.product_section_name_max_length), default="", nullable=False)
    product_section_2_link = db.Column(db.String(R.dimen.link_max_length), default="", nullable=False)
    product_section_2_product_1_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_2_product_2_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_2_product_3_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_2_product_4_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_2_product_5_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_2_product_6_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_2_product_7_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_2_product_8_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_2_product_9_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_2_product_10_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_2_product_11_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_2_product_12_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_2_product_13_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_2_product_14_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_2_product_15_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_2_product_16_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_2_product_17_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_2_product_18_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_2_product_19_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_2_product_20_id = db.Column(db.Integer, ForeignKey("product.id"))

    product_section_3_active = db.Column(db.Boolean, default=False, nullable=False)
    product_section_3_name = db.Column(db.String(R.dimen.product_section_name_max_length), default="", nullable=False)
    product_section_3_link = db.Column(db.String(R.dimen.link_max_length), default="", nullable=False)
    product_section_3_product_1_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_3_product_2_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_3_product_3_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_3_product_4_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_3_product_5_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_3_product_6_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_3_product_7_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_3_product_8_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_3_product_9_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_3_product_10_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_3_product_11_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_3_product_12_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_3_product_13_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_3_product_14_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_3_product_15_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_3_product_16_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_3_product_17_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_3_product_18_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_3_product_19_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_3_product_20_id = db.Column(db.Integer, ForeignKey("product.id"))

    product_section_4_active = db.Column(db.Boolean, default=False, nullable=False)
    product_section_4_name = db.Column(db.String(R.dimen.product_section_name_max_length), default="", nullable=False)
    product_section_4_link = db.Column(db.String(R.dimen.link_max_length), default="", nullable=False)
    product_section_4_product_1_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_4_product_2_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_4_product_3_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_4_product_4_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_4_product_5_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_4_product_6_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_4_product_7_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_4_product_8_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_4_product_9_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_4_product_10_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_4_product_11_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_4_product_12_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_4_product_13_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_4_product_14_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_4_product_15_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_4_product_16_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_4_product_17_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_4_product_18_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_4_product_19_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_4_product_20_id = db.Column(db.Integer, ForeignKey("product.id"))

    product_section_5_active = db.Column(db.Boolean, default=False, nullable=False)
    product_section_5_name = db.Column(db.String(R.dimen.product_section_name_max_length), default="", nullable=False)
    product_section_5_link = db.Column(db.String(R.dimen.link_max_length), default="", nullable=False)
    product_section_5_product_1_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_5_product_2_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_5_product_3_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_5_product_4_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_5_product_5_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_5_product_6_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_5_product_7_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_5_product_8_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_5_product_9_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_5_product_10_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_5_product_11_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_5_product_12_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_5_product_13_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_5_product_14_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_5_product_15_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_5_product_16_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_5_product_17_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_5_product_18_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_5_product_19_id = db.Column(db.Integer, ForeignKey("product.id"))
    product_section_5_product_20_id = db.Column(db.Integer, ForeignKey("product.id"))

    more_categories_section_category_1_id = db.Column(db.Integer, ForeignKey("product_category.id"))
    more_categories_section_category_1_image = db.Column(db.Text)
    more_categories_section_subcategory_1_of_category_1_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    more_categories_section_subcategory_2_of_category_1_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    more_categories_section_subcategory_3_of_category_1_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    more_categories_section_subcategory_4_of_category_1_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    more_categories_section_subcategory_5_of_category_1_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))

    more_categories_section_category_2_id = db.Column(db.Integer, ForeignKey("product_category.id"))
    more_categories_section_category_2_image = db.Column(db.Text)
    more_categories_section_subcategory_1_of_category_2_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    more_categories_section_subcategory_2_of_category_2_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    more_categories_section_subcategory_3_of_category_2_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    more_categories_section_subcategory_4_of_category_2_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    more_categories_section_subcategory_5_of_category_2_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))

    more_categories_section_category_3_id = db.Column(db.Integer, ForeignKey("product_category.id"))
    more_categories_section_category_3_image = db.Column(db.Text)
    more_categories_section_subcategory_1_of_category_3_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    more_categories_section_subcategory_2_of_category_3_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    more_categories_section_subcategory_3_of_category_3_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    more_categories_section_subcategory_4_of_category_3_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    more_categories_section_subcategory_5_of_category_3_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))

    more_categories_section_category_4_id = db.Column(db.Integer, ForeignKey("product_category.id"))
    more_categories_section_category_4_image = db.Column(db.Text)
    more_categories_section_subcategory_1_of_category_4_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    more_categories_section_subcategory_2_of_category_4_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    more_categories_section_subcategory_3_of_category_4_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    more_categories_section_subcategory_4_of_category_4_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    more_categories_section_subcategory_5_of_category_4_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))

    more_categories_section_category_5_id = db.Column(db.Integer, ForeignKey("product_category.id"))
    more_categories_section_category_5_image = db.Column(db.Text)
    more_categories_section_subcategory_1_of_category_5_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    more_categories_section_subcategory_2_of_category_5_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    more_categories_section_subcategory_3_of_category_5_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    more_categories_section_subcategory_4_of_category_5_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    more_categories_section_subcategory_5_of_category_5_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))

    more_categories_section_category_6_id = db.Column(db.Integer, ForeignKey("product_category.id"))
    more_categories_section_category_6_image = db.Column(db.Text)
    more_categories_section_subcategory_1_of_category_6_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    more_categories_section_subcategory_2_of_category_6_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    more_categories_section_subcategory_3_of_category_6_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    more_categories_section_subcategory_4_of_category_6_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    more_categories_section_subcategory_5_of_category_6_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))

    blog_section_1_active = db.Column(db.Boolean, default=False, nullable=False)
    blog_section_1_name = db.Column(db.String(R.dimen.blog_section_name_max_length), default="", nullable=False)
    blog_section_1_link = db.Column(db.String(R.dimen.link_max_length), default="", nullable=False)
    blog_section_1_post_1_id = db.Column(db.Integer, ForeignKey("blog_post.id"))
    blog_section_1_post_2_id = db.Column(db.Integer, ForeignKey("blog_post.id"))

    blog_section_2_active = db.Column(db.Boolean, default=False, nullable=False)
    blog_section_2_name = db.Column(db.String(R.dimen.blog_section_name_max_length), default="", nullable=False)
    blog_section_2_link = db.Column(db.String(R.dimen.link_max_length), default="", nullable=False)
    blog_section_2_post_1_id = db.Column(db.Integer, ForeignKey("blog_post.id"))
    blog_section_2_post_2_id = db.Column(db.Integer, ForeignKey("blog_post.id"))

    blog_section_3_active = db.Column(db.Boolean, default=False, nullable=False)
    blog_section_3_name = db.Column(db.String(R.dimen.blog_section_name_max_length), default="", nullable=False)
    blog_section_3_link = db.Column(db.String(R.dimen.link_max_length), default="", nullable=False)
    blog_section_3_post_1_id = db.Column(db.Integer, ForeignKey("blog_post.id"))
    blog_section_3_post_2_id = db.Column(db.Integer, ForeignKey("blog_post.id"))

    @staticmethod
    def get():
        home_contents = HomeContent.query.all()
        if len(home_contents) != 1:
            raise InconsistentDataBaseError
        return home_contents[0]

    @staticmethod
    def set_carousel_1_values_from_form(carousel_form):
        home_content = HomeContent.get()
        home_content.carousel_item_1_active = carousel_form.active.data
        home_content.carousel_item_1_title = carousel_form.title.data
        home_content.carousel_item_1_subtitle = carousel_form.subtitle.data
        home_content.carousel_item_1_link = carousel_form.link.data
        home_content.carousel_item_1_image = carousel_form.image.data
        db.session.add(home_content)
        db.session.commit()

    @staticmethod
    def set_carousel_2_values_from_form(carousel_form):
        home_content = HomeContent.get()
        home_content.carousel_item_2_active = carousel_form.active.data
        home_content.carousel_item_2_title = carousel_form.title.data
        home_content.carousel_item_2_subtitle = carousel_form.subtitle.data
        home_content.carousel_item_2_link = carousel_form.link.data
        home_content.carousel_item_2_image = carousel_form.image.data
        db.session.add(home_content)
        db.session.commit()

    @staticmethod
    def set_carousel_3_values_from_form(carousel_form):
        home_content = HomeContent.get()
        home_content.carousel_item_3_active = carousel_form.active.data
        home_content.carousel_item_3_title = carousel_form.title.data
        home_content.carousel_item_3_subtitle = carousel_form.subtitle.data
        home_content.carousel_item_3_link = carousel_form.link.data
        home_content.carousel_item_3_image = carousel_form.image.data
        db.session.add(home_content)
        db.session.commit()

    @staticmethod
    def set_product_section_1_values_from_form(product_section_form):
        home_content = HomeContent.get()
        home_content.product_section_1_active = product_section_form.active.data
        home_content.product_section_1_name = product_section_form.name.data
        home_content.product_section_1_link = product_section_form.link.data
        home_content.product_section_1_product_1_id = safe_id(product_section_form.product_1_id.data)
        home_content.product_section_1_product_2_id = safe_id(product_section_form.product_2_id.data)
        home_content.product_section_1_product_3_id = safe_id(product_section_form.product_3_id.data)
        home_content.product_section_1_product_4_id = safe_id(product_section_form.product_4_id.data)
        home_content.product_section_1_product_5_id = safe_id(product_section_form.product_5_id.data)
        home_content.product_section_1_product_6_id = safe_id(product_section_form.product_6_id.data)
        home_content.product_section_1_product_7_id = safe_id(product_section_form.product_7_id.data)
        home_content.product_section_1_product_8_id = safe_id(product_section_form.product_8_id.data)
        home_content.product_section_1_product_9_id = safe_id(product_section_form.product_9_id.data)
        home_content.product_section_1_product_10_id = safe_id(product_section_form.product_10_id.data)
        home_content.product_section_1_product_11_id = safe_id(product_section_form.product_11_id.data)
        home_content.product_section_1_product_12_id = safe_id(product_section_form.product_12_id.data)
        home_content.product_section_1_product_13_id = safe_id(product_section_form.product_13_id.data)
        home_content.product_section_1_product_14_id = safe_id(product_section_form.product_14_id.data)
        home_content.product_section_1_product_15_id = safe_id(product_section_form.product_15_id.data)
        home_content.product_section_1_product_16_id = safe_id(product_section_form.product_16_id.data)
        home_content.product_section_1_product_17_id = safe_id(product_section_form.product_17_id.data)
        home_content.product_section_1_product_18_id = safe_id(product_section_form.product_18_id.data)
        home_content.product_section_1_product_19_id = safe_id(product_section_form.product_19_id.data)
        home_content.product_section_1_product_20_id = safe_id(product_section_form.product_20_id.data)
        db.session.add(home_content)
        db.session.commit()

    @staticmethod
    def set_product_section_2_values_from_form(product_section_form):
        home_content = HomeContent.get()
        home_content.product_section_2_active = product_section_form.active.data
        home_content.product_section_2_name = product_section_form.name.data
        home_content.product_section_2_link = product_section_form.link.data
        home_content.product_section_2_product_1_id = safe_id(product_section_form.product_1_id.data)
        home_content.product_section_2_product_2_id = safe_id(product_section_form.product_2_id.data)
        home_content.product_section_2_product_3_id = safe_id(product_section_form.product_3_id.data)
        home_content.product_section_2_product_4_id = safe_id(product_section_form.product_4_id.data)
        home_content.product_section_2_product_5_id = safe_id(product_section_form.product_5_id.data)
        home_content.product_section_2_product_6_id = safe_id(product_section_form.product_6_id.data)
        home_content.product_section_2_product_7_id = safe_id(product_section_form.product_7_id.data)
        home_content.product_section_2_product_8_id = safe_id(product_section_form.product_8_id.data)
        home_content.product_section_2_product_9_id = safe_id(product_section_form.product_9_id.data)
        home_content.product_section_2_product_10_id = safe_id(product_section_form.product_10_id.data)
        home_content.product_section_2_product_11_id = safe_id(product_section_form.product_11_id.data)
        home_content.product_section_2_product_12_id = safe_id(product_section_form.product_12_id.data)
        home_content.product_section_2_product_13_id = safe_id(product_section_form.product_13_id.data)
        home_content.product_section_2_product_14_id = safe_id(product_section_form.product_14_id.data)
        home_content.product_section_2_product_15_id = safe_id(product_section_form.product_15_id.data)
        home_content.product_section_2_product_16_id = safe_id(product_section_form.product_16_id.data)
        home_content.product_section_2_product_17_id = safe_id(product_section_form.product_17_id.data)
        home_content.product_section_2_product_18_id = safe_id(product_section_form.product_18_id.data)
        home_content.product_section_2_product_19_id = safe_id(product_section_form.product_19_id.data)
        home_content.product_section_2_product_20_id = safe_id(product_section_form.product_20_id.data)
        db.session.add(home_content)
        db.session.commit()

    @staticmethod
    def set_product_section_3_values_from_form(product_section_form):
        home_content = HomeContent.get()
        home_content.product_section_3_active = product_section_form.active.data
        home_content.product_section_3_name = product_section_form.name.data
        home_content.product_section_3_link = product_section_form.link.data
        home_content.product_section_3_product_1_id = safe_id(product_section_form.product_1_id.data)
        home_content.product_section_3_product_2_id = safe_id(product_section_form.product_2_id.data)
        home_content.product_section_3_product_3_id = safe_id(product_section_form.product_3_id.data)
        home_content.product_section_3_product_4_id = safe_id(product_section_form.product_4_id.data)
        home_content.product_section_3_product_5_id = safe_id(product_section_form.product_5_id.data)
        home_content.product_section_3_product_6_id = safe_id(product_section_form.product_6_id.data)
        home_content.product_section_3_product_7_id = safe_id(product_section_form.product_7_id.data)
        home_content.product_section_3_product_8_id = safe_id(product_section_form.product_8_id.data)
        home_content.product_section_3_product_9_id = safe_id(product_section_form.product_9_id.data)
        home_content.product_section_3_product_10_id = safe_id(product_section_form.product_10_id.data)
        home_content.product_section_3_product_11_id = safe_id(product_section_form.product_11_id.data)
        home_content.product_section_3_product_12_id = safe_id(product_section_form.product_12_id.data)
        home_content.product_section_3_product_13_id = safe_id(product_section_form.product_13_id.data)
        home_content.product_section_3_product_14_id = safe_id(product_section_form.product_14_id.data)
        home_content.product_section_3_product_15_id = safe_id(product_section_form.product_15_id.data)
        home_content.product_section_3_product_16_id = safe_id(product_section_form.product_16_id.data)
        home_content.product_section_3_product_17_id = safe_id(product_section_form.product_17_id.data)
        home_content.product_section_3_product_18_id = safe_id(product_section_form.product_18_id.data)
        home_content.product_section_3_product_19_id = safe_id(product_section_form.product_19_id.data)
        home_content.product_section_3_product_20_id = safe_id(product_section_form.product_20_id.data)
        db.session.add(home_content)
        db.session.commit()

    @staticmethod
    def set_product_section_4_values_from_form(product_section_form):
        home_content = HomeContent.get()
        home_content.product_section_4_active = product_section_form.active.data
        home_content.product_section_4_name = product_section_form.name.data
        home_content.product_section_4_link = product_section_form.link.data
        home_content.product_section_4_product_1_id = safe_id(product_section_form.product_1_id.data)
        home_content.product_section_4_product_2_id = safe_id(product_section_form.product_2_id.data)
        home_content.product_section_4_product_3_id = safe_id(product_section_form.product_3_id.data)
        home_content.product_section_4_product_4_id = safe_id(product_section_form.product_4_id.data)
        home_content.product_section_4_product_5_id = safe_id(product_section_form.product_5_id.data)
        home_content.product_section_4_product_6_id = safe_id(product_section_form.product_6_id.data)
        home_content.product_section_4_product_7_id = safe_id(product_section_form.product_7_id.data)
        home_content.product_section_4_product_8_id = safe_id(product_section_form.product_8_id.data)
        home_content.product_section_4_product_9_id = safe_id(product_section_form.product_9_id.data)
        home_content.product_section_4_product_10_id = safe_id(product_section_form.product_10_id.data)
        home_content.product_section_4_product_11_id = safe_id(product_section_form.product_11_id.data)
        home_content.product_section_4_product_12_id = safe_id(product_section_form.product_12_id.data)
        home_content.product_section_4_product_13_id = safe_id(product_section_form.product_13_id.data)
        home_content.product_section_4_product_14_id = safe_id(product_section_form.product_14_id.data)
        home_content.product_section_4_product_15_id = safe_id(product_section_form.product_15_id.data)
        home_content.product_section_4_product_16_id = safe_id(product_section_form.product_16_id.data)
        home_content.product_section_4_product_17_id = safe_id(product_section_form.product_17_id.data)
        home_content.product_section_4_product_18_id = safe_id(product_section_form.product_18_id.data)
        home_content.product_section_4_product_19_id = safe_id(product_section_form.product_19_id.data)
        home_content.product_section_4_product_20_id = safe_id(product_section_form.product_20_id.data)
        db.session.add(home_content)
        db.session.commit()

    @staticmethod
    def set_product_section_5_values_from_form(product_section_form):
        home_content = HomeContent.get()
        home_content.product_section_5_active = product_section_form.active.data
        home_content.product_section_5_name = product_section_form.name.data
        home_content.product_section_5_link = product_section_form.link.data
        home_content.product_section_5_product_1_id = safe_id(product_section_form.product_1_id.data)
        home_content.product_section_5_product_2_id = safe_id(product_section_form.product_2_id.data)
        home_content.product_section_5_product_3_id = safe_id(product_section_form.product_3_id.data)
        home_content.product_section_5_product_4_id = safe_id(product_section_form.product_4_id.data)
        home_content.product_section_5_product_5_id = safe_id(product_section_form.product_5_id.data)
        home_content.product_section_5_product_6_id = safe_id(product_section_form.product_6_id.data)
        home_content.product_section_5_product_7_id = safe_id(product_section_form.product_7_id.data)
        home_content.product_section_5_product_8_id = safe_id(product_section_form.product_8_id.data)
        home_content.product_section_5_product_9_id = safe_id(product_section_form.product_9_id.data)
        home_content.product_section_5_product_10_id = safe_id(product_section_form.product_10_id.data)
        home_content.product_section_5_product_11_id = safe_id(product_section_form.product_11_id.data)
        home_content.product_section_5_product_12_id = safe_id(product_section_form.product_12_id.data)
        home_content.product_section_5_product_13_id = safe_id(product_section_form.product_13_id.data)
        home_content.product_section_5_product_14_id = safe_id(product_section_form.product_14_id.data)
        home_content.product_section_5_product_15_id = safe_id(product_section_form.product_15_id.data)
        home_content.product_section_5_product_16_id = safe_id(product_section_form.product_16_id.data)
        home_content.product_section_5_product_17_id = safe_id(product_section_form.product_17_id.data)
        home_content.product_section_5_product_18_id = safe_id(product_section_form.product_18_id.data)
        home_content.product_section_5_product_19_id = safe_id(product_section_form.product_19_id.data)
        home_content.product_section_5_product_20_id = safe_id(product_section_form.product_20_id.data)
        db.session.add(home_content)
        db.session.commit()

    @staticmethod
    def set_more_categories_section_from_form(more_categories_section_form):
        home_content = HomeContent.get()

        home_content.more_categories_section_category_1_id = safe_id(more_categories_section_form.category_1_id.data)
        home_content.more_categories_section_category_1_image = more_categories_section_form.category_1_image.data
        home_content.more_categories_section_subcategory_1_of_category_1_id = safe_id(
            more_categories_section_form.subcategory_1_of_category_1_id.data)
        home_content.more_categories_section_subcategory_2_of_category_1_id = safe_id(
            more_categories_section_form.subcategory_2_of_category_1_id.data)
        home_content.more_categories_section_subcategory_3_of_category_1_id = safe_id(
            more_categories_section_form.subcategory_3_of_category_1_id.data)
        home_content.more_categories_section_subcategory_4_of_category_1_id = safe_id(
            more_categories_section_form.subcategory_4_of_category_1_id.data)
        home_content.more_categories_section_subcategory_5_of_category_1_id = safe_id(
            more_categories_section_form.subcategory_5_of_category_1_id.data)

        home_content.more_categories_section_category_2_id = safe_id(more_categories_section_form.category_2_id.data)
        home_content.more_categories_section_category_2_image = more_categories_section_form.category_2_image.data
        home_content.more_categories_section_subcategory_1_of_category_2_id = safe_id(
            more_categories_section_form.subcategory_1_of_category_2_id.data)
        home_content.more_categories_section_subcategory_2_of_category_2_id = safe_id(
            more_categories_section_form.subcategory_2_of_category_2_id.data)
        home_content.more_categories_section_subcategory_3_of_category_2_id = safe_id(
            more_categories_section_form.subcategory_3_of_category_2_id.data)
        home_content.more_categories_section_subcategory_4_of_category_2_id = safe_id(
            more_categories_section_form.subcategory_4_of_category_2_id.data)
        home_content.more_categories_section_subcategory_5_of_category_2_id = safe_id(
            more_categories_section_form.subcategory_5_of_category_2_id.data)

        home_content.more_categories_section_category_3_id = safe_id(more_categories_section_form.category_3_id.data)
        home_content.more_categories_section_category_3_image = more_categories_section_form.category_3_image.data
        home_content.more_categories_section_subcategory_1_of_category_3_id = safe_id(
            more_categories_section_form.subcategory_1_of_category_3_id.data)
        home_content.more_categories_section_subcategory_2_of_category_3_id = safe_id(
            more_categories_section_form.subcategory_2_of_category_3_id.data)
        home_content.more_categories_section_subcategory_3_of_category_3_id = safe_id(
            more_categories_section_form.subcategory_3_of_category_3_id.data)
        home_content.more_categories_section_subcategory_4_of_category_3_id = safe_id(
            more_categories_section_form.subcategory_4_of_category_3_id.data)
        home_content.more_categories_section_subcategory_5_of_category_3_id = safe_id(
            more_categories_section_form.subcategory_5_of_category_3_id.data)

        home_content.more_categories_section_category_4_id = safe_id(more_categories_section_form.category_4_id.data)
        home_content.more_categories_section_category_4_image = more_categories_section_form.category_4_image.data
        home_content.more_categories_section_subcategory_1_of_category_4_id = safe_id(
            more_categories_section_form.subcategory_1_of_category_4_id.data)
        home_content.more_categories_section_subcategory_2_of_category_4_id = safe_id(
            more_categories_section_form.subcategory_2_of_category_4_id.data)
        home_content.more_categories_section_subcategory_3_of_category_4_id = safe_id(
            more_categories_section_form.subcategory_3_of_category_4_id.data)
        home_content.more_categories_section_subcategory_4_of_category_4_id = safe_id(
            more_categories_section_form.subcategory_4_of_category_4_id.data)
        home_content.more_categories_section_subcategory_5_of_category_4_id = safe_id(
            more_categories_section_form.subcategory_5_of_category_4_id.data)

        home_content.more_categories_section_category_5_id = safe_id(more_categories_section_form.category_5_id.data)
        home_content.more_categories_section_category_5_image = more_categories_section_form.category_5_image.data
        home_content.more_categories_section_subcategory_1_of_category_5_id = safe_id(
            more_categories_section_form.subcategory_1_of_category_5_id.data)
        home_content.more_categories_section_subcategory_2_of_category_5_id = safe_id(
            more_categories_section_form.subcategory_2_of_category_5_id.data)
        home_content.more_categories_section_subcategory_3_of_category_5_id = safe_id(
            more_categories_section_form.subcategory_3_of_category_5_id.data)
        home_content.more_categories_section_subcategory_4_of_category_5_id = safe_id(
            more_categories_section_form.subcategory_4_of_category_5_id.data)
        home_content.more_categories_section_subcategory_5_of_category_5_id = safe_id(
            more_categories_section_form.subcategory_5_of_category_5_id.data)

        home_content.more_categories_section_category_6_id = safe_id(more_categories_section_form.category_6_id.data)
        home_content.more_categories_section_category_6_image = more_categories_section_form.category_6_image.data
        home_content.more_categories_section_subcategory_1_of_category_6_id = safe_id(
            more_categories_section_form.subcategory_1_of_category_6_id.data)
        home_content.more_categories_section_subcategory_2_of_category_6_id = safe_id(
            more_categories_section_form.subcategory_2_of_category_6_id.data)
        home_content.more_categories_section_subcategory_3_of_category_6_id = safe_id(
            more_categories_section_form.subcategory_3_of_category_6_id.data)
        home_content.more_categories_section_subcategory_4_of_category_6_id = safe_id(
            more_categories_section_form.subcategory_4_of_category_6_id.data)
        home_content.more_categories_section_subcategory_5_of_category_6_id = safe_id(
            more_categories_section_form.subcategory_5_of_category_6_id.data)

        db.session.add(home_content)
        db.session.commit()

    @staticmethod
    def set_blog_section_1_values_from_form(blog_section_form):
        home_content = HomeContent.get()
        home_content.blog_section_1_active = blog_section_form.active.data
        home_content.blog_section_1_name = blog_section_form.name.data
        home_content.blog_section_1_link = blog_section_form.link.data
        home_content.blog_section_1_post_1_id = safe_id(blog_section_form.post_1_id.data)
        home_content.blog_section_1_post_2_id = safe_id(blog_section_form.post_2_id.data)
        db.session.add(home_content)
        db.session.commit()

    @staticmethod
    def set_blog_section_2_values_from_form(blog_section_form):
        home_content = HomeContent.get()
        home_content.blog_section_2_active = blog_section_form.active.data
        home_content.blog_section_2_name = blog_section_form.name.data
        home_content.blog_section_2_link = blog_section_form.link.data
        home_content.blog_section_2_post_1_id = safe_id(blog_section_form.post_1_id.data)
        home_content.blog_section_2_post_2_id = safe_id(blog_section_form.post_2_id.data)
        db.session.add(home_content)
        db.session.commit()

    @staticmethod
    def set_blog_section_3_values_from_form(blog_section_form):
        home_content = HomeContent.get()
        home_content.blog_section_3_active = blog_section_form.active.data
        home_content.blog_section_3_name = blog_section_form.name.data
        home_content.blog_section_3_link = blog_section_form.link.data
        home_content.blog_section_3_post_1_id = safe_id(blog_section_form.post_1_id.data)
        home_content.blog_section_3_post_2_id = safe_id(blog_section_form.post_2_id.data)
        db.session.add(home_content)
        db.session.commit()

    def get_carousel_img_src(self, carousel_number):
        if carousel_number == 1:
            image_name = self.carousel_item_1_image
        elif carousel_number == 2:
            image_name = self.carousel_item_2_image
        elif carousel_number == 3:
            image_name = self.carousel_item_3_image
        else:
            raise ValueError
        if image_name is None or image_name == "":
            image_name = R.string.default_carousel_image_name
        return url_for("static", filename="imgs/" + image_name)

    def get_section_is_active(self, section_number):
        return getattr(self, "product_section_" + str(section_number) + "_active", "")

    def get_product_section_title(self, section_number):
        return getattr(self, "product_section_" + str(section_number) + "_name", "")

    def get_product_section_link(self, section_number):
        return getattr(self, "product_section_" + str(section_number) + "_link", None)

    def get_blog_section_link(self, section_number):
        return getattr(self, "blog_section_" + str(section_number) + "_link", None)

    def get_blog_section_title(self, section_number):
        return getattr(self, "blog_section_" + str(section_number) + "_name", "")

    def get_product_of_section(self, section_number, product_number):
        return Product.get(self.get_product_id_of_section(section_number=section_number, product_number=product_number))

    def get_product_id_of_section(self, section_number, product_number):
        return getattr(self, "product_section_" + str(section_number) + "_product_" + str(product_number) + "_id", 0)

    def get_blog_post_of_section(self, section_number, blog_post_number):
        return BlogPost.get(self.get_blog_post_id_of_section(section_number=section_number, blog_post_number=blog_post_number))

    def get_blog_post_id_of_section(self, section_number, blog_post_number):
        return getattr(self, "blog_section_" + str(section_number) + "_post_" + str(blog_post_number) + "_id", 0)
