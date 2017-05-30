# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 28/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import json

from components import components_blueprint
from components.forms import NewsletterEmailForm
from models.newsletter_emails import NewsletterEmails


@components_blueprint.route("/registrar-novo-email-do-newsletter", methods=["POST"])
def register_new_newsletter_email():
    newsletter_email_form = NewsletterEmailForm()
    if newsletter_email_form.validate_on_submit():
        newsletter_emails = NewsletterEmails.get()
        newsletter_emails.add(newsletter_email_form.email.data)
        return "", 200
    else:
        return json.dumps(dict(errors=newsletter_email_form.errors)), 400
