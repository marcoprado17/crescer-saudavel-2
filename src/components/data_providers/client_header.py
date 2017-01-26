# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 25/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from pprint import pprint

from flask import url_for

from models.product_category import ProductCategory
from r import R


class ClientHeaderDataProvider(object):
    def get_data(self):
        return dict(
            logged=False,
            first_name="João",
            menu_data=self.get_menu_data(),
            cart_data=dict(
                n_items=5,
                total_price="R$ 32,60",
                products=[
                    dict(
                        title="Papinha de maça - 500g",
                        href="#",
                        img_src=url_for("static", filename="imgs/product_default.jpg"),
                        quantity=2,
                        unity_price="R$ 10,00"
                    ),
                    dict(
                        title="Papinha de arroz doce - 200g",
                        href="#",
                        img_src=url_for("static", filename="imgs/product_default.jpg"),
                        quantity=3,
                        unity_price="R$ 4,20"
                    )
                ]
            )
        )

    def get_menu_data(self):
        return [
            dict(
                name=R.string.products,
                href=url_for("client_products.products"),
                children=self.get_products_menu_tree()
            ),
            dict(
                name=R.string.blog,
                href=url_for("client_blog.blog"),
            ),
        ]

    def get_products_menu_tree(self):
        menu_tree = []
        for category in ProductCategory.get_all():
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


client_header_data_provider = ClientHeaderDataProvider()
