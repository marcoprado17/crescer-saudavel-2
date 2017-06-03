from markupsafe import Markup
from models_view.content.base_content_view import BaseContentView
from proj_utils import build_image_upload_field
from r import R
from configs import default_app_config as config


class BlogContentView(BaseContentView):
    name = R.string.blog_content
    endpoint = R.string.blog_content_endpoint

    image_upload_field_args = dict(
        full_path=config.TAG_IMAGES_FULL_PATH,
        folder=config.TAG_IMAGES_FOLDER,
        width=config.TAG_IMAGE_WIDTH,
        height=config.TAG_IMAGE_HEIGHT
    )

    column_editable_list = ["main_image_active"]
    column_formatters = dict(
        main_image_filename=lambda view, context, model, name:
        Markup("<img style='max-width: 240px;max-height: 80;' src='%s'>" % model.get_main_image_src())
    )
    column_list = ["main_image_active", "main_image_filename"]

    form_extra_fields = dict(
        main_image_filename=build_image_upload_field(
            label=R.dict.column_labels["main_image_filename"],
            full_path=config.BLOG_CONTENT_IMAGES_FULL_PATH,
            folder=config.BLOG_CONTENT_IMAGES_FOLDER
        )
    )
