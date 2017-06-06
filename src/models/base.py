# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from sqlalchemy import desc
from os.path import isfile, join
from configs import default_app_config as config
from proj_extensions import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def count(cls):
        return cls.query.count()

    @classmethod
    def get_last(cls):
        return cls.query.order_by(desc(cls.id)).first()

    # noinspection PyShadowingBuiltins
    @classmethod
    def get(cls, id=None):
        if id is None:
            return cls.query.one()
        else:
            return cls.query.filter_by(id=id).one_or_none()

    @classmethod
    def has_image(cls, image_filename):
        return (image_filename is not None) and \
               isfile(join(config.MODEL_IMAGES_FULL_PATH, image_filename))

    @classmethod
    def get_img_src(cls, image_filename, default_image_filename=None):
        if cls.has_image(image_filename):
            return join("/", config.MODEL_IMAGES_FROM_STATIC_PATH, image_filename)
        elif default_image_filename is not None:
            return join("/", config.IMAGES_FROM_STATIC_PATH, default_image_filename)
        else:
            return ""
