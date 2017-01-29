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

from proj_exceptions import InvalidSortMapError
from r import R


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
