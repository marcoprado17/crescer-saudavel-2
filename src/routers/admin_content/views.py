# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 24/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import json
from flask import render_template
from flask import request
from flask_login import login_required
from models.about_us import AboutUs
from models.contact import Contact
from models.dispatch import Dispatch
from models.exchanges_and_returns import ExchangesAndReturns
from models.faq import Faq
from models.footer import Footer
from models.header import Header
from models.home_content import HomeContent
from models.payment import Payment
from models.tags_row import TagsRow
from proj_decorators import admin_required
from routers.admin_content import admin_content_blueprint
from routers.admin_content.data_providers.about_us import admin_about_us_data_provider
from routers.admin_content.data_providers.contact import admin_contact_data_provider
from routers.admin_content.data_providers.dispatch import admin_dispatch_data_provider
from routers.admin_content.data_providers.exchanges_and_returns import admin_exchanges_and_returns_data_provider
from routers.admin_content.data_providers.faq import admin_faq_data_provider
from routers.admin_content.data_providers.footer import admin_footer_data_provider
from routers.admin_content.data_providers.header import admin_header_data_provider
from routers.admin_content.data_providers.home import admin_content_home_data_provider
from routers.admin_content.data_providers.payment import admin_payment_data_provider
from routers.admin_content.data_providers.tags_row import admin_tags_row_data_provider
from routers.admin_content.forms import CarouselForm, ProductSectionForm, BlogSectionForm, ContactForm, AboutUsForm, \
    FaqForm, FooterForm, HeaderForm, PaymentForm, DispatchForm, ExchangesAndReturnsForm, MoreCategoriesSectionForm, \
    TagsRowForm


@admin_content_blueprint.route("/home")
@login_required
@admin_required
def home():
    return render_template("admin_content/home.html", data=admin_content_home_data_provider.get_data())


@admin_content_blueprint.route("/home/salvar-carrossel/<int:carousel_number>", methods=["POST"])
@login_required
@admin_required
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
@login_required
@admin_required
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


@admin_content_blueprint.route("/home/salvar-secao-olha-so-o-que-temos-mais-para-voce", methods=["POST"])
@login_required
@admin_required
def save_more_categories_section():
    more_categories_section_form = MoreCategoriesSectionForm()

    if more_categories_section_form.validate_on_submit():
        HomeContent.set_more_categories_section_from_form(more_categories_section_form)
        return "", 200
    else:
        return json.dumps(dict(errors=more_categories_section_form.errors)), 400


@admin_content_blueprint.route("/home/salvar-secao-do-blog/<int:blog_section_number>", methods=["POST"])
@login_required
@admin_required
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


@admin_content_blueprint.route("/contato", methods=["GET", "POST"])
@login_required
@admin_required
def contact():
    if request.method=="GET":
        return render_template("admin_content/contact.html", data=admin_contact_data_provider.get_data())
    else:
        contact_form = ContactForm()
        if contact_form.validate_on_submit():
            Contact.get().update_from_form(form=contact_form)
            return "", 200
        else:
            return json.dumps(dict(errors=contact_form.errors)), 400


@admin_content_blueprint.route("/sobre-nos", methods=["GET", "POST"])
@login_required
@admin_required
def about_us():
    if request.method=="GET":
        return render_template("admin_content/about_us.html", data=admin_about_us_data_provider.get_data())
    else:
        about_us_form = AboutUsForm()
        if about_us_form.validate_on_submit():
            AboutUs.get().update_from_form(form=about_us_form)
            return "", 200
        else:
            return json.dumps(dict(errors=about_us_form.errors)), 400


@admin_content_blueprint.route("/faq", methods=["GET", "POST"])
@login_required
@admin_required
def faq():
    if request.method=="GET":
        return render_template("admin_content/faq.html", data=admin_faq_data_provider.get_data())
    else:
        faq_form = FaqForm()
        if faq_form.validate_on_submit():
            Faq.get().update_from_form(form=faq_form)
            return "", 200
        else:
            return json.dumps(dict(errors=faq_form.errors)), 400


@admin_content_blueprint.route("/pagamento", methods=["GET", "POST"])
@login_required
@admin_required
def payment():
    if request.method=="GET":
        return render_template("admin_content/payment.html", data=admin_payment_data_provider.get_data())
    else:
        payment_form = PaymentForm()
        if payment_form.validate_on_submit():
            Payment.get().update_from_form(form=payment_form)
            return "", 200
        else:
            return json.dumps(dict(errors=payment_form.errors)), 400


@admin_content_blueprint.route("/envio", methods=["GET", "POST"])
@login_required
@admin_required
def dispatch():
    if request.method=="GET":
        return render_template("admin_content/dispatch.html", data=admin_dispatch_data_provider.get_data())
    else:
        dispatch_form = DispatchForm()
        if dispatch_form.validate_on_submit():
            Dispatch.get().update_from_form(form=dispatch_form)
            return "", 200
        else:
            return json.dumps(dict(errors=dispatch_form.errors)), 400


@admin_content_blueprint.route("/trocas-e-devolucoes", methods=["GET", "POST"])
@login_required
@admin_required
def exchanges_and_returns():
    if request.method=="GET":
        return render_template("admin_content/exchanges_and_returns.html", data=admin_exchanges_and_returns_data_provider.get_data())
    else:
        exchanges_and_returns_form = ExchangesAndReturnsForm()
        if exchanges_and_returns_form.validate_on_submit():
            ExchangesAndReturns.get().update_from_form(form=exchanges_and_returns_form)
            return "", 200
        else:
            return json.dumps(dict(errors=exchanges_and_returns_form.errors)), 400


@admin_content_blueprint.route("/cabecalho", methods=["GET", "POST"])
@login_required
@admin_required
def header():
    if request.method=="GET":
        return render_template("admin_content/header.html", data=admin_header_data_provider.get_data())
    else:
        header_form = HeaderForm()
        if header_form.validate_on_submit():
            Header.get().update_from_form(form=header_form)
            return "", 200
        else:
            return json.dumps(dict(errors=header_form.errors)), 400


@admin_content_blueprint.route("/rodape", methods=["GET", "POST"])
@login_required
@admin_required
def footer():
    if request.method=="GET":
        return render_template("admin_content/footer.html", data=admin_footer_data_provider.get_data())
    else:
        footer_form = FooterForm()
        if footer_form.validate_on_submit():
            Footer.get().update_from_form(form=footer_form)
            return "", 200
        else:
            return json.dumps(dict(errors=footer_form.errors)), 400


@admin_content_blueprint.route("/tags", methods=["GET", "POST"])
@login_required
@admin_required
def tags():
    if request.method=="GET":
        return render_template("admin_content/tags_row.html", data=admin_tags_row_data_provider.get_data())
    else:
        tags_row_form = TagsRowForm()
        if tags_row_form.validate_on_submit():
            TagsRow.get().update_from_form(form=tags_row_form)
            return "", 200
        else:
            return json.dumps(dict(errors=tags_row_form.errors)), 400
