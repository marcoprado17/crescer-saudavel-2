# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 24/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.admin_attended_cities import admin_attended_cities_blueprint


@admin_attended_cities_blueprint.route("/")
def index():
    return "Cidades atendidas."


@admin_attended_cities_blueprint.route("/adiciona-cidade")
def add_city():
    return "Adicionar nova cidade."
