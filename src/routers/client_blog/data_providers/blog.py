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
        q = q.order_by(desc(BlogPost.datetime))

        n_active_posts = q.count()

        per_page = current_app.config["CLIENT_BLOG_POSTS_PER_PAGE"]
        curr_page = get_valid_page(page_arg_name=R.string.page_arg_name, per_page=per_page,
                                        n_items=n_active_posts)

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

    def get_page_heading_data(self):
        return {
            "path": [
                {
                    "name": "Home",
                    "href": "#",
                },
                {
                    "name": "Blog",
                },
            ],
            "title": "Blog",
        }

    def sample_data_0(self, page):
        data = {
            "page_heading_data": self.get_page_heading_data(),
            # posts list contains only the the posts of this page
            "posts": [
                {
                    "id": 1,
                    "title": "Lorem ipsum dolor sit amet",
                    "date": "15/10/2016",
                    "thumbnail_href": url_for("static", filename="imgs/blog_post_thumbnail_default.jpg"),
                    "summary": """
                        <p>Fusce ac pharetra urna. Duis non lacus sit amet lacus interdum facilisis sed non est. Ut mi metus, semper eu dictum nec, condimentum sed sapien. Nullam lobortis nunc semper ipsum luctus ut viverra ante eleifend. Nunc pretium velit sed augue luctus accumsan.</p>
                        <p>Quisque nisl lectus, accumsan et euismod eu, sollicitudin ac augue. In sit amet urna magna. Curabitur imperdiet urna nec purus egestas eget aliquet purus iaculis. Nunc porttitor blandit imperdiet. Nulla facilisi. Cras odio ipsum, vehicula nec vehicula sed, convallis scelerisque quam. Phasellus ut odio dui, ut fermentum neque.</p>
                    """,
                },
                {
                    "id": 1,
                    "title": "Lorem ipsum dolor sit amet",
                    "date": "15/10/2016",
                    "thumbnail_href": url_for("static", filename="imgs/blog_post_thumbnail_default.jpg"),
                    "summary": """
                        <p>Fusce ac pharetra urna. Duis non lacus sit amet lacus interdum facilisis sed non est. Ut mi metus, semper eu dictum nec, condimentum sed sapien. Nullam lobortis nunc semper ipsum luctus ut viverra ante eleifend. Nunc pretium velit sed augue luctus accumsan.</p>
                        <p>Quisque nisl lectus, accumsan et euismod eu, sollicitudin ac augue. In sit amet urna magna. Curabitur imperdiet urna nec purus egestas eget aliquet purus iaculis. Nunc porttitor blandit imperdiet. Nulla facilisi. Cras odio ipsum, vehicula nec vehicula sed, convallis scelerisque quam. Phasellus ut odio dui, ut fermentum neque.</p>
                    """,
                },
                {
                    "id": 1,
                    "title": "Lorem ipsum dolor sit amet",
                    "date": "15/10/2016",
                    "thumbnail_href": url_for("static", filename="imgs/blog_post_thumbnail_default.jpg"),
                    "summary": """
                        <p>Fusce ac pharetra urna. Duis non lacus sit amet lacus interdum facilisis sed non est. Ut mi metus, semper eu dictum nec, condimentum sed sapien. Nullam lobortis nunc semper ipsum luctus ut viverra ante eleifend. Nunc pretium velit sed augue luctus accumsan.</p>
                        <p>Quisque nisl lectus, accumsan et euismod eu, sollicitudin ac augue. In sit amet urna magna. Curabitur imperdiet urna nec purus egestas eget aliquet purus iaculis. Nunc porttitor blandit imperdiet. Nulla facilisi. Cras odio ipsum, vehicula nec vehicula sed, convallis scelerisque quam. Phasellus ut odio dui, ut fermentum neque.</p>
                    """,
                },
            ],
        }
        return data


blog_data_provider = BlogDataProvider()
