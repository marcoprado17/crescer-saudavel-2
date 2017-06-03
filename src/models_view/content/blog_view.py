from markupsafe import Markup
from models_view.content.base_content_view import BaseContentView
from proj_utils import build_model_image_upload_field
from r import R


class BlogContentView(BaseContentView):
    name = R.string.blog
    endpoint = R.string.blog_content_endpoint

    column_editable_list = ["main_image_active"]
    column_formatters = dict(
        main_image_filename=lambda view, context, model, name:
        Markup("<img style='max-width: 240px;max-height: 80;' src='%s'>" % model.get_main_image_src())
    )
    column_list = ["main_image_active", "main_image_filename"]
    column_descriptions = dict(
        main_image_filename=R.string.blog_main_image_description
    )

    form_extra_fields = dict(
        main_image_filename=build_model_image_upload_field(label=R.dict.column_labels["main_image_filename"])
    )
