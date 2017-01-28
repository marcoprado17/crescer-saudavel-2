# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 27/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import current_app
from flask import url_for
from sqlalchemy import desc
from components.data_providers.paginator import paginator_data_provider
from flask_bombril.utils import n_pages
from flask_bombril.utils import get_page_range
from flask_bombril.url_args import get_valid_page
from models.blog_post import BlogPost
from r import R


class BlogDataProvider(object):
    def get_data(self):
        q = BlogPost.query
        q = q.filter(BlogPost.active == True)
        q = q.order_by(desc(BlogPost.datetime), desc("id"))

        n_active_posts = q.count()

        per_page = current_app.config["CLIENT_BLOG_POSTS_PER_PAGE"]
        curr_page = get_valid_page(page_arg_name=R.string.page_arg_name, per_page=per_page, n_items=n_active_posts)

        data = dict(
            page_heading_data=dict(
                path=[
                    dict(
                        name=R.string.home,
                        href=url_for("client_home.home")
                    ),
                    dict(
                        name=R.string.blog,
                        href=url_for("client_blog.blog")
                    )
                ],
                title=R.string.blog
            ),
            paginator_data=paginator_data_provider.get_data(
                min_page=R.dimen.min_page,
                curr_page=curr_page,
                max_page=n_pages(per_page=per_page, n_items=n_active_posts)
            ),
            posts=q.slice(*get_page_range(curr_page=curr_page, per_page=per_page, min_page=R.dimen.min_page)).all()
        )
        return data

blog_data_provider = BlogDataProvider()
