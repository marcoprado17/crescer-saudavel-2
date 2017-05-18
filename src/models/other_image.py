from configs import default_app_config
from models.image import Image


class OtherImage(Image):
    __tablename__ = "other_image"
    full_path = default_app_config.OTHER_IMAGES_FULL_PATH
