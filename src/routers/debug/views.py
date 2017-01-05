# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import os
import random
import shutil
import string

from flask import render_template, redirect, url_for, current_app

from models.product_category import ProductCategory
from models.product_subcategory import ProductSubcategory
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

    for i in range(0, 50):
        db.session.add(get_random_product_category())
        db.session.commit()

    for i in range(0, 300):
        db.session.add(get_random_product_subcategory())
        db.session.commit()

def get_random_product_category():
    return ProductCategory(
        name=get_random_string(random.randint(4, 8)),
        active=random.choice([True, False])
    )

def get_random_product_subcategory():
    return ProductSubcategory(
        name=get_random_string(random.randint(4, 8)),
        active=random.choice([True, False]),
        category_id = get_random_valid_product_category_id()
    )

def get_random_valid_product_category_id():
    return random.choice(ProductCategory.query.with_entities(ProductCategory.id).all())

def get_random_string(size):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(size))
