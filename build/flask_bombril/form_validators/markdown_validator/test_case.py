# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 05/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from unittest import TestCase as BaseTestCase
from flask_wtf import FlaskForm
from wtforms import Field

from flask_bombril.form_validators.markdown_validator.markdown_validator import MarkdownValidator
from flask_bombril.form_validators.utils import AlwaysError
from app_contexts.unit_test_app import unit_test_app as app
from flask_bombril.r import R


class MockForm(FlaskForm):
    field = Field(validators=[MarkdownValidator()])


class TestCase(BaseTestCase):
    def test_valid_inputs(self):
        with app.test_client() as c:
            c.post("/", data=dict(
                field="""# hello, This is Markdown Live Preview

----
## what is Markdown?
see [Wikipedia](http://en.wikipedia.org/wiki/Markdown)

> Markdown is a lightweight markup language, originally created by John Gruber and Aaron Swartz allowing people "to write using an easy-to-read, easy-to-write plain text format, then convert it to structurally valid XHTML (or HTML)".

----
## usage
1. Write markdown text in this textarea.
2. Click 'HTML Preview' button.

----
## markdown quick reference
# headers

*emphasis*

**strong**

* list

>block quote

    code (4 spaces indent)
[links](http://wikipedia.org)

----
## changelog
* 17-Feb-2013 re-design

----
## thanks
* [markdown-js](https://github.com/evilstreak/markdown-js)
"""
            ))
            form = MockForm()
            self.assertTrue(form.validate_on_submit())
