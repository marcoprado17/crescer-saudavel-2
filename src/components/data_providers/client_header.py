# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 25/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import flash
from flask import url_for

from models.header import Header
from models.product_category import ProductCategory
from proj_decorators import login_or_anonymous
from r import R
from flask_bombril.r import R as bombril_R


class ClientHeaderDataProvider(object):
    @login_or_anonymous
    def get_data(self, base_user):
        carta_data=base_user.get_cart_data()
        cart_update_messages = base_user.get_cart_update_messages()
        for message in cart_update_messages:
            flash(message, bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.info))
        return dict(
            logged=(not base_user.is_anonymous) and base_user.is_authenticated,
            name= getattr(base_user, "name", None),
            menu_data=self.get_menu_data(),
            cart_data=carta_data,
            n_items=base_user.get_n_items(),
            product_total_price_as_string=base_user.get_cart_products_total_as_string(include_rs=True)
        )

    def get_menu_data(self):
        return self.get_products_menu_tree()[0:Header.get().n_visible_categories] + [
            dict(
                name=R.string.others,
                children=self.get_products_menu_tree()
            ),
            dict(
                name=R.string.blog,
                href=url_for("client_blog.blog"),
            ),
        ]

    def get_products_menu_tree(self):
        menu_tree = []
        for category in self.get_product_categories_sorted_by_priority():
            if category.active:
                children = []
                for subcategory in category.subcategories:
                    if subcategory.active:
                        children.append(
                            dict(
                                name=subcategory.name,
                                href=url_for("client_products.products", **{R.string.subcategory_id_arg_name: subcategory.id})
                            )
                        )
                menu_tree.append(
                    dict(
                        name=category.name,
                        href=url_for("client_products.products", **{R.string.category_id_arg_name: category.id}),
                        children=children
                    )
                )
        return menu_tree

    def get_product_categories_sorted_by_priority(self):
        return sorted(ProductCategory.get_all(), key=lambda product_category: product_category.priority, reverse=True)


client_header_data_provider = ClientHeaderDataProvider()
