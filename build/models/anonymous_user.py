# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 13/02/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.base_user import BaseUser


class AnonymousUser(BaseUser):
    @property
    def is_authenticated(self):
        return False

    @property
    def is_active(self):
        return False

    @property
    def is_anonymous(self):
        return True

    def get_id(self):
        return
