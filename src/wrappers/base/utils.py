# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 13/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import os
import markdown

from flask import current_app
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
