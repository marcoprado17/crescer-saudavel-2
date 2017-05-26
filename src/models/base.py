# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from sqlalchemy import desc
from proj_extensions import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def count(cls):
        return cls.query.count()

    @classmethod
    def get_last(cls):
        return cls.query.order_by(desc(cls.id)).first()

    # noinspection PyShadowingBuiltins
    @classmethod
    def get(cls, id):
        return cls.query.filter_by(id=id).one_or_none()
