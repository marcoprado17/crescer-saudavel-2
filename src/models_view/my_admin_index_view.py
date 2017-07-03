from flask import current_app, redirect, url_for, request
from flask_admin import expose, AdminIndexView
from flask_login import current_user


class MyAdminIndexView(AdminIndexView):
    @expose()
    def index(self):
        if current_user is not None and current_user.is_authenticated and current_user.email == current_app.config['ADMIN_MAIL']:
            return self.render("admin/index.html")
        else:
            return redirect(url_for("user_management.login", next=request.url))
