# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.client_user_management import client_user_management_blueprint


@client_user_management_blueprint.route("/entrar")
def login():
    return "Entrar."


@client_user_management_blueprint.route("/cadastrar")
def register():
    return "Cadastrar."
