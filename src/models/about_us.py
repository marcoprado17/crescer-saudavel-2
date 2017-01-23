# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 16/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from proj_extensions import db
from models.base import BaseModel


class AboutUs(BaseModel):
    content = db.Column(db.UnicodeText)

    @staticmethod
    def get():
        all_about_us = AboutUs.query.all()
        assert len(all_about_us)
        return all_about_us[0]

    @staticmethod
    def set_values_from_form(about_us_form):
        about_us = AboutUs.get()
        about_us.content = about_us_form.content.data
        db.session.add(about_us)
        db.session.commit()
