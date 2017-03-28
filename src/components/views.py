# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 28/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from components import components_blueprint


@components_blueprint.route("/registrar-novo-email-do-newsletter", methods=["POST"])
def register_new_newsletter_email():
    return "", 200
