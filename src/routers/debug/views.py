# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import os
import shutil

from flask import render_template, redirect, url_for, current_app
from routers.debug import debug_blueprint
from extensions import db


@debug_blueprint.route("/test")
def test():
    return render_template("debug/test.html")

@debug_blueprint.route("/reiniciar-imagens")
def restart_images():
    restart_images_implementation()
    return redirect(url_for("admin_home.index"))

def restart_images_implementation():
    src_folder_path = "/vagrant/debug_images"
    destiny_folder_path = current_app.config['UPLOADED_IMAGES_FOLDER_FULL_PATH']

    for file_name in os.listdir(destiny_folder_path):
        file_path = os.path.join(destiny_folder_path, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)

    for file_name in os.listdir(src_folder_path):
        file_path = os.path.join(src_folder_path, file_name)
        if os.path.exists(file_path):
            shutil.copy(file_path, destiny_folder_path)

@debug_blueprint.route("/reiniciar-db")
def restart_db():
    restart_db_implementation()
    return redirect(url_for("admin_home.index"))

def restart_db_implementation():
    db.drop_all()
    db.create_all()
