# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 16/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.admin_blog.forms import AddBlogPostForm


class AddBlogPostDataProvider(object):
    def get_data_when_get(self):
        return dict(
            add_blog_post_form = AddBlogPostForm()
        )

    def get_data_when_post(self, add_blog_post_form):
        return dict(
            add_blog_post_form = add_blog_post_form
        )


admin_add_blog_post_data_provider = AddBlogPostDataProvider()
