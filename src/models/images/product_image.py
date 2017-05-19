from os.path import join

from configs import default_app_config as config
from models.images.image import Image


class ProductImage(Image):
    __tablename__ = "product_image"
    full_path = config.PRODUCT_IMAGES_FULL_PATH
    path_from_static = join(config.IMAGES_FOLDER, config.PRODUCT_IMAGES_FOLDER)

    def resize(self):
        self.resize_to(config.PRODUCT_IMAGE_WIDTH, config.PRODUCT_IMAGE_HEIGHT)
