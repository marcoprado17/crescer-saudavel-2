# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 10/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

from models.order import Order
from r import R


class AdminOrderFilterForm(FlaskForm):
    status = SelectField(
        label=R.string.order_status
    )
    filter = SubmitField(label=R.string.filter)

    def __init__(self, **kwargs):
        super(AdminOrderFilterForm, self).__init__(**kwargs)
        self.status.choices = Order.get_choices()

    def set_values(self, order_status_id):
        self.status.data = str(order_status_id.value)
