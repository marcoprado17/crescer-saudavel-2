# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 13/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from os.path import isfile, join

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.blog.blog_post import BlogPost
from models.content.base_content import BaseContent
from models.product.product import Product
from proj_extensions import db
from r import R
from configs import default_app_config as config


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
    products_of_section_1 = relationship("Product")

    product_section_2_active = db.Column(db.Boolean, default=False, nullable=False)
    product_section_2_name = db.Column(db.String(R.dimen.product_section_name_max_length), default="", nullable=False)
    product_section_2_link = db.Column(db.String(R.dimen.link_max_length))
    products_of_section_2 = relationship("Product")

    product_section_3_active = db.Column(db.Boolean, default=False, nullable=False)
    product_section_3_name = db.Column(db.String(R.dimen.product_section_name_max_length), default="", nullable=False)
    product_section_3_link = db.Column(db.String(R.dimen.link_max_length))
    products_of_section_3 = relationship("Product")

    product_section_4_active = db.Column(db.Boolean, default=False, nullable=False)
    product_section_4_name = db.Column(db.String(R.dimen.product_section_name_max_length), default="", nullable=False)
    product_section_4_link = db.Column(db.String(R.dimen.link_max_length))
    products_of_section_4 = relationship("Product")

    product_section_5_active = db.Column(db.Boolean, default=False, nullable=False)
    product_section_5_name = db.Column(db.String(R.dimen.product_section_name_max_length), default="", nullable=False)
    product_section_5_link = db.Column(db.String(R.dimen.link_max_length))
    products_of_section_5 = relationship("Product")

    more_categories_section_category_1 = relationship("ProductCategory", uselist=False)
    more_categories_section_category_1_image_filename = db.Column(db.String(R.dimen.filename_max_size), unique=True)
    more_categories_section_category_1_subcategories = relationship("ProductSubcategory")

    # more_categories_section_category_2_id = db.Column(db.Integer, ForeignKey("product_category.id"))
    # more_categories_section_category_2_image = db.Column(db.Text)
    # more_categories_section_subcategory_1_of_category_2_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    # more_categories_section_subcategory_2_of_category_2_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    # more_categories_section_subcategory_3_of_category_2_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    # more_categories_section_subcategory_4_of_category_2_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    # more_categories_section_subcategory_5_of_category_2_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    #
    # more_categories_section_category_3_id = db.Column(db.Integer, ForeignKey("product_category.id"))
    # more_categories_section_category_3_image = db.Column(db.Text)
    # more_categories_section_subcategory_1_of_category_3_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    # more_categories_section_subcategory_2_of_category_3_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    # more_categories_section_subcategory_3_of_category_3_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    # more_categories_section_subcategory_4_of_category_3_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    # more_categories_section_subcategory_5_of_category_3_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    #
    # more_categories_section_category_4_id = db.Column(db.Integer, ForeignKey("product_category.id"))
    # more_categories_section_category_4_image = db.Column(db.Text)
    # more_categories_section_subcategory_1_of_category_4_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    # more_categories_section_subcategory_2_of_category_4_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    # more_categories_section_subcategory_3_of_category_4_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    # more_categories_section_subcategory_4_of_category_4_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    # more_categories_section_subcategory_5_of_category_4_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    #
    # more_categories_section_category_5_id = db.Column(db.Integer, ForeignKey("product_category.id"))
    # more_categories_section_category_5_image = db.Column(db.Text)
    # more_categories_section_subcategory_1_of_category_5_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    # more_categories_section_subcategory_2_of_category_5_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    # more_categories_section_subcategory_3_of_category_5_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    # more_categories_section_subcategory_4_of_category_5_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    # more_categories_section_subcategory_5_of_category_5_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    #
    # more_categories_section_category_6_id = db.Column(db.Integer, ForeignKey("product_category.id"))
    # more_categories_section_category_6_image = db.Column(db.Text)
    # more_categories_section_subcategory_1_of_category_6_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    # more_categories_section_subcategory_2_of_category_6_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    # more_categories_section_subcategory_3_of_category_6_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    # more_categories_section_subcategory_4_of_category_6_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    # more_categories_section_subcategory_5_of_category_6_id = db.Column(db.Integer, ForeignKey("product_subcategory.id"))
    #
    # blog_section_1_active = db.Column(db.Boolean, default=False, nullable=False)
    # blog_section_1_name = db.Column(db.String(R.dimen.blog_section_name_max_length), default="", nullable=False)
    # blog_section_1_link = db.Column(db.String(R.dimen.link_max_length), default="", nullable=False)
    # blog_section_1_post_1_id = db.Column(db.Integer, ForeignKey("blog_post.id"))
    # blog_section_1_post_2_id = db.Column(db.Integer, ForeignKey("blog_post.id"))
    #
    # blog_section_2_active = db.Column(db.Boolean, default=False, nullable=False)
    # blog_section_2_name = db.Column(db.String(R.dimen.blog_section_name_max_length), default="", nullable=False)
    # blog_section_2_link = db.Column(db.String(R.dimen.link_max_length), default="", nullable=False)
    # blog_section_2_post_1_id = db.Column(db.Integer, ForeignKey("blog_post.id"))
    # blog_section_2_post_2_id = db.Column(db.Integer, ForeignKey("blog_post.id"))
    #
    # blog_section_3_active = db.Column(db.Boolean, default=False, nullable=False)
    # blog_section_3_name = db.Column(db.String(R.dimen.blog_section_name_max_length), default="", nullable=False)
    # blog_section_3_link = db.Column(db.String(R.dimen.link_max_length), default="", nullable=False)
    # blog_section_3_post_1_id = db.Column(db.Integer, ForeignKey("blog_post.id"))
    # blog_section_3_post_2_id = db.Column(db.Integer, ForeignKey("blog_post.id"))

    def get_carousel_n_image_filename(self, n):
        return getattr(self, "carousel_" + str(n) + "_image_filename")

    def get_carousel_n_img_src(self, n):
        carousel_n_image_filename = self.get_carousel_n_image_filename(n)
        if carousel_n_image_filename is not None and isfile(join(config.CAROUSEL_IMAGES_FULL_PATH, carousel_n_image_filename)):
            return join("/", config.CAROUSEL_IMAGES_FROM_STATIC_PATH, carousel_n_image_filename)
        else:
            return join("/", config.IMAGES_FROM_STATIC_PATH, R.string.carousel_default_filename)

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
