# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import os
import random
import shutil
import string
from decimal import Decimal

from flask import render_template, redirect, url_for, current_app

from models.product import Product
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

    for i in range(0, 500):
        db.session.add(get_random_product())
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

def get_random_product():
    random_value = random.uniform(0, 1)
    category_id = None
    subcategory_id = None
    if random_value < 0.75:
        category_id = get_random_valid_product_category_id(),
        subcategory_id = get_random_valid_product_subcategory_id(category_id=category_id),
    else:
        category_id = get_random_valid_product_category_id(),

    return Product(
        active=(random.uniform(0, 1) < 0.5),
        title=get_random_title(),
        category_id=category_id,
        subcategory_id=subcategory_id,
        price=Decimal(get_random_price()),
        stock=get_random_stock(),
        min_stock=get_random_min_stock(),
        summary=get_random_summary(),
        sales_number=get_random_sales_number(),
        **get_random_images_dic()
    )

def get_random_valid_product_category_id():
    return random.choice(ProductCategory.query.with_entities(ProductCategory.id).all())

def get_random_valid_product_subcategory_id(category_id):
    try:
        return random.choice(ProductSubcategory.query.filter(ProductSubcategory.category_id==category_id).with_entities(ProductSubcategory.id).all())
    except Exception:
        return None

def get_random_title():
    s = ""
    for _ in range(random.randint(3, 6)):
        s += get_random_string(random.randint(3, 8))
        s += " "
    return s[:-1]

def get_random_summary():
    s = ""
    for _ in range(random.randint(20, 100)):
        s += get_random_string(random.randint(3, 8))
        s += " "
    return s[:-1]

def get_random_string(size):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(size))

def get_random_price():
    s = get_random_digit()
    if random.uniform(0, 1) < 0.5:
        s += get_random_digit()
    s += "."
    s += get_random_digit()
    s += get_random_digit()

    return s

def get_random_digit():
    return random.choice(string.digits)

def get_random_stock():
    return random.randint(0, 500)

def get_random_min_stock():
    return random.randint(2, 20)

def get_random_sales_number():
    return random.randint(0, 500)

images_key_list = [
    "image_1",
    "image_2",
    "image_3",
    "image_4",
    "image_5",
    "image_6",
    "image_7",
    "image_8",
    "image_9",
    "image_10",
]

def get_random_images_dic():
    images_key_list_copy = list(images_key_list)
    dic = {images_key_list_copy.pop(0): get_random_image_name()}
    for i in range(0, 9):
        dic[images_key_list_copy.pop(random.randint(0, len(images_key_list_copy)-1))] = get_random_image_name()
    return dic

def get_random_image_name():
    return random.choice(os.listdir(current_app.config["UPLOADED_IMAGES_FOLDER_FULL_PATH"]))
