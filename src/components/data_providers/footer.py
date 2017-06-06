# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 25/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from components.forms import NewsletterEmailForm
from models.content.about_us import AboutUsContent
from models.content.contact import Contact
from models.content.footer import Footer


class FooterDataProvider(object):
    # noinspection PyMethodMayBeStatic
    def get_data(self):
        return dict(
            contact=Contact.get(),
            about_us=AboutUsContent.get(),
            footer=Footer.get(),
            newsletter_email_form=NewsletterEmailForm()
        )

footer_data_provider = FooterDataProvider()
