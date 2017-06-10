# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 13/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from sqlalchemy.orm import relationship
from models.associations import home_content_products_of_section_1_association_table, \
    home_content_products_of_section_2_association_table, home_content_products_of_section_3_association_table, \
    home_content_products_of_section_4_association_table, home_content_products_of_section_5_association_table, \
    home_content_more_categories_section_category_1_association_table, \
    home_content_more_categories_section_category_2_association_table, \
    home_content_more_categories_section_category_3_association_table, \
    home_content_more_categories_section_category_4_association_table, \
    home_content_more_categories_section_category_5_association_table, \
    home_content_more_categories_section_category_6_association_table, \
    home_content_more_categories_section_category_1_subcategories_association_table, \
    home_content_more_categories_section_category_2_subcategories_association_table, \
    home_content_more_categories_section_category_3_subcategories_association_table, \
    home_content_more_categories_section_category_4_subcategories_association_table, \
    home_content_more_categories_section_category_5_subcategories_association_table, \
    home_content_more_categories_section_category_6_subcategories_association_table, \
    home_content_blog_section_1_post_1_association_table, home_content_blog_section_1_post_2_association_table, \
    home_content_blog_section_2_post_1_association_table, home_content_blog_section_2_post_2_association_table, \
    home_content_blog_section_3_post_1_association_table, home_content_blog_section_3_post_2_association_table
from models.content.base_content import BaseContent
from proj_extensions import db
from r import R


class HomeContent(BaseContent):
    __tablename__ = "home_content"

    carousel_1_active = db.Column(db.Boolean, default=False, nullable=False)
    carousel_1_title = db.Column(db.String(R.dimen.carousel_title_max_length))
    carousel_1_subtitle = db.Column(db.String(R.dimen.carousel_subtitle_max_length))
    carousel_1_link = db.Column(db.String(R.dimen.link_max_length))
    carousel_1_image_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)

    carousel_2_active = db.Column(db.Boolean, default=False, nullable=False)
    carousel_2_title = db.Column(db.String(R.dimen.carousel_title_max_length))
    carousel_2_subtitle = db.Column(db.String(R.dimen.carousel_subtitle_max_length))
    carousel_2_link = db.Column(db.String(R.dimen.link_max_length))
    carousel_2_image_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)

    carousel_3_active = db.Column(db.Boolean, default=False, nullable=False)
    carousel_3_title = db.Column(db.String(R.dimen.carousel_title_max_length))
    carousel_3_subtitle = db.Column(db.String(R.dimen.carousel_subtitle_max_length))
    carousel_3_link = db.Column(db.String(R.dimen.link_max_length))
    carousel_3_image_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)

    product_section_1_active = db.Column(db.Boolean, default=False, nullable=False)
    product_section_1_name = db.Column(db.String(R.dimen.product_section_name_max_length), default="", nullable=False)
    product_section_1_link = db.Column(db.String(R.dimen.link_max_length))
    products_of_section_1 = relationship("Product", secondary=home_content_products_of_section_1_association_table)

    product_section_2_active = db.Column(db.Boolean, default=False, nullable=False)
    product_section_2_name = db.Column(db.String(R.dimen.product_section_name_max_length), default="", nullable=False)
    product_section_2_link = db.Column(db.String(R.dimen.link_max_length))
    products_of_section_2 = relationship("Product", secondary=home_content_products_of_section_2_association_table)

    product_section_3_active = db.Column(db.Boolean, default=False, nullable=False)
    product_section_3_name = db.Column(db.String(R.dimen.product_section_name_max_length), default="", nullable=False)
    product_section_3_link = db.Column(db.String(R.dimen.link_max_length))
    products_of_section_3 = relationship("Product", secondary=home_content_products_of_section_3_association_table)

    product_section_4_active = db.Column(db.Boolean, default=False, nullable=False)
    product_section_4_name = db.Column(db.String(R.dimen.product_section_name_max_length), default="", nullable=False)
    product_section_4_link = db.Column(db.String(R.dimen.link_max_length))
    products_of_section_4 = relationship("Product", secondary=home_content_products_of_section_4_association_table)

    product_section_5_active = db.Column(db.Boolean, default=False, nullable=False)
    product_section_5_name = db.Column(db.String(R.dimen.product_section_name_max_length), default="", nullable=False)
    product_section_5_link = db.Column(db.String(R.dimen.link_max_length))
    products_of_section_5 = relationship("Product", secondary=home_content_products_of_section_5_association_table)

    more_categories_section_category_1 = \
        relationship("ProductCategory", uselist=False,
                     secondary=home_content_more_categories_section_category_1_association_table)
    more_categories_section_category_1_image_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)
    more_categories_section_category_1_subcategories = \
        relationship("ProductSubcategory",
                     secondary=home_content_more_categories_section_category_1_subcategories_association_table)

    more_categories_section_category_2 = \
        relationship("ProductCategory", uselist=False,
                     secondary=home_content_more_categories_section_category_2_association_table)
    more_categories_section_category_2_image_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)
    more_categories_section_category_2_subcategories = \
        relationship("ProductSubcategory",
                     secondary=home_content_more_categories_section_category_2_subcategories_association_table)

    more_categories_section_category_3 = \
        relationship("ProductCategory", uselist=False,
                     secondary=home_content_more_categories_section_category_3_association_table)
    more_categories_section_category_3_image_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)
    more_categories_section_category_3_subcategories = \
        relationship("ProductSubcategory",
                     secondary=home_content_more_categories_section_category_3_subcategories_association_table)

    more_categories_section_category_4 = \
        relationship("ProductCategory", uselist=False,
                     secondary=home_content_more_categories_section_category_4_association_table)
    more_categories_section_category_4_image_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)
    more_categories_section_category_4_subcategories = \
        relationship("ProductSubcategory",
                     secondary=home_content_more_categories_section_category_4_subcategories_association_table)

    more_categories_section_category_5 = \
        relationship("ProductCategory", uselist=False,
                     secondary=home_content_more_categories_section_category_5_association_table)
    more_categories_section_category_5_image_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)
    more_categories_section_category_5_subcategories = \
        relationship("ProductSubcategory",
                     secondary=home_content_more_categories_section_category_5_subcategories_association_table)

    more_categories_section_category_6 = \
        relationship("ProductCategory", uselist=False,
                     secondary=home_content_more_categories_section_category_6_association_table)
    more_categories_section_category_6_image_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)
    more_categories_section_category_6_subcategories = \
        relationship("ProductSubcategory",
                     secondary=home_content_more_categories_section_category_6_subcategories_association_table)

    blog_section_1_active = db.Column(db.Boolean, default=False, nullable=False)
    blog_section_1_name = db.Column(db.String(R.dimen.blog_section_name_max_length), default="", nullable=False)
    blog_section_1_link = db.Column(db.String(R.dimen.link_max_length))
    blog_section_1_post_1 = \
        relationship("BlogPost", uselist=False,
                     secondary=home_content_blog_section_1_post_1_association_table)
    blog_section_1_post_2 = \
        relationship("BlogPost", uselist=False,
                     secondary=home_content_blog_section_1_post_2_association_table)

    blog_section_2_active = db.Column(db.Boolean, default=False, nullable=False)
    blog_section_2_name = db.Column(db.String(R.dimen.blog_section_name_max_length), default="", nullable=False)
    blog_section_2_link = db.Column(db.String(R.dimen.link_max_length))
    blog_section_2_post_1 = \
        relationship("BlogPost", uselist=False,
                     secondary=home_content_blog_section_2_post_1_association_table)
    blog_section_2_post_2 = \
        relationship("BlogPost", uselist=False,
                     secondary=home_content_blog_section_2_post_2_association_table)

    blog_section_3_active = db.Column(db.Boolean, default=False, nullable=False)
    blog_section_3_name = db.Column(db.String(R.dimen.blog_section_name_max_length), default="", nullable=False)
    blog_section_3_link = db.Column(db.String(R.dimen.link_max_length))
    blog_section_3_post_1 = \
        relationship("BlogPost", uselist=False,
                     secondary=home_content_blog_section_3_post_1_association_table)
    blog_section_3_post_2 = \
        relationship("BlogPost", uselist=False,
                     secondary=home_content_blog_section_3_post_2_association_table)

    def get_carousel_n_active(self, n):
        return getattr(self, "carousel_" + str(n) + "_active")

    def get_carousel_n_title(self, n):
        return getattr(self, "carousel_" + str(n) + "_title")

    def get_carousel_n_subtitle(self, n):
        return getattr(self, "carousel_" + str(n) + "_subtitle")

    def get_carousel_n_link(self, n):
        return getattr(self, "carousel_" + str(n) + "_link")

    def get_carousel_n_is_first(self, n):
        if n == 1:
            return self.carousel_1_active
        elif n == 2:
            return self.carousel_2_active and (not self.carousel_1_active)
        elif n == 3:
            return self.carousel_3_active and (not self.carousel_1_active) and (not self.carousel_2_active)
        return False

    def get_carousel_n_image_filename(self, n):
        return getattr(self, "carousel_" + str(n) + "_image_filename")

    def get_carousel_n_img_src(self, n):
        return self.get_img_src(self.get_carousel_n_image_filename(n), R.string.carousel_default_filename)

    def get_more_categories_n_image_filename(self, n):
        return getattr(self, "more_categories_section_category_" + str(n) + "_image_filename")

    def get_more_categories_n_img_src(self, n):
        return self.get_img_src(self.get_more_categories_n_image_filename(n), R.string.more_categories_default_filename)

    def get_section_is_active(self, section_number):
        return getattr(self, "product_section_" + str(section_number) + "_active", "")

    def get_product_section_title(self, section_number):
        return getattr(self, "product_section_" + str(section_number) + "_name", "")

    def get_product_section_link(self, section_number):
        return getattr(self, "product_section_" + str(section_number) + "_link", None)

    def get_products_of_section_n(self, n):
        return getattr(self, "products_of_section_" + str(n), None)

    def get_blog_section_link(self, section_number):
        return getattr(self, "blog_section_" + str(section_number) + "_link", None)

    def get_blog_section_title(self, section_number):
        return getattr(self, "blog_section_" + str(section_number) + "_name", "")

    def get_blog_post_of_section(self, section_number, blog_post_number):
        return getattr(self, "blog_section_" + str(section_number) + "_post_" + str(blog_post_number))

    def n_carousel_active(self):
        n = 0
        if self.carousel_1_active:
            n += 1
        if self.carousel_2_active:
            n += 1
        if self.carousel_3_active:
            n += 1
        return n

    def n_product_sections_active(self):
        n = 0
        if self.product_section_1_active:
            n += 1
        if self.product_section_2_active:
            n += 1
        if self.product_section_3_active:
            n += 1
        if self.product_section_4_active:
            n += 1
        if self.product_section_5_active:
            n += 1
        return n
