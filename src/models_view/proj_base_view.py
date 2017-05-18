import logging

from flask import flash, redirect, url_for, request
from flask_admin.contrib.sqla import ModelView
from proj_utils import parse_markdown
from r import R
from flask_admin.babel import gettext
from flask_login import current_user
from flask import current_app


log = logging.getLogger("flask-admin.sqla")


class ProjBaseView(ModelView):
    column_labels = R.dict.column_labels
    name = None
    endpoint = None
    category = None

    def __init__(self, *args, **kwargs):
        if self.name:
            kwargs["name"] = self.name
        if self.endpoint:
            kwargs["endpoint"] = self.endpoint
        if self.category:
            kwargs["category"] = self.category
        super(ProjBaseView, self).__init__(*args, **kwargs)

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

    def is_accessible(self):
        return current_user is not None and current_user.is_authenticated and current_user.email == current_app.config['ADMIN_MAIL']

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("client_user_management.login", next=request.url))
