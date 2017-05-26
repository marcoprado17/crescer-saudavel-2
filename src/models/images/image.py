import os

from configs import default_app_config as config
from models.base import BaseModel
from proj_extensions import db
from r import R


class Image(BaseModel):
    __abstract__ = True

    full_path = config.IMAGES_FULL_PATH
    path_from_static = config.IMAGES_FOLDER

    filename = db.Column(db.String(R.dimen.filename_max_size), unique=True, nullable=False)

    def get_src(self):
        return os.path.join("/", "static", self.path_from_static, self.filename)

    def delete_file(self):
        image_full_path = os.path.join(self.full_path, self.filename)
        if os.path.exists(image_full_path):
            os.remove(image_full_path)
