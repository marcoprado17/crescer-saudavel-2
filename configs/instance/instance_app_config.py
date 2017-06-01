# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from db_info import DB_USERNAME, DB_PASSWORD, PRODUCTION_DB_NAME

DEBUG = True

TEMPLATE_FOLDER = "/vagrant/src/admin/templates"

SECRET_KEY = "3c9966fecd6cc8b52faaf9df91a8cd7435186396609ffde1a114c0bc8c17c07b"
EMAIL_TOKEN_SALT = "3c9966fecd6cc8b52faaf9df91a8cd7435186396609ffde1a114c0bc8c17c07b"

SQLALCHEMY_DATABASE_URI = "postgresql://"+DB_USERNAME+":"+DB_PASSWORD+"@localhost/"+PRODUCTION_DB_NAME

MAIL_PASSWORD = "a2b4c6d8e0"

ADMIN_MAIL = "marco.pdsv@gmail.com"

FACEBOOK_APP_ID = "125783674609947"
FACEBOOK_APP_SECRET = "a27cc85ef961847e11436ab1d37468a9"

DEBUG = False
TEMPLATE_FOLDER = '/vagrant/build/templates'
ADMIN_MAIL = 'crescer.saudavel.suporte@gmail.com'

