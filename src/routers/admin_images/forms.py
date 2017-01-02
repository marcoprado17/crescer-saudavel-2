# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 25/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField

from flask_bombril.form_validators.allowed_file_format import AllowedFileFormat
from flask_bombril.form_validators.has_file_part import HasFilePart
from r import R


class UploadImageForm(FlaskForm):
    allowed_extensions = [R.string.png, R.string.jpg, R.string.jpeg]
    image = FileField(label=R.string.image, validators=[
        HasFilePart(input_file_name="image", message=R.string.no_file_selected),
        AllowedFileFormat(
            input_file_name="image",
            allowed_extensions=allowed_extensions,
            message=R.string.invalid_format(allowed_extensions)
        )
    ])
    submit = SubmitField(label=R.string.upload)
