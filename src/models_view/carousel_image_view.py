from os.path import join

from models.carousel_image import CarouselImage
from models.product_image import ProductImage
from models_view.image_view import ImageView
from r import R
from configs import default_app_config as config


class CarouselImageView(ImageView):
    folder_path_from_static = join(config.IMAGES_FOLDER, config.CAROUSEL_IMAGES_FOLDER)
    form_extra_fields = ImageView.build_form_extra_fields(folder_full_path=config.CAROUSEL_IMAGES_FULL_PATH,
                                                          folder_name=config.CAROUSEL_IMAGES_FOLDER,
                                                          model=CarouselImage,
                                                          field=CarouselImage.filename)
    name = R.string.carousel_images
    endpoint = R.string.carousel_images_endpoint
    form_create_rules = ImageView.build_form_create_rules(R.string.ideal_carousel_images_size_auxiliar_text)
