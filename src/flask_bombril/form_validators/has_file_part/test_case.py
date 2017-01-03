# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 25/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from unittest import TestCase as BaseTestCase

from StringIO import StringIO
from flask_wtf import FlaskForm
from wtforms import FileField

from flask_bombril.form_validators.has_file_part.has_file_part import HasFilePart
from flask_bombril.r import R
from flask_bombril.form_validators.utils import AlwaysError
from app_contexts.unit_test_app import unit_test_app as app


class MockForm(FlaskForm):
    file = FileField(validators=[HasFilePart(input_file_name=R.string.test_file_name)])


class MockFormCustomMessage(FlaskForm):
    file = FileField(validators=[HasFilePart(input_file_name=R.string.test_file_name, message=R.string.test_message)])


class MockFormCustomCallableMessage(FlaskForm):
    file = FileField(
        validators=[HasFilePart(input_file_name=R.string.test_file_name, message=lambda: R.string.test_message)])


class MockFormStopTrue(FlaskForm):
    file = FileField(validators=[HasFilePart(input_file_name=R.string.test_file_name, stop=True), AlwaysError()])


class MockFormStopFalse(FlaskForm):
    file = FileField(validators=[HasFilePart(input_file_name=R.string.test_file_name, stop=False), AlwaysError()])


class TestCase(BaseTestCase):
    def test_valid_input(self):
        with app.test_client() as c:
            c.post("/",
                   buffered=True,
                   content_type="multipart/form-data",
                   data={
                       R.string.test_file_name: (StringIO("hello there"), "hello.txt")
                   })
            form = MockForm()
            self.assertTrue(form.validate_on_submit())

    def test_invalid_input_by_file_part_missing(self):
        with app.test_client() as c:
            c.post("/",
                   buffered=True,
                   content_type="multipart/form-data",
                   data={
                       "abc": (StringIO("hello there"), "hello.txt")
                   })
            form = MockForm()
            self.assertFalse(form.validate_on_submit())

    def test_invalid_input_by_invalid_file_name(self):
        with app.test_client() as c:
            c.post("/",
                   buffered=True,
                   content_type="multipart/form-data",
                   data={
                       R.string.test_file_name: (StringIO("hello there"), "")
                   })
            form = MockForm()
            self.assertFalse(form.validate_on_submit())

    def test_invalid_input_default_message(self):
        with app.test_client() as c:
            c.post("/",
                   buffered=True,
                   content_type="multipart/form-data",
                   data={
                       "abc": (StringIO("hello there"), "hello.txt")
                   })
            form = MockForm()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.file.errors), 1)
            self.assertEqual(form.file.errors[0], R.string.file_part_not_found)

    def test_invalid_input_custom_message(self):
        with app.test_client() as c:
            c.post("/",
                   buffered=True,
                   content_type="multipart/form-data",
                   data={
                       "abc": (StringIO("hello there"), "hello.txt")
                   })
            form = MockFormCustomMessage()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.file.errors), 1)
            self.assertEqual(form.file.errors[0], R.string.test_message)

    def test_invalid_input_custom_callable_message(self):
        with app.test_client() as c:
            c.post("/",
                   buffered=True,
                   content_type="multipart/form-data",
                   data={
                       "abc": (StringIO("hello there"), "hello.txt")
                   })
            form = MockFormCustomCallableMessage()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.file.errors), 1)
            self.assertEqual(form.file.errors[0], R.string.test_message)

    def test_stop_true(self):
        with app.test_client() as c:
            c.post("/",
                   buffered=True,
                   content_type="multipart/form-data",
                   data={
                       "abc": (StringIO("hello there"), "hello.txt")
                   })
            form = MockFormStopTrue()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.file.errors), 1)

    def test_stop_false(self):
        with app.test_client() as c:
            c.post("/",
                   buffered=True,
                   content_type="multipart/form-data",
                   data={
                       "abc": (StringIO("hello there"), "hello.txt")
                   })
            form = MockFormStopFalse()
            self.assertFalse(form.validate_on_submit())
            self.assertEqual(len(form.file.errors), 2)
