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

    filename = db.Column(db.String(R.dimen.image_path_max_size), unique=True)

    def html_preview(self):
        if os.path.basename(self.full_path) == config.IMAGES_FOLDER:
            url = url_for("static", filename=os.path.join(config.IMAGES_FOLDER, self.filename))
        else:
            path_from_static = os.path.join(config.IMAGES_FOLDER, os.path.basename(self.full_path))
            url = url_for("static", filename=os.path.join(path_from_static, self.filename))
        return Markup("<img style='max-width: 100px;max-height: 100px;' src='%s'>" % url)

    def delete_file(self):
        image_full_path = os.path.join(self.full_path, self.filename)
        if os.path.exists(image_full_path):
            os.remove(image_full_path)

    def resize(self):
        pass

    def resize_to(self, width, height):
        if not os.path.exists(self.full_path):
            os.makedirs(self.full_path)

        image_full_path = os.path.join(self.full_path, self.filename)
        if os.path.exists(image_full_path):
            image = ImagePIL.open(image_full_path)
            old_width = image.size[0]
            old_height = image.size[1]
            if old_width >= old_height:
                new_height = height
                new_width = int(new_height * float(old_width) / float(old_height))
            else:
                new_width = width
                new_height = int(new_width * float(old_height) / float(old_width))
            image = image.resize((new_width, new_height), ImagePIL.ANTIALIAS)
            left = (new_width - width) / 2
            top = (new_height - height) / 2
            right = (new_width + width) / 2
            bottom = (new_height + height) / 2
            image = image.crop((left, top, right, bottom))
            image.save(image_full_path)
