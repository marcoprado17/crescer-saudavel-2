from configs import default_app_config
from models.image import Image


class CarouselImage(Image):
    __tablename__ = "carousel_image"
    full_path = default_app_config.CAROUSEL_IMAGES_FULL_PATH

    def resize(self):
        self.resize_to(default_app_config.CAROUSEL_IMAGE_HEIGHT, default_app_config.CAROUSEL_IMAGE_HEIGHT)
