# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import os
import shutil

from flask import render_template, redirect, url_for, current_app
from models.utils import create_states, create_random_product_categories, create_random_product_subcategories, \
    create_random_products, create_specif_cities, create_random_clients, create_random_orders, create_home_content, \
    create_contact, create_about_us, create_faq, create_footer, create_random_blog_posts, create_header, create_payment, \
    create_dispatch, create_exchanges_and_returns, create_newsletter_emails, create_tags_row
from proj_utils import create_product_image, create_blog_thumbnail_image
from routers.debug import debug_blueprint
from proj_extensions import db


@debug_blueprint.route("/test")
def test():
    return render_template("debug/test.html")


@debug_blueprint.route("/reiniciar-imagens")
def restart_images():
    restart_images_implementation()
    return redirect(url_for("admin_home.home"))


def restart_images_implementation():
    src_folder_path = "/vagrant/images"
    destiny_folder_path = current_app.config['UPLOADED_IMAGES_FOLDER_FULL_PATH']

    if os.path.isdir(destiny_folder_path):
        for file_or_dir_name in os.listdir(destiny_folder_path):
            file_or_dir_path = os.path.join(destiny_folder_path, file_or_dir_name)
            if os.path.exists(file_or_dir_path):
                if os.path.isfile(file_or_dir_path):
                    os.remove(file_or_dir_path)
                elif os.path.isdir(file_or_dir_path):
                    shutil.rmtree(file_or_dir_path)

    for file_name in os.listdir(src_folder_path):
        file_path = os.path.join(src_folder_path, file_name)
        if os.path.exists(file_path):
            shutil.copy(file_path, destiny_folder_path)


@debug_blueprint.route("/criar-imagens-redimensionadas")
def create_resized_images():
    create_products_images_implementation()
    create_blog_thumbnails_images_implementation()
    return redirect(url_for("admin_home.home"))


def create_products_images_implementation():
    src_folder_path = "/vagrant/images"
    products_folder_path = current_app.config['PRODUCTS_IMAGES_FOLDER_FULL_PATH']

    if os.path.isdir(products_folder_path):
        for file_name in os.listdir(products_folder_path):
            file_path = os.path.join(products_folder_path, file_name)
            if os.path.exists(file_path):
                os.remove(file_path)

    for file_name in os.listdir(src_folder_path):
        file_path = os.path.join(src_folder_path, file_name)
        create_product_image(file_path, file_name)


def create_blog_thumbnails_images_implementation():
    src_folder_path = "/vagrant/images"
    blog_thumbnails_folder_path = current_app.config['BLOG_THUMBNAILS_IMAGES_FOLDER_FULL_PATH']

    if os.path.isdir(blog_thumbnails_folder_path):
        for file_name in os.listdir(blog_thumbnails_folder_path):
            file_path = os.path.join(blog_thumbnails_folder_path, file_name)
            if os.path.exists(file_path):
                os.remove(file_path)

    for file_name in os.listdir(src_folder_path):
        file_path = os.path.join(src_folder_path, file_name)
        create_blog_thumbnail_image(file_path, file_name)


@debug_blueprint.route("/reiniciar-db")
def restart_db():
    restart_db_implementation()
    return redirect(url_for("admin_home.home"))


def restart_db_implementation():
    whoosh_base_path = current_app.config['WHOOSH_BASE']
    if os.path.isdir(whoosh_base_path):
        shutil.rmtree(whoosh_base_path)

    db.drop_all()
    db.create_all()

    create_random_product_categories()
    create_random_product_subcategories()
    create_random_products()
    create_states()
    create_specif_cities()
    create_random_clients()
    create_random_orders()
    create_random_blog_posts()

    create_home_content()
    create_newsletter_emails()
    create_tags_row()
    create_contact()
    create_about_us()
    create_faq()
    create_payment()
    create_dispatch()
    create_exchanges_and_returns()
    create_header()
    create_footer()
