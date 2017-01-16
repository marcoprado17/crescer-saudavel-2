# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 16/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.admin_blog.forms import AddBlogPostForm


class AddBlogPostDataProvider(object):
    def get_data(self, add_blog_post_form=None):
        if not add_blog_post_form:
            add_blog_post_form = AddBlogPostForm()

        return dict(
            add_blog_post_form = add_blog_post_form
        )

admin_add_blog_post_data_provider = AddBlogPostDataProvider()
