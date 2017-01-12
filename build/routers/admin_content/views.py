# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 24/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.admin_content import admin_content_blueprint


@admin_content_blueprint.route("/contato")
def contact():
    return "Contato."


@admin_content_blueprint.route("/sobre-nos")
def about_us():
    return "Sobre-nós."


@admin_content_blueprint.route("/faq")
def faq():
    return "FAQ."
