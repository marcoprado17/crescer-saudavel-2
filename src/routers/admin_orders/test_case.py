# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 24/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import os
import shutil
from datetime import datetime
from unittest import TestCase as BaseTestCase

from flask import url_for
from models.product_category import ProductCategory

from app_contexts.app import app
from models.order import Order
from models.product import Product
from models.product.product_subcategory import ProductSubcategory
from models.user import User
from proj_exceptions import InvalidOrderError, InvalidOrderStatusChange
from proj_extensions import db
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
                response = c.post(url_for("admin_products.add_category"), data=dict(
                    category_name="a",
                    active=True,
                ))
                self.assertEqual(response.status_code, 302)
                self.assertEqual(ProductCategory.count(), 1)

                # ------------------------------------------------------------------------------------------------------
                # Add ProductSubcategory
                # ------------------------------------------------------------------------------------------------------
                response = c.post(url_for("admin_products.add_subcategory"), data=dict(
                    category_id="1",
                    subcategory_name="b",
                    active=True,
                ))
                self.assertEqual(response.status_code, 302)
                self.assertEqual(ProductSubcategory.count(), 1)

                # ------------------------------------------------------------------------------------------------------
                # Add Product
                # ------------------------------------------------------------------------------------------------------
                response = c.post(url_for("admin_products.add_product"), data=dict(
                    title="a",
                    active=True,
                    category_id="1",
                    subcategory_id="1",
                    price="1,11",
                    stock=50,
                    min_available=10,
                    summary="summary",
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
                    title="b",
                    active=True,
                    category_id="1",
                    subcategory_id="1",
                    price="1,11",
                    stock=100,
                    min_available=10,
                    summary="summary",
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

                response = c.post(url_for("admin_products.add_product"), data=dict(
                    title="c",
                    active=True,
                    category_id="1",
                    subcategory_id="1",
                    price="1,11",
                    stock=150,
                    min_available=10,
                    summary="summary",
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
                self.assertEqual(Product.count(), 3)

                # ------------------------------------------------------------------------------------------------------
                # Add Client
                # ------------------------------------------------------------------------------------------------------
                client = User(
                    email="a@a.com",
                    email_confirmed=True,
                    authenticated=True,
                    password="secret",
                    register_datetime=datetime.now(),
                )
                db.session.add(client)
                db.session.commit()
                self.assertEqual(User.count(), 1)

                # ------------------------------------------------------------------------------------------------------
                # Add Order
                # ------------------------------------------------------------------------------------------------------
                # Testing invalid orders creation
                with self.assertRaises(InvalidOrderError):
                    Order.create_new(
                        client_id=1,
                        paid_datetime=datetime.now(),
                        amount_by_product_id = {
                            1: 60
                        }
                    )

                with self.assertRaises(InvalidOrderError):
                    Order.create_new(
                        client_id=1,
                        paid_datetime=datetime.now(),
                        amount_by_product_id={
                            1: 0
                        }
                    )

                with self.assertRaises(InvalidOrderError):
                    Order.create_new(
                        client_id=1,
                        paid_datetime=datetime.now(),
                        amount_by_product_id={
                            1: -10
                        }
                    )

                with self.assertRaises(InvalidOrderError):
                    Order.create_new(
                        client_id=1,
                        paid_datetime=datetime.now(),
                        amount_by_product_id={
                            999: 30
                        }
                    )

                # Testing valid order creation
                Order.create_new(
                    client_id=1,
                    paid_datetime=datetime.now(),
                    amount_by_product_id={
                        1: 30
                    }
                )

                product = Product.get(1)
                self.assertEqual(product.stock, 50)
                self.assertEqual(product.reserved, 30)
                self.assertEqual(product.available, 20)

                # Testing invalid orders id
                response = c.post(url_for("admin_orders.mark_as_sent", order_id=Order.count()+1))
                self.assertEqual(response.status_code, 404)
                response = c.post(url_for("admin_orders.unmark_as_sent", order_id=Order.count() + 1))
                self.assertEqual(response.status_code, 404)
                response = c.post(url_for("admin_orders.mark_as_delivered", order_id=Order.count() + 1))
                self.assertEqual(response.status_code, 404)
                response = c.post(url_for("admin_orders.unmark_as_delivered", order_id=Order.count() + 1))
                self.assertEqual(response.status_code, 404)
                response = c.post(url_for("admin_orders.mark_as_canceled", order_id=Order.count() + 1))
                self.assertEqual(response.status_code, 404)
                response = c.post(url_for("admin_orders.mark_as_paid", order_id=Order.count() + 1))
                self.assertEqual(response.status_code, 404)

                # Testing invalid order status change for paid order
                order = Order.get_last()
                self.assertEqual(order.status, R.id.ORDER_STATUS_PAID)

                with self.assertRaises(InvalidOrderStatusChange):
                    c.post(url_for("admin_orders.unmark_as_sent", order_id=order.id))

                with self.assertRaises(InvalidOrderStatusChange):
                    c.post(url_for("admin_orders.mark_as_delivered", order_id=order.id))

                with self.assertRaises(InvalidOrderStatusChange):
                    c.post(url_for("admin_orders.unmark_as_delivered", order_id=order.id))

                with self.assertRaises(InvalidOrderStatusChange):
                    c.post(url_for("admin_orders.mark_as_paid", order_id=order.id))

                response = c.post(url_for("admin_orders.mark_as_canceled", order_id=order.id))
                self.assertEqual(response.status_code, 200)
                product = Product.get(1)
                self.assertEqual(product.stock, 50)
                self.assertEqual(product.reserved, 0)
                self.assertEqual(product.available, 50)

                # Testing invalid order status change for canceled order
                order = Order.get_last()
                self.assertEqual(order.status, R.id.ORDER_STATUS_CANCELED)

                with self.assertRaises(InvalidOrderStatusChange):
                    c.post(url_for("admin_orders.mark_as_sent", order_id=order.id))

                with self.assertRaises(InvalidOrderStatusChange):
                    c.post(url_for("admin_orders.unmark_as_sent", order_id=order.id))

                with self.assertRaises(InvalidOrderStatusChange):
                    c.post(url_for("admin_orders.mark_as_delivered", order_id=order.id))

                with self.assertRaises(InvalidOrderStatusChange):
                    c.post(url_for("admin_orders.unmark_as_delivered", order_id=order.id))

                with self.assertRaises(InvalidOrderStatusChange):
                    c.post(url_for("admin_orders.mark_as_canceled", order_id=order.id))

                response = c.post(url_for("admin_orders.mark_as_paid", order_id=order.id))
                self.assertEqual(response.status_code, 200)
                product = Product.get(1)
                self.assertEqual(product.stock, 50)
                self.assertEqual(product.reserved, 30)
                self.assertEqual(product.available, 20)

                product = Product.get(1)
                self.assertEqual(product.stock, 50)
                response = c.post(url_for("admin_products.product_stock_update", product_id=order.id)
                                  , data = dict(value=10))
                self.assertEqual(product.stock, 10)
                self.assertEqual(response.status_code, 200)

                response = c.post(url_for("admin_orders.mark_as_sent", order_id=order.id))
                self.assertEqual(response.status_code, 409)

                product = Product.get(1)
                self.assertEqual(product.stock, 10)
                response = c.post(url_for("admin_products.product_stock_update", product_id=order.id)
                                  , data=dict(value=50))
                self.assertEqual(product.stock, 50)
                self.assertEqual(response.status_code, 200)

                response = c.post(url_for("admin_orders.mark_as_sent", order_id=order.id))
                self.assertEqual(response.status_code, 200)
                order = Order.get_last()
                product = Product.get(1)
                self.assertEqual(order.status, R.id.ORDER_STATUS_SENT)
                self.assertEqual(product.stock, 20)
                self.assertEqual(product.reserved, 0)
                self.assertEqual(product.available, 20)

                # Testing invalid order status change for sent order
                order = Order.get_last()
                self.assertEqual(order.status, R.id.ORDER_STATUS_SENT)

                with self.assertRaises(InvalidOrderStatusChange):
                    c.post(url_for("admin_orders.mark_as_sent", order_id=order.id))

                with self.assertRaises(InvalidOrderStatusChange):
                    c.post(url_for("admin_orders.unmark_as_delivered", order_id=order.id))

                with self.assertRaises(InvalidOrderStatusChange):
                    c.post(url_for("admin_orders.mark_as_canceled", order_id=order.id))

                with self.assertRaises(InvalidOrderStatusChange):
                    c.post(url_for("admin_orders.mark_as_paid", order_id=order.id))

                response = c.post(url_for("admin_orders.unmark_as_sent", order_id=order.id))
                self.assertEqual(response.status_code, 200)
                order = Order.get_last()
                product = Product.get(1)
                self.assertEqual(order.status, R.id.ORDER_STATUS_PAID)
                self.assertEqual(product.stock, 50)
                self.assertEqual(product.reserved, 30)
                self.assertEqual(product.available, 20)

                response = c.post(url_for("admin_orders.mark_as_sent", order_id=order.id))
                self.assertEqual(response.status_code, 200)
                order = Order.get_last()
                product = Product.get(1)
                self.assertEqual(order.status, R.id.ORDER_STATUS_SENT)
                self.assertEqual(product.stock, 20)
                self.assertEqual(product.reserved, 0)
                self.assertEqual(product.available, 20)

                response = c.post(url_for("admin_orders.mark_as_delivered", order_id=order.id))
                self.assertEqual(response.status_code, 200)
                order = Order.get_last()
                product = Product.get(1)
                self.assertEqual(order.status, R.id.ORDER_STATUS_DELIVERED)
                self.assertEqual(product.stock, 20)
                self.assertEqual(product.reserved, 0)
                self.assertEqual(product.available, 20)

                # Testing invalid order status change for delivered order
                order = Order.get_last()
                self.assertEqual(order.status, R.id.ORDER_STATUS_DELIVERED)

                with self.assertRaises(InvalidOrderStatusChange):
                    c.post(url_for("admin_orders.mark_as_sent", order_id=order.id))

                with self.assertRaises(InvalidOrderStatusChange):
                    c.post(url_for("admin_orders.unmark_as_sent", order_id=order.id))

                with self.assertRaises(InvalidOrderStatusChange):
                    c.post(url_for("admin_orders.mark_as_delivered", order_id=order.id))

                with self.assertRaises(InvalidOrderStatusChange):
                    c.post(url_for("admin_orders.mark_as_canceled", order_id=order.id))

                with self.assertRaises(InvalidOrderStatusChange):
                    c.post(url_for("admin_orders.mark_as_paid", order_id=order.id))

                response = c.post(url_for("admin_orders.unmark_as_delivered", order_id=order.id))
                self.assertEqual(response.status_code, 200)
                order = Order.get_last()
                product = Product.get(1)
                self.assertEqual(order.status, R.id.ORDER_STATUS_SENT)
                self.assertEqual(product.stock, 20)
                self.assertEqual(product.reserved, 0)
                self.assertEqual(product.available, 20)

                # Creating invalid orders with 3 products
                with self.assertRaises(InvalidOrderError):
                    Order.create_new(
                        client_id=1,
                        paid_datetime=datetime.now(),
                        amount_by_product_id = {
                            1: 50,
                            2: 50,
                            3: 50
                        }
                    )

                with self.assertRaises(InvalidOrderError):
                    Order.create_new(
                        client_id=1,
                        paid_datetime=datetime.now(),
                        amount_by_product_id = {
                            1: 10,
                            2: 20,
                            3: 200
                        }
                    )

                with self.assertRaises(InvalidOrderError):
                    Order.create_new(
                        client_id=1,
                        paid_datetime=datetime.now(),
                        amount_by_product_id = {
                            1: 10,
                            2: 20,
                            3: 100,
                            999: 1
                        }
                    )

                with self.assertRaises(InvalidOrderError):
                    Order.create_new(
                        client_id=1,
                        paid_datetime=datetime.now(),
                        amount_by_product_id = {
                            1: 10,
                            2: 20,
                            3: -100,
                        }
                    )

                with self.assertRaises(InvalidOrderError):
                    Order.create_new(
                        client_id=1,
                        paid_datetime=datetime.now(),
                        amount_by_product_id = {
                            1: 10,
                            2: 0,
                            3: 100,
                        }
                    )

                # Creating valid order with 3 products
                product1 = Product.get(1)
                self.assertEqual(product1.stock, 20)
                self.assertEqual(product1.reserved, 0)
                self.assertEqual(product1.available, 20)
                product2 = Product.get(2)
                self.assertEqual(product2.stock, 100)
                self.assertEqual(product2.reserved, 0)
                self.assertEqual(product2.available, 100)
                product3 = Product.get(3)
                self.assertEqual(product3.stock, 150)
                self.assertEqual(product3.reserved, 0)
                self.assertEqual(product3.available, 150)

                Order.create_new(
                    client_id=1,
                    paid_datetime=datetime.now(),
                    amount_by_product_id={
                        1: 10,
                        2: 50,
                        3: 110,
                    }
                )

                product1 = Product.get(1)
                self.assertEqual(product1.stock, 20)
                self.assertEqual(product1.reserved, 10)
                self.assertEqual(product1.available, 10)
                product2 = Product.get(2)
                self.assertEqual(product2.stock, 100)
                self.assertEqual(product2.reserved, 50)
                self.assertEqual(product2.available, 50)
                product3 = Product.get(3)
                self.assertEqual(product3.stock, 150)
                self.assertEqual(product3.reserved, 110)
                self.assertEqual(product3.available, 40)

                order = Order.get(2)
                response = c.post(url_for("admin_orders.mark_as_canceled", order_id=order.id))
                self.assertEqual(response.status_code, 200)

                product1 = Product.get(1)
                self.assertEqual(product1.stock, 20)
                self.assertEqual(product1.reserved, 0)
                self.assertEqual(product1.available, 20)
                product2 = Product.get(2)
                self.assertEqual(product2.stock, 100)
                self.assertEqual(product2.reserved, 0)
                self.assertEqual(product2.available, 100)
                product3 = Product.get(3)
                self.assertEqual(product3.stock, 150)
                self.assertEqual(product3.reserved, 0)
                self.assertEqual(product3.available, 150)

                order = Order.get(2)
                response = c.post(url_for("admin_orders.mark_as_paid", order_id=order.id))
                self.assertEqual(response.status_code, 200)

                product1 = Product.get(1)
                self.assertEqual(product1.stock, 20)
                self.assertEqual(product1.reserved, 10)
                self.assertEqual(product1.available, 10)
                product2 = Product.get(2)
                self.assertEqual(product2.stock, 100)
                self.assertEqual(product2.reserved, 50)
                self.assertEqual(product2.available, 50)
                product3 = Product.get(3)
                self.assertEqual(product3.stock, 150)
                self.assertEqual(product3.reserved, 110)
                self.assertEqual(product3.available, 40)

                order = Order.get(2)
                response = c.post(url_for("admin_orders.mark_as_sent", order_id=order.id))
                self.assertEqual(response.status_code, 200)

                product1 = Product.get(1)
                self.assertEqual(product1.stock, 10)
                self.assertEqual(product1.reserved, 0)
                self.assertEqual(product1.available, 10)
                product2 = Product.get(2)
                self.assertEqual(product2.stock, 50)
                self.assertEqual(product2.reserved, 0)
                self.assertEqual(product2.available, 50)
                product3 = Product.get(3)
                self.assertEqual(product3.stock, 40)
                self.assertEqual(product3.reserved, 0)
                self.assertEqual(product3.available, 40)

                Order.create_new(
                    client_id=1,
                    paid_datetime=datetime.now(),
                    amount_by_product_id={
                        1: 2,
                        2: 7,
                        3: 3,
                    }
                )

                Order.create_new(
                    client_id=1,
                    paid_datetime=datetime.now(),
                    amount_by_product_id={
                        2: 7,
                        3: 8,
                    }
                )

                product1 = Product.get(1)
                self.assertEqual(product1.stock, 10)
                self.assertEqual(product1.reserved, 2)
                self.assertEqual(product1.available, 8)
                product2 = Product.get(2)
                self.assertEqual(product2.stock, 50)
                self.assertEqual(product2.reserved, 14)
                self.assertEqual(product2.available, 36)
                product3 = Product.get(3)
                self.assertEqual(product3.stock, 40)
                self.assertEqual(product3.reserved, 11)
                self.assertEqual(product3.available, 29)

                order = Order.get(3)
                response = c.post(url_for("admin_orders.mark_as_sent", order_id=order.id))
                self.assertEqual(response.status_code, 200)

                order = Order.get(4)
                response = c.post(url_for("admin_orders.mark_as_sent", order_id=order.id))
                self.assertEqual(response.status_code, 200)

                product1 = Product.get(1)
                self.assertEqual(product1.stock, 8)
                self.assertEqual(product1.reserved, 0)
                self.assertEqual(product1.available, 8)
                product2 = Product.get(2)
                self.assertEqual(product2.stock, 36)
                self.assertEqual(product2.reserved, 0)
                self.assertEqual(product2.available, 36)
                product3 = Product.get(3)
                self.assertEqual(product3.stock, 29)
                self.assertEqual(product3.reserved, 0)
                self.assertEqual(product3.available, 29)
