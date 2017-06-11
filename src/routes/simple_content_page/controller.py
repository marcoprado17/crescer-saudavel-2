# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 25/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template
from models.content.about_us import AboutUsContent
from models.content.dispatch import DispatchContent
from models.content.exchanges_and_returns import ExchangesAndReturnsContent
from models.content.faq import FaqContent
from models.content.payment import PaymentContent
from r import R
from routes.simple_content_page import simple_content_page_blueprint


@simple_content_page_blueprint.route("/sobre-nos")
def about_us():
    return render_template(
        "simple_content_page/main.html",
        title=R.string.about_us,
        content_html=AboutUsContent.get().content_html
    )


@simple_content_page_blueprint.route("/faq")
def faq():
    return render_template(
        "simple_content_page/main.html",
        title=R.string.faq,
        content_html=FaqContent.get().content_html
    )


@simple_content_page_blueprint.route("/pagamento")
def payment():
    return render_template(
        "simple_content_page/main.html",
        title=R.string.payment,
        content_html=PaymentContent.get().content_html
    )


@simple_content_page_blueprint.route("/envio")
def dispatch():
    return render_template(
        "simple_content_page/main.html",
        title=R.string.dispatch,
        content_html=DispatchContent.get().content_html
    )


@simple_content_page_blueprint.route("/trocas-e-devolucoes")
def exchanges_and_returns():
    return render_template(
        "simple_content_page/main.html",
        title=R.string.exchanges_and_returns,
        content_html=ExchangesAndReturnsContent.get().content_html
    )
