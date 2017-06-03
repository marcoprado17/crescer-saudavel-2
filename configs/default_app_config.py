# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from os.path import join

DEBUG = False

STATIC_FOLDER = "static"
STATIC_FULL_PATH = "/vagrant/build/static"
IMAGES_FOLDER = "imagens"
IMAGES_FROM_STATIC_PATH = join(STATIC_FOLDER, IMAGES_FOLDER)
IMAGES_FULL_PATH = join(STATIC_FULL_PATH, IMAGES_FOLDER)
OTHER_IMAGES_FOLDER = "outro"
OTHER_IMAGES_FROM_STATIC_PATH = join(IMAGES_FROM_STATIC_PATH, OTHER_IMAGES_FOLDER)
OTHER_IMAGES_FULL_PATH = join(IMAGES_FULL_PATH, OTHER_IMAGES_FOLDER)
MODEL_IMAGES_FOLDER = "modelo"
MODEL_IMAGES_FROM_STATIC_PATH = join(IMAGES_FROM_STATIC_PATH, MODEL_IMAGES_FOLDER)
MODEL_IMAGES_FULL_PATH = join(IMAGES_FULL_PATH, MODEL_IMAGES_FOLDER)

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

# WHOOSH_BASE variable name can't be renamed. It's used by whoosh library like it is.
WHOOSH_BASE = "/vagrant/whoosh_index"
