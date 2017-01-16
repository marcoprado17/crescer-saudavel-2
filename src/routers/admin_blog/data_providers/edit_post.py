# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 16/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.admin_blog.forms import EditBlogPostForm


class EditPostDataProvider(object):
    def get_data_when_get(self, blog_post):
        edit_post_form = EditBlogPostForm()
        edit_post_form.set_values(blog_post=blog_post)
        return dict(
            edit_post_form=edit_post_form
        )

    def get_data_when_post(self, edit_post_form):
        return dict(
            edit_post_form=edit_post_form
        )


admin_edit_post_data_provider = EditPostDataProvider()
