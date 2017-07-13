from flask import Blueprint, app, render_template

error_pages_blueprint = Blueprint("error_pages", __name__, static_folder="static", template_folder="templates")
