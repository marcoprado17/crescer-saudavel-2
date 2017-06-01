# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import request
from r import R


class AdminNavbarDataProvider(object):
    tab_id_by_blueprint = dict(
        admin_attended_cities=R.id.ADMIN_NAVBAR_ATTENDED_CITIES,
        admin_blog=R.id.ADMIN_NAVBAR_BLOG,
        admin_content=R.id.ADMIN_NAVBAR_CONTENT,
        admin_clients=R.id.ADMIN_NAVBAR_CLIENTS,
        admin_home=R.id.ADMIN_NAVBAR_HOME,
        admin_images=R.id.ADMIN_NAVBAR_IMAGES,
        admin_orders=R.id.ADMIN_NAVBAR_ORDERS,
        admin_products=R.id.ADMIN_NAVBAR_PRODUCTS
    )

    def get_data(self):
        return dict(
            active_tab_id=self.tab_id_by_blueprint[request.blueprint]
        )
