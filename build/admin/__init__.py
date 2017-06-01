from flask import Blueprint

admin_proj_blueprint = Blueprint("admin_proj", __name__, static_folder="static", template_folder="templates")

import views
