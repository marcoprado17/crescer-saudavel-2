# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 12/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import sys

from models.utils import create_random_product_categories, create_random_products, create_specif_cities, create_random_clients, create_random_orders, \
    create_random_product_subcategories, create_random_blog_posts

sys.path.append("/vagrant")
sys.path.append("/vagrant/build")

from app_contexts.app import app


def fill_db_with_random_data():
    with app.app_context():
        create_random_product_categories()
        create_random_product_subcategories()
        create_random_products()
        create_specif_cities()
        create_random_clients()
        create_random_orders()
        create_random_blog_posts()

if __name__ == "__main__":
    fill_db_with_random_data()
