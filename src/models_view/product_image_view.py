from os.path import join
from models.product_image import ProductImage
from models_view.image_view import ImageView
from r import R
from configs import default_app_config as config


class ProductImageView(ImageView):
    folder_path_from_static = join(config.IMAGES_FOLDER, config.PRODUCT_IMAGES_FOLDER)
    form_extra_fields = ImageView.build_form_extra_fields(folder_full_path=config.PRODUCT_IMAGES_FULL_PATH,
                                                          folder_name=config.PRODUCT_IMAGES_FOLDER,
                                                          model=ProductImage,
                                                          field=ProductImage.filename)
    name = R.string.product_images
    endpoint = R.string.product_images_endpoint
    form_create_rules = ImageView.build_form_create_rules(R.string.ideal_product_image_size_auxiliar_text)
