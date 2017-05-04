# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask_admin import Admin
from flask_login import LoginManager
from flask_cache import Cache
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

bcrypt = Bcrypt()
db = SQLAlchemy()
mail = Mail()
cache = Cache(config={'CACHE_TYPE': 'simple'})
login_manager = LoginManager()
admin = Admin(name='microblog', template_mode='bootstrap3')
