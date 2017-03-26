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

    def __init__(self, order_status_id, **kwargs):
        super(AdminOrderFilterForm, self).__init__(**kwargs)
        self.status.choices = Order.get_order_status_id_choices()
        self.status.data = str(order_status_id.value)
