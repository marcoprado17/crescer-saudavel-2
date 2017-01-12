# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from db_info import DB_USERNAME, DB_PASSWORD, TEST_DB_NAME

SQLALCHEMY_DATABASE_URI = "postgresql://"+DB_USERNAME+":"+DB_PASSWORD+"@localhost/"+TEST_DB_NAME
WTF_CSRF_ENABLED = False
