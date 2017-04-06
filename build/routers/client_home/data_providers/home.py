# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 29/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import url_for

from models.home_content import HomeContent
from models.product_category import ProductCategory
from models.product_subcategory import ProductSubcategory
from r import R


class ClientHomeDataProvider(object):
    def get_data(self):
        carousel = []

        home_content = HomeContent.get()

        if home_content.carousel_item_1_active:
            carousel.append(
                dict(
                    title=home_content.carousel_item_1_title,
                    subtitle=home_content.carousel_item_1_subtitle,
                    img_src=home_content.get_carousel_img_src(carousel_number=1),
                    href=home_content.carousel_item_1_link if home_content.carousel_item_1_link is not None and home_content.carousel_item_1_link != "" else None
                )
            )
        if home_content.carousel_item_2_active:
            carousel.append(
                dict(
                    title=home_content.carousel_item_2_title,
                    subtitle=home_content.carousel_item_2_subtitle,
                    img_src=home_content.get_carousel_img_src(carousel_number=2),
                    href=home_content.carousel_item_2_link if home_content.carousel_item_2_link is not None and home_content.carousel_item_2_link != "" else None
                )
            )
        if home_content.carousel_item_3_active:
            carousel.append(
                dict(
                    title=home_content.carousel_item_3_title,
                    subtitle=home_content.carousel_item_3_subtitle,
                    img_src=home_content.get_carousel_img_src(carousel_number=3),
                    href=home_content.carousel_item_3_link if home_content.carousel_item_3_link is not None and home_content.carousel_item_3_link != "" else None
                )
            )

        product_sections = []
        for section_number in range(1, 5 + 1):
            if home_content.get_section_is_active(section_number=section_number):
                section = {}
                products = []
                for product_number in range(1, 20 + 1):
                    product = home_content.get_product_of_section(section_number=section_number,
                                                                  product_number=product_number)
                    if product is not None and product.active:
                        products.append(product)
                if len(products) > 0:
                    section["title"] = home_content.get_product_section_title(section_number=section_number)
                    section["href"] = home_content.get_product_section_link(section_number=section_number)
                    section["products"] = products
                    product_sections.append(section)

        more_categories = []
        for i in range(1, 6 + 1):
            category_data = self.get_more_categories_section_category_data(home_content=home_content, category_number=i)
            if category_data is not None:
                more_categories.append(category_data)

        blog_sections = []
        for section_number in range(1, 3 + 1):
            section = {}
            blog_posts = []
            for blog_post_number in range(1, 2 + 1):
                blog_post = home_content.get_blog_post_of_section(section_number=section_number,
                                                                  blog_post_number=blog_post_number)
                if blog_post is not None and blog_post.active:
                    blog_posts.append(blog_post)
            if len(blog_posts) > 0:
                section["title"] = home_content.get_blog_section_title(section_number=section_number)
                section["href"] = home_content.get_blog_section_link(section_number=section_number)
                section["blog_posts"] = blog_posts
                blog_sections.append(section)

        return dict(
            carousel=carousel,
            product_sections=product_sections,
            more_categories=more_categories,
            blog_sections=blog_sections
        )

    def get_more_categories_section_category_data(self, home_content, category_number):
        category_id = getattr(home_content, "more_categories_section_category_%s_id" % category_number, None)
        if category_id is None:
            return None

        subcategories = []

        subcategory_1_id = getattr(home_content,
                                   "more_categories_section_subcategory_1_of_category_%s_id" % category_number, None)
        if subcategory_1_id is not None:
            subcategories.append(dict(
                name=ProductSubcategory.get(subcategory_1_id).name,
                href=url_for("client_products.products", **{R.string.subcategory_id_arg_name: subcategory_1_id})
            ))

        subcategory_2_id = getattr(home_content,
                                   "more_categories_section_subcategory_2_of_category_%s_id" % category_number, None)
        if subcategory_2_id is not None:
            subcategories.append(dict(
                name=ProductSubcategory.get(subcategory_2_id).name,
                href=url_for("client_products.products", **{R.string.subcategory_id_arg_name: subcategory_2_id})
            ))

        subcategory_3_id = getattr(home_content,
                                   "more_categories_section_subcategory_3_of_category_%s_id" % category_number, None)
        if subcategory_3_id is not None:
            subcategories.append(dict(
                name=ProductSubcategory.get(subcategory_3_id).name,
                href=url_for("client_products.products", **{R.string.subcategory_id_arg_name: subcategory_3_id})
            ))

        subcategory_4_id = getattr(home_content,
                                   "more_categories_section_subcategory_4_of_category_%s_id" % category_number, None)
        if subcategory_4_id is not None:
            subcategories.append(dict(
                name=ProductSubcategory.get(subcategory_4_id).name,
                href=url_for("client_products.products", **{R.string.subcategory_id_arg_name: subcategory_4_id})
            ))

        subcategory_5_id = getattr(home_content,
                                   "more_categories_section_subcategory_5_of_category_%s_id" % category_number, None)
        if subcategory_5_id is not None:
            subcategories.append(dict(
                name=ProductSubcategory.get(subcategory_5_id).name,
                href=url_for("client_products.products", **{R.string.subcategory_id_arg_name: subcategory_5_id})
            ))

        category = ProductCategory.get(category_id)

        image_name = getattr(home_content, "more_categories_section_category_%s_image" % category_number, None)

        return dict(
            category_name=category.name,
            category_href=url_for("client_products.products", **{R.string.category_id_arg_name: category_id}),
            image_src=url_for("static", filename="imgs/%s" % image_name) if image_name is not None and image_name != "" else None,
            subcategories=subcategories
        )


client_home_data_provider = ClientHomeDataProvider()
