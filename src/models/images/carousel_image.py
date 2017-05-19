from configs import default_app_config as config
from models.images.image import Image
from os.path import join


class CarouselImage(Image):
    __tablename__ = "carousel_image"
    full_path = config.CAROUSEL_IMAGES_FULL_PATH
    path_from_static = join(config.IMAGES_FOLDER, config.CAROUSEL_IMAGES_FOLDER)

    def resize(self):
        self.resize_to(config.CAROUSEL_IMAGE_HEIGHT, config.CAROUSEL_IMAGE_HEIGHT)
