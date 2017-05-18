from configs import default_app_config
from models.image import Image


class BlogThumbnailImage(Image):
    __tablename__ = "blog_thumbnail_image"
    full_path = default_app_config.BLOG_THUMBNAIL_IMAGES_FULL_PATH

    def resize(self):
        self.resize_to(default_app_config.BLOG_THUMBNAIL_IMAGE_WIDTH, default_app_config.BLOG_THUMBNAIL_IMAGE_HEIGHT)
