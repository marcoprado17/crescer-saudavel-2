from configs import default_app_config
from models.image import Image


class ProductImage(Image):
    __tablename__ = "product_image"
    full_path = default_app_config.PRODUCT_IMAGES_FULL_PATH

    def resize(self):
        self.resize_to(default_app_config.PRODUCT_IMAGE_WIDTH, default_app_config.PRODUCT_IMAGE_HEIGHT)
