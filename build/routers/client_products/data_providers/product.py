# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 29/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import url_for

from flask.ext.bombril.utils.utils import get_random_sublist
from models.product.product import Product
from r import R


class ClientProductDataProvider(object):
    def get_data(self, product):
        images_src = []
        images_src.append(product.get_main_image_src())
        if product.image_2 is not None and product.image_2 != "": images_src.append(
            url_for("static", filename="imgs/products/" + product.image_2))
        if product.image_3 is not None and product.image_3 != "": images_src.append(
            url_for("static", filename="imgs/products/" + product.image_3))
        if product.image_4 is not None and product.image_4 != "": images_src.append(
            url_for("static", filename="imgs/products/" + product.image_4))
        if product.image_5 is not None and product.image_5 != "": images_src.append(
            url_for("static", filename="imgs/products/" + product.image_5))
        if product.image_6 is not None and product.image_6 != "": images_src.append(
            url_for("static", filename="imgs/products/" + product.image_6))
        if product.image_7 is not None and product.image_7 != "": images_src.append(
            url_for("static", filename="imgs/products/" + product.image_7))
        if product.image_8 is not None and product.image_8 != "": images_src.append(
            url_for("static", filename="imgs/products/" + product.image_8))
        if product.image_9 is not None and product.image_9 != "": images_src.append(
            url_for("static", filename="imgs/products/" + product.image_9))
        if product.image_10 is not None and product.image_10 != "": images_src.append(
            url_for("static", filename="imgs/products/" + product.image_10))

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

        q = Product.query.filter(Product.is_available_to_client == True, Product.id != product.id)
        q = q.filter(Product.category_id == product.category_id)
        products_of_same_category = q.all()
        more_products = get_random_sublist(original_list=products_of_same_category, n=4)
        if product.subcategory:
            q = q.filter(Product.subcategory_id == product.subcategory_id)
            products_of_same_subcategory = q.all()
            if len(products_of_same_subcategory) >= 4:
                more_products = get_random_sublist(original_list=products_of_same_subcategory, n=4)
            else:
                products_of_same_category_but_not_same_subcategory = [x for x in products_of_same_category if x.subcategory_id != product.subcategory_id]
                more_products = products_of_same_subcategory + get_random_sublist(
                    original_list=products_of_same_category_but_not_same_subcategory,
                    n=4 - len(products_of_same_subcategory))

        return dict(
            breadcrumbs=[
                 dict(
                     name=R.string.home,
                     href=url_for("client_home.home")
                 ),
                 dict(
                     name=R.string.products,
                     href=url_for("client_products.products")
                 ),
                 dict(
                     name=product.category.name,
                     href=url_for("client_products.products",
                                  **{R.string.category_id_arg_name: product.category_id})
                 )
            ] + self.get_subcategory_dict(product=product) + [
                 dict(
                     name=product.title
                 )
            ],
            product=product,
            images_src=images_src,
            sections=sections,
            more_products=more_products
        )

    def get_subcategory_dict(self, product):
        if product.subcategory is None:
            return []
        return [
            dict(
                name=product.subcategory.name,
                href=url_for("client_products.products", **{R.string.subcategory_id_arg_name: product.subcategory_id})
            )
        ]


client_product_data_provider = ClientProductDataProvider()
