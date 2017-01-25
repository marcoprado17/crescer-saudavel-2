# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 25/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import url_for


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
                name="Produtos",
                href="#",
                children=[
                    dict(
                        name="Frutas",
                        href="#",
                    ),
                    dict(
                        name="Sopa creme",
                        href="#",
                    ),
                    dict(
                        name="Sopa com pedaços",
                        href="#",
                    ),
                    dict(
                        name="Linha Single",
                        href="#",
                        children=[
                            dict(
                                name="Sobremesas",
                                href="#",
                            ),
                        ]
                    ),
                    dict(
                        name="Linha Emporinho",
                        href="#",
                        children=[
                            dict(
                                name="Risotos",
                                href="#",
                            ),
                            dict(
                                name="Massas",
                                href="#",
                            ),
                            dict(
                                name="Escondidinhos",
                                href="#",
                            ),
                            dict(
                                name="Arroz",
                                href="#",
                            ),
                            dict(
                                name="Legumes",
                                href="#",
                            ),
                            dict(
                                name="Sopas/Cremes",
                                href="#",
                            ),
                            dict(
                                name="Refeições combinadas",
                                href="#",
                            ),
                        ]
                    ),
                    dict(
                        name="Acessórios",
                        href="#",
                    ),
                ]
            ),
            dict(
                name="Blog",
                href="#",
            ),
        ]


client_header_data_provider = ClientHeaderDataProvider()
