from os.path import join

from models.blog_thumbnail_image import BlogThumbnailImage
from models_view.image_view import ImageView
from r import R
from configs import default_app_config as config


class BlogThumbnailImageView(ImageView):
    folder_path_from_static = join(config.IMAGES_FOLDER, config.BLOG_THUMBNAIL_IMAGES_FOLDER)
    form_extra_fields = ImageView.build_form_extra_fields(folder_full_path=config.BLOG_THUMBNAIL_IMAGES_FULL_PATH,
                                                          folder_name=config.BLOG_THUMBNAIL_IMAGES_FOLDER,
                                                          model=BlogThumbnailImage,
                                                          field=BlogThumbnailImage.filename)
    name = R.string.blog_thumbnail_images
    endpoint = R.string.blog_thumbnail_images_endpoint
    form_create_rules = ImageView.build_form_create_rules(R.string.ideal_blog_thumbnail_size_auxiliar_text)
