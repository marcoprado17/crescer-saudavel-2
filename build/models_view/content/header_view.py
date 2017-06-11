from markupsafe import Markup

from models_view.content.base_content_view import BaseContentView
from proj_utils import build_model_image_upload_field
from r import R


class HeaderContentView(BaseContentView):
    name = R.string.header
    endpoint = R.string.header_endpoint

    column_editable_list = ["n_visible_categories"]
    column_formatters = dict(
        logo=lambda view, context, model, name:
        Markup("<img style='max-width: 150px;max-height: 50px;' src='%s'>" % model.get_logo_img_src()),
    )
    column_list = ["n_visible_categories", "logo"]

    form_args = dict(
        n_visible_categories=dict(
            render_kw=dict(
                placeholder=R.string.n_visible_categories_placeholder
            )
        )
    )
    form_extra_fields = dict(
        logo_image_filename=build_model_image_upload_field(label=R.string.logo_image)
    )
