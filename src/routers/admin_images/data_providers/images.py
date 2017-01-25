# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import os

from flask import current_app
from flask import url_for

from components.data_providers.paginator import paginator_data_provider
from flask_bombril.url_args import get_valid_page
from flask_bombril.utils import n_pages, slice_items
from proj_forms import SubmitForm
from r import R


class AdminImagesDataProvider(object):
    default_images = [
        "blog_post_thumbnail_default.jpg",
        "carousel_default.jpg",
        "post_exemplo_abobora.jpg",
        "product_default.jpg"
    ]

    def get_data(self):
        self.images_name = os.listdir(current_app.config["UPLOADED_IMAGES_FOLDER_FULL_PATH"])
        self.images_name.sort()
        n_images = len(self.images_name)
        self.per_page = current_app.config["DEFAULT_PER_PAGE"]
        self.curr_page = get_valid_page(page_arg_name=R.string.page_arg_name, per_page=self.per_page, n_items=n_images)
        return dict(
            n_items=n_images,
            paginator_data=paginator_data_provider.get_data(
                min_page=R.dimen.min_page,
                curr_page=self.curr_page,
                max_page=n_pages(per_page=self.per_page, n_items=n_images)
            ),
            table_data=self.get_table_data()
        )

    def get_table_data(self):
        rows = []
        for image_name in slice_items(items=self.images_name, page=self.curr_page, per_page=self.per_page):
            rows.append([
                url_for("static", filename=(current_app.config["UPLOADED_IMAGES_FOLDER"] + "/" + image_name)),
                image_name,
                [
                    dict(
                        type=R.id.ACTION_TYPE_BUTTON,
                        text=R.string.remove,
                        form=SubmitForm(),
                        url=url_for("admin_images.remove_image", image_name=image_name),
                        classes="remove",
                        meta_data={
                            "image-name": image_name
                        }
                    ) if not image_name in self.default_images else
                    dict(
                        type=R.id.ACTION_TYPE_BUTTON,
                        text=R.string.can_not_be_removed,
                        classes="disabled"
                    )
                ]
            ])

        return dict(
            id=R.string.images_table_id,
            cols=[
                dict(
                    id=R.string.image_col_id,
                    type=R.id.COL_TYPE_IMAGE
                ),
                dict(
                    id=R.string.image_name_col_id,
                    title=R.string.name,
                    type=R.id.COL_TYPE_TEXT
                ),
                dict(
                    id=R.string.action_col_id,
                    type=R.id.COL_TYPE_ACTION
                )
            ],
            rows=rows
        )


admin_images_data_provider = AdminImagesDataProvider()
