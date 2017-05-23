# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 20/02/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import url_for

from models.blog.blog_post import BlogPost
from models.product import Product
from r import R


class ClientSearchDataProvider(object):
    def get_data(self, q):
        products = None
        if q != "":
            products = Product.query.whoosh_search(q, or_=True).filter(Product.active == True).all()
            products = sorted(products, key = lambda product: product.is_available_to_client, reverse=True)[0:R.dimen.product_search_limit]

        blog_posts = None
        if q != "":
            blog_posts = BlogPost.query.whoosh_search(q, or_=True, limit=R.dimen.blog_post_search_limit).filter(BlogPost.active == True).all()

        return dict(
            page_heading_data=dict(
                path=[
                    dict(
                        name=R.string.home,
                        href=url_for("client_home.home")
                    ),
                    dict(
                        name=R.string.search
                    )
                ],
                title=R.string.search_for(q)
            ),
            q=q,
            products=products,
            blog_posts=blog_posts
        )

client_search_data_provider = ClientSearchDataProvider()
