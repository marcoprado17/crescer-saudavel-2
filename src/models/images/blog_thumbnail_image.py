from os.path import join

from configs import default_app_config as config
from models.images.image import Image


class BlogThumbnailImage(Image):
    __tablename__ = "blog_thumbnail_image"
    full_path = config.BLOG_THUMBNAIL_IMAGES_FULL_PATH
    path_from_static = join(config.IMAGES_FOLDER, config.BLOG_THUMBNAIL_IMAGES_FOLDER)

    def resize(self):
        self.resize_to(config.BLOG_THUMBNAIL_IMAGE_WIDTH, config.BLOG_THUMBNAIL_IMAGE_HEIGHT)
