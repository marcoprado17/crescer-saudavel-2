# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 13/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.admin_content.forms import CarouselForm, ProductSectionForm, BlogSectionForm


class AdminContentHomeDataProvider(object):
    def get_data(self):
        carousel_1_form = CarouselForm()
        carousel_2_form = CarouselForm()
        carousel_3_form = CarouselForm()

        product_section_1_form = ProductSectionForm()
        product_section_2_form = ProductSectionForm()
        product_section_3_form = ProductSectionForm()
        product_section_4_form = ProductSectionForm()
        product_section_5_form = ProductSectionForm()

        blog_section_1_form = BlogSectionForm()
        blog_section_2_form = BlogSectionForm()
        blog_section_3_form = BlogSectionForm()

        return dict(
            carousel_1_form=carousel_1_form,
            carousel_2_form=carousel_2_form,
            carousel_3_form=carousel_3_form,
            product_section_1_form=product_section_1_form,
            product_section_2_form=product_section_2_form,
            product_section_3_form=product_section_3_form,
            product_section_4_form=product_section_4_form,
            product_section_5_form=product_section_5_form,
            blog_section_1_form=blog_section_1_form,
            blog_section_2_form=blog_section_2_form,
            blog_section_3_form=blog_section_3_form
        )

admin_content_home_data_provider = AdminContentHomeDataProvider()
