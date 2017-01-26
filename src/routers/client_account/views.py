# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.client_account import client_account_blueprint


@client_account_blueprint.route("/")
def my_account():
    return "My account page."
