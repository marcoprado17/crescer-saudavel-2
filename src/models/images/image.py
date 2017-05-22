import os

from flask import url_for
from markupsafe import Markup

from configs import default_app_config as config
from models.base import BaseModel
from proj_extensions import db
from r import R
from PIL import Image as ImagePIL


class Image(BaseModel):
    __abstract__ = True

    full_path = config.IMAGES_FULL_PATH
    path_from_static = config.IMAGES_FOLDER

    filename = db.Column(db.String(R.dimen.filename_max_size))

    def get_html_preview(self):
        return Markup("<img style='max-width: 100px;max-height: 100px;' src='%s'>" % self.get_link())

    def get_link(self):
        return os.path.join("/", config.STATIC_FOLDER, self.path_from_static, self.filename)

    def delete_file(self):
        image_full_path = os.path.join(self.full_path, self.filename)
        if os.path.exists(image_full_path):
            os.remove(image_full_path)
