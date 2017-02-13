# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 29/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import url_for
from r import R


class ClientProductDataProvider(object):
    def get_data(self, product):
        images_src = []
        images_src.append(product.get_main_image_src())
        if product.image_2 is not None and product.image_2 != "": images_src.append(url_for("static", filename="imgs/products/"+product.image_2))
        if product.image_3 is not None and product.image_3 != "": images_src.append(url_for("static", filename="imgs/products/"+product.image_3))
        if product.image_4 is not None and product.image_4 != "": images_src.append(url_for("static", filename="imgs/products/"+product.image_4))
        if product.image_5 is not None and product.image_5 != "": images_src.append(url_for("static", filename="imgs/products/"+product.image_5))
        if product.image_6 is not None and product.image_6 != "": images_src.append(url_for("static", filename="imgs/products/"+product.image_6))
        if product.image_7 is not None and product.image_7 != "": images_src.append(url_for("static", filename="imgs/products/"+product.image_7))
        if product.image_8 is not None and product.image_8 != "": images_src.append(url_for("static", filename="imgs/products/"+product.image_8))
        if product.image_9 is not None and product.image_9 != "": images_src.append(url_for("static", filename="imgs/products/"+product.image_9))
        if product.image_10 is not None and product.image_10 != "": images_src.append(url_for("static", filename="imgs/products/"+product.image_10))

        sections = []
        if product.tab_1_active:
            sections.append(
                dict(
                    id="1",
                    title=product.tab_1_title,
                    content=product.tab_1_content_html
                )
            )
        if product.tab_2_active:
            sections.append(
                dict(
                    id="2",
                    title=product.tab_2_title,
                    content=product.tab_2_content_html
                )
            )
        if product.tab_3_active:
            sections.append(
                dict(
                    id="3",
                    title=product.tab_3_title,
                    content=product.tab_3_content_html
                )
            )
        if product.tab_4_active:
            sections.append(
                dict(
                    id="4",
                    title=product.tab_4_title,
                    content=product.tab_4_content_html
                )
            )
        if product.tab_5_active:
            sections.append(
                dict(
                    id="5",
                    title=product.tab_5_title,
                    content=product.tab_5_content_html
                )
            )
        if product.tab_6_active:
            sections.append(
                dict(
                    id="6",
                    title=product.tab_6_title,
                    content=product.tab_6_content_html
                )
            )
        if product.tab_7_active:
            sections.append(
                dict(
                    id="7",
                    title=product.tab_7_title,
                    content=product.tab_7_content_html
                )
            )
        if product.tab_8_active:
            sections.append(
                dict(
                    id="8",
                    title=product.tab_8_title,
                    content=product.tab_8_content_html
                )
            )
        if product.tab_9_active:
            sections.append(
                dict(
                    id="9",
                    title=product.tab_9_title,
                    content=product.tab_9_content_html
                )
            )
        if product.tab_10_active:
            sections.append(
                dict(
                    id="10",
                    title=product.tab_10_title,
                    content=product.tab_10_content_html
                )
            )

        return dict(
            page_heading_data=dict(
                path=[
                    dict(
                        name=R.string.home,
                        href=url_for("client_home.home")
                    ),
                    dict(
                        name=R.string.products,
                        href=url_for("client_products.products")
                    ),
                    dict(
                        name=product.title
                    )
                ],
                title=product.title
            ),
            product=product,
            images_src=images_src,
            sections=sections
        )

client_product_data_provider = ClientProductDataProvider()
