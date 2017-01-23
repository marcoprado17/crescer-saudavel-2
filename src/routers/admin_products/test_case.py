# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import os
import shutil

from decimal import Decimal
from unittest import TestCase as BaseTestCase
from flask import url_for
from app_contexts.app import app
from proj_extensions import db
from models.product import Product
from models.product_subcategory import ProductSubcategory
from models.product_category import ProductCategory
from r import R


class TestCase(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        with app.app_context():
            db.drop_all()
            db.create_all()

            app.config["SERVER_NAME"] = "localhost:5000"
            app.config["WTF_CSRF_ENABLED"] = False

            src_folder_path = "/vagrant/debug_images"
            destiny_folder_path = app.config['UPLOADED_IMAGES_FOLDER_FULL_PATH']
            file_path = os.path.join(src_folder_path, "product_default.jpg")
            shutil.copy(file_path, destiny_folder_path)

    @classmethod
    def tearDownClass(cls):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test(self):
        with app.app_context():
            with app.test_client() as c:
                # ------------------------------------------------------------------------------------------------------
                # Add ProductCategory
                # ------------------------------------------------------------------------------------------------------
                self.assertEqual(ProductCategory.count(), 0)
                response = c.post(url_for("admin_products.add_category"), data=dict(
                    category_name=R.string.test1,
                    active=True,
                ))
                self.assertEqual(response.status_code, 302)
                n_categories = ProductCategory.count()
                self.assertEqual(n_categories, 1)
                product_category = ProductCategory.get_last()
                self.assertEqual(product_category.name, R.string.test1)
                self.assertEqual(product_category.active, True)

                response = c.post(url_for("admin_products.add_category"), data=dict(
                    category_name="a",
                ))
                self.assertEqual(response.status_code, 302)
                self.assertEqual(ProductCategory.count(), 2)
                product_category = ProductCategory.get_last()
                self.assertEqual(product_category.name, "a")
                self.assertEqual(product_category.active, False)

                # ------------------------------------------------------------------------------------------------------
                # Edit ProductCategory
                # ------------------------------------------------------------------------------------------------------
                product_category = ProductCategory.get_last()
                response = c.post(url_for("admin_products.edit_category", product_category_id=product_category.id), data=dict(
                    category_name="b",
                    active=True,
                ))
                product_category = ProductCategory.get_last()
                self.assertEqual(response.status_code, 302)
                self.assertEqual(product_category.name, "b")
                self.assertEqual(product_category.active, True)

                product_category = ProductCategory.get_last()
                response = c.post(url_for("admin_products.edit_category", product_category_id=product_category.id), data=dict(
                      category_name="c",
                ))
                product_category = ProductCategory.get_last()
                self.assertEqual(response.status_code, 302)
                self.assertEqual(product_category.name, "c")
                self.assertEqual(product_category.active, False)

                # ------------------------------------------------------------------------------------------------------
                # ProductCategory Activate / Disable
                # ------------------------------------------------------------------------------------------------------
                product_category = ProductCategory.get_last()
                response = c.post(url_for("admin_products.to_activate_category", product_category_id=product_category.id))
                product_category = ProductCategory.get_last()
                self.assertEqual(response.status_code, 200)
                self.assertEqual(product_category.active, True)

                response = c.post(
                    url_for("admin_products.disable_category", product_category_id=product_category.id))
                product_category = ProductCategory.get_last()
                self.assertEqual(response.status_code, 200)
                self.assertEqual(product_category.active, False)

                response = c.post(
                    url_for("admin_products.disable_category", product_category_id=product_category.id))
                product_category = ProductCategory.get_last()
                self.assertEqual(response.status_code, 200)
                self.assertEqual(product_category.active, False)

                product_category = ProductCategory.get_last()
                response = c.post(
                    url_for("admin_products.to_activate_category", product_category_id=product_category.id))
                product_category = ProductCategory.get_last()
                self.assertEqual(response.status_code, 200)
                self.assertEqual(product_category.active, True)

                product_category = ProductCategory.get_last()
                response = c.post(
                    url_for("admin_products.to_activate_category", product_category_id=product_category.id))
                product_category = ProductCategory.get_last()
                self.assertEqual(response.status_code, 200)
                self.assertEqual(product_category.active, True)

                response = c.post(
                    url_for("admin_products.disable_category", product_category_id=product_category.id))
                product_category = ProductCategory.get_last()
                self.assertEqual(response.status_code, 200)
                self.assertEqual(product_category.active, False)

                # ------------------------------------------------------------------------------------------------------
                # Add ProductSubcategory
                # ------------------------------------------------------------------------------------------------------
                n_subcategories = ProductSubcategory.count()
                self.assertEqual(n_subcategories, 0)
                response = c.post(url_for("admin_products.add_subcategory"), data=dict(
                    category_id="1",
                    subcategory_name=R.string.test1,
                    active=True,
                ))
                self.assertEqual(response.status_code, 302)
                n_subcategories = ProductSubcategory.count()
                self.assertEqual(n_subcategories, 1)
                subcategory = ProductSubcategory.get_last()
                self.assertEqual(subcategory.category_id, 1)
                self.assertEqual(subcategory.name, R.string.test1)
                self.assertEqual(subcategory.active, True)

                # ------------------------------------------------------------------------------------------------------
                # Add Product
                # ------------------------------------------------------------------------------------------------------
                n_products = Product.query.count()
                self.assertEqual(n_products, 0)
                response = c.post(url_for("admin_products.add_product"), data=dict(
                    title=R.string.test1,
                    active=False,
                    category_id="1",
                    subcategory_id="1",
                    price=R.string.test_price,
                    stock=R.dimen.test_stock,
                    min_available=R.dimen.test_min_available,
                    summary=R.string.test1,
                    image_1="",
                    image_2="",
                    image_3="",
                    image_4="",
                    image_5="",
                    image_6="",
                    image_7="",
                    image_8="",
                    image_9="",
                    image_10=""
                ))
                self.assertEqual(response.status_code, 302)
                self.assertEqual(Product.count(), 1)

                response = c.post(url_for("admin_products.add_product"), data=dict(
                    title=R.string.test1,
                    active=True,
                    category_id="1",
                    subcategory_id="1",
                    price=R.string.test_price,
                    stock=R.dimen.test_stock,
                    min_available=R.dimen.test_min_available,
                    summary=R.string.test1,
                    image_1="",
                    image_2="",
                    image_3="",
                    image_4="",
                    image_5="",
                    image_6="",
                    image_7="",
                    image_8="",
                    image_9="",
                    image_10=""
                ))
                self.assertEqual(response.status_code, 302)
                self.assertEqual(Product.count(), 2)
                product = Product.get_last()
                self.assertEqual(product.title, R.string.test1)
                self.assertEqual(product.active, True)
                self.assertEqual(product.category_id, 1)
                self.assertEqual(product.subcategory_id, 1)
                self.assertEqual(product.price, Decimal(R.string.test_price.replace(",", ".")))
                self.assertEqual(product.stock, R.dimen.test_stock)
                self.assertEqual(product.min_available, R.dimen.test_min_available)
                self.assertEqual(product.image_1, "")
                self.assertEqual(product.image_2, "")
                self.assertEqual(product.image_3, "")
                self.assertEqual(product.image_4, "")
                self.assertEqual(product.image_5, "")
                self.assertEqual(product.image_6, "")
                self.assertEqual(product.image_7, "")
                self.assertEqual(product.image_8, "")
                self.assertEqual(product.image_9, "")
                self.assertEqual(product.image_10, "")

                self.assertEqual(product.available, R.dimen.test_stock)
                self.assertEqual(product.reserved, 0)
                self.assertEqual(product.sales_number, 0)

                product = Product(
                    title=R.string.test1,
                    active=True,
                    category_id="1",
                    subcategory_id="1",
                    price=Decimal(R.string.test_price.replace(",", ".")),
                    stock=22,
                    reserved=12,
                    min_available=R.dimen.test_min_available,
                    summary=R.string.test1,
                    image_1="",
                    image_2="",
                    image_3="",
                    image_4="",
                    image_5="",
                    image_6="",
                    image_7="",
                    image_8="",
                    image_9="",
                    image_10="",
                    sales_number=3
                )
                db.session.add(product)
                db.session.commit()
                self.assertEqual(Product.count(), 3)
                product = Product.get_last()
                self.assertEqual(product.title, R.string.test1)
                self.assertEqual(product.active, True)
                self.assertEqual(product.category_id, 1)
                self.assertEqual(product.subcategory_id, 1)
                self.assertEqual(product.price, Decimal(R.string.test_price.replace(",", ".")))
                self.assertEqual(product.stock, 22)
                self.assertEqual(product.min_available, R.dimen.test_min_available)
                self.assertEqual(product.image_1, "")
                self.assertEqual(product.image_2, "")
                self.assertEqual(product.image_3, "")
                self.assertEqual(product.image_4, "")
                self.assertEqual(product.image_5, "")
                self.assertEqual(product.image_6, "")
                self.assertEqual(product.image_7, "")
                self.assertEqual(product.image_8, "")
                self.assertEqual(product.image_9, "")
                self.assertEqual(product.image_10, "")

                self.assertEqual(product.available, 10)
                self.assertEqual(product.reserved, 12)
                self.assertEqual(product.sales_number, 3)

                # ------------------------------------------------------------------------------------------------------
                # Edit Product
                # ------------------------------------------------------------------------------------------------------
                product = Product.get_last()
                response = c.post(url_for("admin_products.edit_product", product_id=Product.count()+1), data=dict(
                    title="a",
                    category_id=str(product.category_id),
                    subcategory_id=str(product.subcategory_id),
                    price="1,42",
                    stock=13,
                    min_available=product.min_available,
                    summary=product.summary,
                    image_1="product_default.jpg",
                    image_2="product_default.jpg",
                    image_3="",
                    image_4="",
                    image_5="",
                    image_6="",
                    image_7="",
                    image_8="",
                    image_9="",
                    image_10=""
                ))
                self.assertEqual(response.status_code, 404)

                product = Product.get_last()
                response = c.post(url_for("admin_products.edit_product", product_id=product.id), data=dict(
                    title="a",
                    category_id=str(product.category_id),
                    subcategory_id=str(product.subcategory_id),
                    price="1,42",
                    stock=13,
                    min_available=product.min_available,
                    summary=product.summary,
                    image_1="product_default.jpg",
                    image_2="product_default.jpg",
                    image_3="",
                    image_4="",
                    image_5="",
                    image_6="",
                    image_7="",
                    image_8="",
                    image_9="",
                    image_10=""
                ))

                self.assertEqual(response.status_code, 302)
                self.assertEqual(Product.count(), 3)

                product = Product.get_last()
                self.assertEqual(product.title, "a")
                self.assertEqual(product.active, False)
                self.assertEqual(product.price, Decimal("1.42"))
                self.assertEqual(product.stock, 13)
                self.assertEqual(product.available, 1)
                self.assertEqual(product.image_1, "product_default.jpg")
                self.assertEqual(product.image_2, "product_default.jpg")

                product = Product.get_last()
                response = c.post(url_for("admin_products.edit_product", product_id=product.id), data=dict(
                    title="a",
                    category_id=str(product.category_id),
                    subcategory_id=str(product.subcategory_id),
                    price="1,42",
                    stock=6,
                    min_available=product.min_available,
                    summary=product.summary,
                    image_1="product_default.jpg",
                    image_2="product_default.jpg",
                    image_3="",
                    image_4="",
                    image_5="",
                    image_6="",
                    image_7="",
                    image_8="",
                    image_9="",
                    image_10=""
                ))

                self.assertEqual(response.status_code, 302)
                self.assertEqual(Product.count(), 3)

                product = Product.get_last()
                self.assertEqual(product.title, "a")
                self.assertEqual(product.active, False)
                self.assertEqual(product.price, Decimal("1.42"))
                self.assertEqual(product.stock, 6)
                self.assertEqual(product.available, -6)
                self.assertEqual(product.image_1, "product_default.jpg")
                self.assertEqual(product.image_2, "product_default.jpg")

                # ------------------------------------------------------------------------------------------------------
                # Product Activate / Disable
                # ------------------------------------------------------------------------------------------------------
                response = c.post(url_for("admin_products.disable_product", product_id=Product.count()+1))
                self.assertEqual(response.status_code, 404)

                response = c.post(url_for("admin_products.to_activate_product", product_id=Product.count() + 1))
                self.assertEqual(response.status_code, 404)

                product = Product.get_last()

                response = c.post(url_for("admin_products.disable_product", product_id=product.id))
                self.assertEqual(response.status_code, 200)
                product = Product.get_last()
                self.assertEqual(product.active, False)

                response = c.post(url_for("admin_products.to_activate_product", product_id=product.id))
                self.assertEqual(response.status_code, 200)
                product = Product.get_last()
                self.assertEqual(product.active, True)

                response = c.post(url_for("admin_products.disable_product", product_id=product.id))
                self.assertEqual(response.status_code, 200)
                product = Product.get_last()
                self.assertEqual(product.active, False)

                response = c.post(url_for("admin_products.to_activate_product", product_id=product.id))
                self.assertEqual(response.status_code, 200)
                product = Product.get_last()
                self.assertEqual(product.active, True)

                product = Product.get_last()
                response = c.post(url_for("admin_products.edit_product", product_id=product.id), data=dict(
                    title="a",
                    category_id=str(product.category_id),
                    subcategory_id=str(product.subcategory_id),
                    price="1,42",
                    stock=50,
                    min_available=product.min_available,
                    summary=product.summary,
                    image_1="product_default.jpg",
                    image_2="product_default.jpg",
                    image_3="",
                    image_4="",
                    image_5="",
                    image_6="",
                    image_7="",
                    image_8="",
                    image_9="",
                    image_10=""
                ))
                self.assertEqual(response.status_code, 302)
                product = Product.get_last()
                product.reserved = 10
                db.session.add(product)
                db.session.commit()

                product = Product.get_last()
                self.assertEqual(product.available, 40)

                # ------------------------------------------------------------------------------------------------------
                # Product Stock Add
                # ------------------------------------------------------------------------------------------------------
                response = c.post(url_for("admin_products.product_stock_addition", product_id=product.id), data=dict(
                    value=-10
                ))
                self.assertEqual(response.status_code, 400)

                response = c.post(url_for("admin_products.product_stock_addition", product_id=product.id), data=dict(
                    value=-1
                ))
                self.assertEqual(response.status_code, 400)

                response = c.post(url_for("admin_products.product_stock_addition", product_id=product.id), data=dict(
                    value=0
                ))
                self.assertEqual(response.status_code, 200)
                product = Product.get_last()
                self.assertEqual(product.stock, 50)
                self.assertEqual(product.available, 40)
                self.assertEqual(product.reserved, 10)

                response = c.post(url_for("admin_products.product_stock_addition", product_id=product.id), data=dict(
                    value=1
                ))
                self.assertEqual(response.status_code, 200)
                product = Product.get_last()
                self.assertEqual(product.stock, 51)
                self.assertEqual(product.available, 41)
                self.assertEqual(product.reserved, 10)

                response = c.post(url_for("admin_products.product_stock_addition", product_id=product.id), data=dict(
                    value=10
                ))
                self.assertEqual(response.status_code, 200)
                product = Product.get_last()
                self.assertEqual(product.stock, 61)
                self.assertEqual(product.available, 51)
                self.assertEqual(product.reserved, 10)

                # ------------------------------------------------------------------------------------------------------
                # Product Stock Remove
                # ------------------------------------------------------------------------------------------------------
                response = c.post(url_for("admin_products.product_stock_removal", product_id=product.id), data=dict(
                    value=-10
                ))
                self.assertEqual(response.status_code, 400)
                product = Product.get_last()
                self.assertEqual(product.stock, 61)

                response = c.post(url_for("admin_products.product_stock_removal", product_id=product.id), data=dict(
                    value=-1
                ))
                self.assertEqual(response.status_code, 400)
                product = Product.get_last()
                self.assertEqual(product.stock, 61)

                response = c.post(url_for("admin_products.product_stock_removal", product_id=product.id), data=dict(
                    value=0
                ))
                self.assertEqual(response.status_code, 200)
                product = Product.get_last()
                self.assertEqual(product.stock, 61)
                self.assertEqual(product.available, 51)
                self.assertEqual(product.reserved, 10)

                response = c.post(url_for("admin_products.product_stock_removal", product_id=product.id), data=dict(
                    value=1
                ))
                self.assertEqual(response.status_code, 200)
                product = Product.get_last()
                self.assertEqual(product.stock, 60)
                self.assertEqual(product.available, 50)
                self.assertEqual(product.reserved, 10)

                response = c.post(url_for("admin_products.product_stock_removal", product_id=product.id), data=dict(
                    value=10
                ))
                self.assertEqual(response.status_code, 200)
                product = Product.get_last()
                self.assertEqual(product.stock, 50)
                self.assertEqual(product.available, 40)
                self.assertEqual(product.reserved, 10)

                response = c.post(url_for("admin_products.product_stock_removal", product_id=product.id), data=dict(
                    value=60
                ))
                self.assertEqual(response.status_code, 200)
                product = Product.get_last()
                self.assertEqual(product.stock, 0)
                self.assertEqual(product.available, -10)
                self.assertEqual(product.reserved, 10)

                # ------------------------------------------------------------------------------------------------------
                # Product Stock Update
                # ------------------------------------------------------------------------------------------------------
                response = c.post(url_for("admin_products.product_stock_update", product_id=product.id), data=dict(
                    value=-10
                ))
                self.assertEqual(response.status_code, 400)

                response = c.post(url_for("admin_products.product_stock_update", product_id=product.id), data=dict(
                    value=-1
                ))
                self.assertEqual(response.status_code, 400)

                response = c.post(url_for("admin_products.product_stock_update", product_id=product.id), data=dict(
                    value=0
                ))
                self.assertEqual(response.status_code, 200)
                product = Product.get_last()
                self.assertEqual(product.stock, 0)
                self.assertEqual(product.available, -10)
                self.assertEqual(product.reserved, 10)

                response = c.post(url_for("admin_products.product_stock_update", product_id=product.id), data=dict(
                    value=100
                ))
                self.assertEqual(response.status_code, 200)
                product = Product.get_last()
                self.assertEqual(product.stock, 100)
                self.assertEqual(product.available, 90)
                self.assertEqual(product.reserved, 10)

                response = c.post(url_for("admin_products.product_stock_update", product_id=product.id), data=dict(
                    value=72
                ))
                self.assertEqual(response.status_code, 200)
                product = Product.get_last()
                self.assertEqual(product.stock, 72)
                self.assertEqual(product.available, 62)
                self.assertEqual(product.reserved, 10)
