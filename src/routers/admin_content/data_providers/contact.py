# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 14/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.contact import Contact
from routers.admin_content.forms import ContactForm


class AdminContactDataProvider(object):
    def get_data(self):
        contact_form = ContactForm()
        contact_form.set_values(Contact.get())
        return dict(
            contact_form=contact_form
        )


admin_contact_data_provider = AdminContactDataProvider()
