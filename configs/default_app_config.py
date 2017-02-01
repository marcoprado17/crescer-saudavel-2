# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================

DEBUG = False

STATIC_FOLDER = None

LOGGING_FORMAT = "[ %(levelname)8s | %(asctime)s ] - [ %(pathname)64s | %(funcName)32s | %(lineno)4d ] - %(message)s"
LOGGING_FILENAME = "/vagrant/logs/log"
LOGGING_WHEN = 'D'
LOGGING_INTERVAL = 7
LOGGING_BACKUP_COUNT = 4

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_NATIVE_UNICODE = True

MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 465
MAIL_USERNAME = "crescer.saudavel.suporte@gmail.com"
MAIL_USE_TLS = False
MAIL_USE_SSL = True

UPLOADED_IMAGES_FOLDER = "imgs"
UPLOADED_IMAGES_FOLDER_FULL_PATH = "/vagrant/build/static/imgs"
PRODUCTS_IMAGES_FOLDER_FULL_PATH = "/vagrant/build/static/imgs/products"

DEFAULT_PER_PAGE = 20
ORDERS_TABLE_PER_PAGE = 10
CLIENTS_TABLE_PER_PAGE = 10
CLIENT_BLOG_POSTS_PER_PAGE = 3
CLIENT_PRODUCTS_PER_PAGE = 12

PAGINATOR_SIZE = 5