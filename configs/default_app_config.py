# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from os.path import join

DEBUG = False

STATIC_FOLDER = "/vagrant/build/static"
STATIC_FULL_PATH = "/vagrant/build/static"
IMAGES_FOLDER = "imgs"
IMAGES_FULL_PATH = join(STATIC_FULL_PATH, IMAGES_FOLDER)
PRODUCT_IMAGES_FOLDER = "product"
PRODUCT_IMAGES_FULL_PATH = join(IMAGES_FULL_PATH, PRODUCT_IMAGES_FOLDER)
BLOG_THUMBNAIL_IMAGES_FOLDER = "blog-thumbnail"
BLOG_THUMBNAIL_IMAGES_FULL_PATH = join(IMAGES_FULL_PATH, BLOG_THUMBNAIL_IMAGES_FOLDER)
CAROUSEL_IMAGES_FOLDER = "carousel"
CAROUSEL_IMAGES_FULL_PATH = join(IMAGES_FULL_PATH, CAROUSEL_IMAGES_FOLDER)
OTHER_IMAGES_FOLDER = "other"
OTHER_IMAGES_FULL_PATH = join(IMAGES_FULL_PATH, OTHER_IMAGES_FOLDER)


LOGGING_FORMAT = "[ %(levelname)8s | %(asctime)s ] - [ %(pathname)64s | %(funcName)32s | %(lineno)4d ] - %(message)s"
LOGGING_FILENAME = "/vagrant/logs/log"
LOGGING_WHEN = 'D'
LOGGING_INTERVAL = 7
LOGGING_BACKUP_COUNT = 4

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_NATIVE_UNICODE = True

MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 465
MAIL_USERNAME = "crescer.saudavel.suporte@gmail.com"
MAIL_USE_TLS = False
MAIL_USE_SSL = True

UPLOADED_IMAGES_FOLDER = "imgs"
UPLOADED_IMAGES_FOLDER_FULL_PATH = "/vagrant/build/static/imgs"
PRODUCTS_IMAGES_FOLDER_FULL_PATH = "/vagrant/build/static/imgs/products"
BLOG_THUMBNAILS_IMAGES_FOLDER_FULL_PATH = "/vagrant/build/static/imgs/blog_thumbnails"

DEFAULT_PER_PAGE = 20
ORDERS_TABLE_PER_PAGE = 10
CLIENTS_TABLE_PER_PAGE = 10
CLIENT_BLOG_POSTS_PER_PAGE = 3
CLIENT_PRODUCTS_PER_PAGE = 12

PAGINATOR_SIZE = 5

PRODUCT_IMAGE_WIDTH = 600
PRODUCT_IMAGE_HEIGHT = 600
BLOG_THUMBNAIL_IMAGE_WIDTH = 900
BLOG_THUMBNAIL_IMAGE_HEIGHT = 500
CAROUSEL_IMAGE_WIDTH = 2560
CAROUSEL_IMAGE_HEIGHT = 500

WHOOSH_BASE = "/vagrant/search.db"
