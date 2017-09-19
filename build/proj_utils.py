# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 13/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import os
import markdown

from flask import current_app
from sqlalchemy import desc
from sqlalchemy.sql.elements import UnaryExpression
from PIL import Image
from proj_exceptions import InvalidSortMapError
from werkzeug.utils import secure_filename
from r import R
from flask_admin import form
from configs import default_app_config as config
from os.path import join, splitext
from uuid import uuid4


def get_image_choices(include_none=False):
    images_name = os.listdir(current_app.config["UPLOADED_IMAGES_FOLDER_FULL_PATH"])
    images_name.sort()
    image_choices = []
    for image_name in images_name:
        image_choices.append((image_name, image_name))
    if include_none:
        image_choices = [("", R.string.none_in_female)] + image_choices
    return image_choices


def parse_markdown(markdown_text):
    markdown_html = markdown.markdown(markdown_text, extensions=['markdown.extensions.tables'])
    markdown_html = markdown_html.replace("<table>", "<table class='table table-bordered table-condensed'>")
    markdown_html = markdown_html.replace("<p><img", "<p class='image-container'><img")
    return markdown_html


def safe_id(element_id):
    if isinstance(element_id, basestring) and element_id == "0":
        return None
    if isinstance(element_id, int) and element_id == 0:
        return None
    return element_id


def safe_string(s):
    if s == None or not isinstance(s, basestring):
        return ""
    return s


def get_sort_methods_data(selected_sort_method_id, sort_method_map):
    sort_method_ids = sort_method_map.ids
    sort_method_names = sort_method_map.names
    sort_method_data = []
    for sort_method_id, sort_method_name in zip(sort_method_ids, sort_method_names):
        sort_method_data.append(
            dict(
                name=sort_method_name,
                value=str(sort_method_id.value),
                selected=sort_method_id==selected_sort_method_id
            )
        )
    return sort_method_data


class SortMethodMap(object):
    def __init__(self, sort_map):
        try:
            assert isinstance(sort_map, list)
            assert len(sort_map) >= 1
            self.ids = []
            self.names = []
            self.order_by_id = {}
            for sort_map_elem in sort_map:
                assert isinstance(sort_map_elem, tuple)
                assert len(sort_map_elem) == 3
                assert isinstance(sort_map_elem[0], R.id)
                self.ids.append(sort_map_elem[0])
                assert isinstance(sort_map_elem[1], basestring)
                self.names.append(sort_map_elem[1])
                assert isinstance(sort_map_elem[2], UnaryExpression)
                self.order_by_id[sort_map_elem[0]] = sort_map_elem[2]
        except:
            raise InvalidSortMapError

    def order(self, sort_method_id):
        return self.order_by_id[sort_method_id], desc("id")


def create_product_image(file_path, file_name):
    products_folder_path = current_app.config['PRODUCTS_IMAGES_FOLDER_FULL_PATH']

    if not os.path.exists(products_folder_path):
        os.makedirs(products_folder_path)

    if os.path.exists(file_path):
        image = Image.open(file_path)
        width = image.size[0]
        height = image.size[1]
        if width >= height:
            new_height = 600
            new_width = int(600 * float(width) / float(height))
        else:
            new_width = 600
            new_height = int(600 * float(height) / float(width))
        image = image.resize((new_width, new_height), Image.ANTIALIAS)
        image = image.crop(
            ((new_width - 600) / 2, (new_height - 600) / 2, (new_width + 600) / 2, (new_height + 600) / 2))
        image.save(os.path.join(os.path.join(products_folder_path, file_name)))

def create_blog_thumbnail_image(file_path, file_name):
    blog_thumbnails_folder_path = current_app.config['BLOG_THUMBNAILS_IMAGES_FOLDER_FULL_PATH']

    if not os.path.exists(blog_thumbnails_folder_path):
        os.makedirs(blog_thumbnails_folder_path)

    if os.path.exists(file_path):
        image = Image.open(file_path)
        width = image.size[0]
        height = image.size[1]
        if float(width)/float(height) >= float(900)/float(500):
            new_height = 500
            new_width = int(width * float(new_height) / float(height))
        else:
            new_width = 900
            new_height = int(height * float(new_width) / float(width))
        image = image.resize((new_width, new_height), Image.ANTIALIAS)
        image = image.crop(
            ((new_width - 900) / 2, (new_height - 500) / 2, (new_width + 900) / 2, (new_height + 500) / 2))
        image.save(os.path.join(os.path.join(blog_thumbnails_folder_path, file_name)))


def generate_uuid_filename(old_filename):
    extension = splitext(old_filename)[-1]
    return secure_filename(str(uuid4()) + extension)


def build_model_image_upload_field(label, size=None):
    def namegen(_, file_data):
        return generate_uuid_filename(file_data.filename)

    return form.ImageUploadField(label,
                                 namegen=namegen,
                                 base_path=config.MODEL_IMAGES_FULL_PATH,
                                 size=size,
                                 url_relative_path=join(
                                     config.IMAGES_FOLDER,
                                     config.MODEL_IMAGES_FOLDER,
                                     config.MODEL_IMAGES_FOLDER))
