# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import logging

from flask import flash
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import desc
from proj_extensions import db
from proj_utils import parse_markdown
from r import R
from flask_admin.babel import gettext

log = logging.getLogger("flask-admin.sqla")


class ProjBaseView(ModelView):
    column_labels = R.dict.column_labels

    def create_model(self, form):
        try:
            model = self.model()
            form.populate_obj(model)
            ProjBaseView.update_html_attrs(model=model)
            self.session.add(model)
            self._on_model_change(form, model, True)
            self.session.commit()
        except Exception as ex:
            if not self.handle_view_exception(ex):
                flash(gettext('Failed to create record. %(error)s', error=str(ex)), 'error')
                log.exception('Failed to create record.')
            self.session.rollback()
            return False
        else:
            self.after_model_change(form, model, True)
        return model

    def update_model(self, form, model):
        try:
            form.populate_obj(model)
            ProjBaseView.update_html_attrs(model=model)
            self._on_model_change(form, model, False)
            self.session.commit()
        except Exception as ex:
            if not self.handle_view_exception(ex):
                flash(gettext('Failed to update record. %(error)s', error=str(ex)), 'error')
                log.exception('Failed to update record.')

            self.session.rollback()

            return False
        else:
            self.after_model_change(form, model, False)

        return True

    @staticmethod
    def update_html_attrs(model):
        html_attrs = dict()
        for attr, value in model.__dict__.iteritems():
            if attr.endswith("_markdown") and value is not None:
                html_attr = attr[0:len(attr) - len("_markdown")] + "_html"
                if hasattr(model, html_attr):
                    html_attrs[html_attr] = parse_markdown(value)
        for key, val in html_attrs.iteritems():
            setattr(model, key, val)


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    @classmethod
    def create_from_form(cls, form, other_attrs=None):
        attrs = cls.get_attrs_from_form(form=form)
        if other_attrs != None and isinstance(other_attrs, dict):
            for key, val in other_attrs.iteritems():
                attrs[key] = val
        model_elem = cls(
            **attrs
        )
        db.session.add(model_elem)
        db.session.commit()
        return model_elem

    @staticmethod
    def get_attrs_from_form(form):
        raise NotImplementedError

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def count(cls):
        return cls.query.count()

    @classmethod
    def get_last(cls):
        return cls.query.order_by(desc(cls.id)).first()

    @classmethod
    def get(cls, id):
        return cls.query.filter_by(id=id).one_or_none()

    def update_from_form(self, form):
        attrs_dict = self.__class__.get_attrs_from_form(form)
        for key, val in attrs_dict.iteritems():
            setattr(self, key, val)
        db.session.add(self)
        db.session.commit()
