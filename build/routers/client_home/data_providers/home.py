# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 29/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.home_content import HomeContent


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
            blog_sections=blog_sections
        )


client_home_data_provider = ClientHomeDataProvider()
