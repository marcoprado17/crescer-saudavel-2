# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 24/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import json
from flask import render_template
from models.home_content import HomeContent
from routers.admin_content import admin_content_blueprint
from routers.admin_content.data_providers.home import admin_content_home_data_provider
from routers.admin_content.forms import CarouselForm, ProductSectionForm, BlogSectionForm


@admin_content_blueprint.route("/home")
def home():
    return render_template("admin_content/home.html", data=admin_content_home_data_provider.get_data())


@admin_content_blueprint.route("/home/salvar-carrossel/<int:carousel_number>", methods=["POST"])
def save_carousel(carousel_number):
    carousel_form = CarouselForm()

    if carousel_number not in [1, 2, 3]:
        return "", 404

    if carousel_form.validate_on_submit():
        if carousel_number == 1:
            HomeContent.set_carousel_1_values_from_form(carousel_form)
        elif carousel_number == 2:
            HomeContent.set_carousel_2_values_from_form(carousel_form)
        elif carousel_number == 3:
            HomeContent.set_carousel_3_values_from_form(carousel_form)
        return "", 200
    else:
        return json.dumps(dict(errors=carousel_form.errors)), 400


@admin_content_blueprint.route("/home/salvar-secao-de-produto/<int:product_section_number>", methods=["POST"])
def save_product_section(product_section_number):
    product_section_form = ProductSectionForm()

    if product_section_number not in [1, 2, 3, 4, 5]:
        return "", 404

    if product_section_form.validate_on_submit():
        if product_section_number == 1:
            HomeContent.set_product_section_1_values_from_form(product_section_form)
        elif product_section_number == 2:
            HomeContent.set_product_section_2_values_from_form(product_section_form)
        elif product_section_number == 3:
            HomeContent.set_product_section_3_values_from_form(product_section_form)
        elif product_section_number == 4:
            HomeContent.set_product_section_4_values_from_form(product_section_form)
        elif product_section_number == 5:
            HomeContent.set_product_section_5_values_from_form(product_section_form)
        return "", 200
    else:
        return json.dumps(dict(errors=product_section_form.errors)), 400


@admin_content_blueprint.route("/home/salvar-secao-do-blog/<int:blog_section_number>", methods=["POST"])
def save_blog_section(blog_section_number):
    blog_section_form = BlogSectionForm()

    if blog_section_number not in [1, 2, 3, 4, 5]:
        return "", 404

    if blog_section_form.validate_on_submit():
        if blog_section_number == 1:
            HomeContent.set_blog_section_1_values_from_form(blog_section_form)
        elif blog_section_number == 2:
            HomeContent.set_blog_section_2_values_from_form(blog_section_form)
        elif blog_section_number == 3:
            HomeContent.set_blog_section_3_values_from_form(blog_section_form)
        return "", 200
    else:
        return json.dumps(dict(errors=blog_section_form.errors)), 400


@admin_content_blueprint.route("/contato")
def contact():
    return "Contato."


@admin_content_blueprint.route("/sobre-nos")
def about_us():
    return "Sobre-nós."


@admin_content_blueprint.route("/faq")
def faq():
    return "FAQ."
