from os.path import join

from configs import default_app_config as config
from models.images.other_image import OtherImage
from models_view.images.image_view import ImageView
from r import R


class OtherImageView(ImageView):
    folder_path_from_static = join(config.IMAGES_FOLDER, config.OTHER_IMAGES_FOLDER)
    form_extra_fields = ImageView.build_form_extra_fields(folder_full_path=config.OTHER_IMAGES_FULL_PATH,
                                                          folder_name=config.OTHER_IMAGES_FOLDER,
                                                          model=OtherImage,
                                                          field=OtherImage.filename)
    name = R.string.other_images
    endpoint = R.string.other_images_endpoint
