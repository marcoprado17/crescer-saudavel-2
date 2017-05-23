# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 13/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.content.home_content import HomeContent
from routers.admin_content.forms import CarouselForm, ProductSectionForm, BlogSectionForm, \
    MoreCategoriesSectionForm


class AdminContentHomeDataProvider(object):
    def get_data(self):
        home_content = HomeContent.get()

        return dict(
            carousel_1_form=CarouselForm(home_content=home_content, carousel_number=1),
            carousel_2_form=CarouselForm(home_content=home_content, carousel_number=2),
            carousel_3_form=CarouselForm(home_content=home_content, carousel_number=3),
            product_section_1_form=ProductSectionForm(home_content=home_content, product_section_number=1),
            product_section_2_form=ProductSectionForm(home_content=home_content, product_section_number=2),
            product_section_3_form=ProductSectionForm(home_content=home_content, product_section_number=3),
            product_section_4_form=ProductSectionForm(home_content=home_content, product_section_number=4),
            product_section_5_form=ProductSectionForm(home_content=home_content, product_section_number=5),
            more_categories_section_form=MoreCategoriesSectionForm(home_content=home_content),
            blog_section_1_form=BlogSectionForm(home_content=home_content, blog_section_number=1),
            blog_section_2_form=BlogSectionForm(home_content=home_content, blog_section_number=2),
            blog_section_3_form=BlogSectionForm(home_content=home_content, blog_section_number=3)
        )

admin_content_home_data_provider = AdminContentHomeDataProvider()
