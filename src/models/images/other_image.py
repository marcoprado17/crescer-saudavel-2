from configs import default_app_config as config
from models.images.image import Image
from os.path import join


class OtherImage(Image):
    __tablename__ = "other_image"
    full_path = config.OTHER_IMAGES_FULL_PATH
    path_from_static = join(config.IMAGES_FOLDER, config.OTHER_IMAGES_FOLDER)
