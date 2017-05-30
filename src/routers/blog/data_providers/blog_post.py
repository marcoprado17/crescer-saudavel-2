# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 28/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import current_app
from flask import url_for

from flask_bombril.url_args import get_valid_page
from models.blog.blog_post import BlogPost
from r import R


class ClientBlogPostDataProvider(object):
    def get_data(self, blog_post):
        q = BlogPost.query
        q = q.filter(BlogPost.active == True)
        n_active_posts = q.count()
        per_page = current_app.config["CLIENT_BLOG_POSTS_PER_PAGE"]
        page_to_return = get_valid_page(page_arg_name=R.string.page_arg_name, per_page=per_page, n_items=n_active_posts)
        blog_href_to_return = url_for("blog.blog", **{R.string.page_arg_name: page_to_return})
        return dict(
            page_heading_data=dict(
                path=[
                    dict(
                        name=R.string.home,
                        href=url_for("client_home.home")
                    ),
                    dict(
                        name=R.string.blog,
                        href=blog_href_to_return
                    ),
                    dict(
                        name=blog_post.title,
                    )
                ],
                title=blog_post.title,
                blog_post_date = blog_post.get_formatted_datetime()
            ),
            thumbnail_src=url_for("static", filename="imgs/blog_thumbnails/" + blog_post.thumbnail),
            title=blog_post.title,
            blog_href_to_return = blog_href_to_return,
            content=blog_post.content_html
        )

client_blog_post_data_provider = ClientBlogPostDataProvider()
