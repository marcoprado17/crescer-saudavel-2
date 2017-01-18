# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 16/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from extensions import db


class Faq(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.UnicodeText)

    @staticmethod
    def get():
        faqs = Faq.query.all()
        assert len(faqs)
        return faqs[0]

    @staticmethod
    def set_values_from_form(faq_form):
        faq = Faq.get()
        faq.content = faq_form.content.data
        db.session.add(faq)
        db.session.commit()
