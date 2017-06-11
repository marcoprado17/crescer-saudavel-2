from flask_admin.form import rules
from markupsafe import Markup
from models_view.content.base_content_view import BaseContentView
from proj_utils import build_model_image_upload_field
from r import R


class TagsRowView(BaseContentView):
    name = R.string.tags
    endpoint = R.string.tags_endpoint

    can_view_details = True

    tag_title_arg = dict(
        render_kw=dict(
            placeholder=R.string.tag_title_placeholder
        )
    )
    tag_subtitle_arg = dict(
        render_kw=dict(
            placeholder=R.string.tag_subtitle_placeholder
        )
    )

    column_formatters = dict(
        tag_1_image_filename=lambda view, context, model, name:
        Markup("<img style='max-width: 64px;max-height: 64;' src='%s'>" % model.get_tag_n_image_src(1)),
        tag_2_image_filename=lambda view, context, model, name:
        Markup("<img style='max-width: 64px;max-height: 64;' src='%s'>" % model.get_tag_n_image_src(2)),
        tag_3_image_filename=lambda view, context, model, name:
        Markup("<img style='max-width: 64px;max-height: 64;' src='%s'>" % model.get_tag_n_image_src(3)),
        tag_4_image_filename=lambda view, context, model, name:
        Markup("<img style='max-width: 64px;max-height: 64;' src='%s'>" % model.get_tag_n_image_src(4)),
    )
    column_list = ["tag_1_active", "tag_1_image_filename", "tag_1_title", "tag_1_subtitle"]

    form_args = dict(
        tag_1_title=tag_title_arg,
        tag_1_subtitle=tag_subtitle_arg,
        tag_2_title=tag_title_arg,
        tag_2_subtitle=tag_subtitle_arg,
        tag_3_title=tag_title_arg,
        tag_3_subtitle=tag_subtitle_arg,
    )
    form_extra_fields = dict(
        tag_1_image_filename=build_model_image_upload_field(
            label=R.dict.column_labels["tag_1_image_filename"],
            size=R.dimen.tag_image_size
        ),
        tag_2_image_filename=build_model_image_upload_field(
            label=R.dict.column_labels["tag_2_image_filename"],
            size=R.dimen.tag_image_size
        ),
        tag_3_image_filename=build_model_image_upload_field(
            label=R.dict.column_labels["tag_3_image_filename"],
            size=R.dimen.tag_image_size
        ),
        tag_4_image_filename=build_model_image_upload_field(
            label=R.dict.column_labels["tag_4_image_filename"],
            size=R.dimen.tag_image_size
        )
    )
    form_rules = (
        rules.FieldSet((
            "tag_1_active",
            "tag_1_image_filename",
            "tag_1_title",
            "tag_1_subtitle"
        ), header=R.string.tag_n_header(1)),
        rules.FieldSet((
            "tag_2_active",
            "tag_2_image_filename",
            "tag_2_title",
            "tag_2_subtitle"
        ), header=R.string.tag_n_header(2)),
        rules.FieldSet((
            "tag_3_active",
            "tag_3_image_filename",
            "tag_3_title",
            "tag_3_subtitle"
        ), header=R.string.tag_n_header(3)),
        rules.FieldSet((
            "tag_4_active",
            "tag_4_image_filename",
            "tag_4_title",
            "tag_4_subtitle"
        ), header=R.string.tag_n_header(4)),
    )
