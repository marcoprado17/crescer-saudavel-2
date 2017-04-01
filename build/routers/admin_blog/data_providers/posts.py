# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 16/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import current_app
from flask import url_for
from components.data_providers.paginator import paginator_data_provider
from flask_bombril.url_args import get_boolean_url_arg
from flask_bombril.url_args import get_valid_enum
from flask_bombril.url_args import get_valid_page
from flask_bombril.utils import get_page_range
from flask_bombril.utils import n_pages
from proj_forms import SubmitForm
from models.blog_post import BlogPost
from proj_utils import get_sort_methods_data
from r import R
from routers.admin_blog.forms import BlogPostFilterForm


class AdminPostsDataProvider(object):
    def get_data(self):
        active = get_boolean_url_arg(arg_name=R.string.subcategory_active_arg_name, default=True)
        sort_method_id = get_valid_enum(arg_name=R.string.sort_method_arg_name, enum=R.id,
                                        default=R.id.SORT_METHOD_NEWEST, possible_values=BlogPost.sort_method_map.ids)

        self.q = BlogPost.query
        self.q = self.q.filter(BlogPost.active == active)
        self.q = self.q.order_by(*BlogPost.sort_method_map.order(sort_method_id))

        n_posts = self.q.count()

        self.per_page = current_app.config["DEFAULT_PER_PAGE"]
        self.curr_page = get_valid_page(page_arg_name=R.string.page_arg_name, per_page=self.per_page,
                                        n_items=n_posts)

        return dict(
            n_items=n_posts,
            paginator_data=paginator_data_provider.get_data(
                min_page=R.dimen.min_page,
                curr_page=self.curr_page,
                max_page=n_pages(per_page=self.per_page, n_items=n_posts)
            ),
            filter_data=dict(
                filter_form=BlogPostFilterForm(active=active)
            ),
            sort_methods=get_sort_methods_data(
                selected_sort_method_id=sort_method_id,
                sort_method_map=BlogPost.sort_method_map
            ),
            table_data=self.get_table_data()
        )

    def get_table_data(self):
        rows = []
        for idx, blog_post in enumerate(self.q.slice(
                *get_page_range(curr_page=self.curr_page, per_page=self.per_page, min_page=R.dimen.min_page)).all()):
            rows.append([
                "#" + str(blog_post.id),
                blog_post.active,
                blog_post.title,
                blog_post.get_formatted_datetime(),
                [
                    dict(
                        type=R.id.ACTION_TYPE_LINK_BUTTON,
                        text=R.string.preview,
                        classes="preview",
                        href=url_for("admin_blog.post_preview", blog_post_id=blog_post.id),
                        new_tab=True
                    ),
                    dict(
                        type=R.id.ACTION_TYPE_LINK_BUTTON,
                        text=R.string.edit,
                        classes="edit",
                        href=url_for("admin_blog.edit_post", blog_post_id=blog_post.id),
                    ),
                    dict(
                        type=R.id.ACTION_TYPE_ACTIVATE_DISABLE_BUTTON,
                        active=blog_post.active,
                        form=SubmitForm(),
                        meta_data= {
                            "data-active-col-id": "active-col"
                        },
                        to_activate_url=url_for(
                            "admin_blog.to_activate_post", blog_post_id=blog_post.id),
                        to_activate_meta_data={
                            "data-error-msg": R.string.to_activate_post_error(blog_post),
                        },
                        disable_url = url_for(
                                "admin_blog.disable_post", blog_post_id=blog_post.id),
                        disable_meta_data= {
                            "data-error-msg": R.string.disable_post_error(blog_post),
                        }
                    ),
                ]
            ])

        return dict(
            id="posts-table",
            expandable=True,
            cols=[
                dict(
                    id="id",
                    title=R.string.id,
                    type=R.id.COL_TYPE_TEXT
                ),
                dict(
                    id="active-col",
                    title=R.string.active,
                    type=R.id.COL_TYPE_BOOL
                ),
                dict(
                    id="title",
                    title=R.string.title,
                    type=R.id.COL_TYPE_TEXT
                ),
                dict(
                    id="date",
                    title=R.string.date,
                    type=R.id.COL_TYPE_TEXT
                ),
                dict(
                    id=R.string.action_col_id,
                    type=R.id.COL_TYPE_ACTION
                )
            ],
            rows=rows
        )


admin_posts_data_provider = AdminPostsDataProvider()
