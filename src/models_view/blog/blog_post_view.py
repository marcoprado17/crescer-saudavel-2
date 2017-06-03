from flask_admin.form import rules
from markupsafe import Markup
from os.path import join
from admin.fields import MarkdownTextField
from models_view.proj_base_view import ProjBaseView
from proj_utils import build_model_image_upload_field
from r import R
from configs import default_app_config as config
from PIL import Image, ImageOps


class BlogPostView(ProjBaseView):
    # noinspection PyMethodParameters, PyUnusedLocal, PyMethodMayBeStatic
    def _tags_formatter(view, context, model, name):
        html = "<div style='max-width: 400px'>"
        for blog_tag in model.tags:
            html += "<span style='margin-right: 6px; margin-bottom: 6px;' class='btn btn-default btn-sm'>"
            html += "%s" % blog_tag.name
            html += "</span>"
        html += "</div>"
        return Markup(html)

    name = R.string.blog_posts
    endpoint = R.string.blog_posts_endpoint
    category = R.string.blog

    can_delete = False

    column_editable_list = ["active"]
    column_filters = ["active", "tags", "date"]
    column_formatters = dict(
        thumbnail_image=lambda view, context, model, name:
        Markup("<img style='max-width: 90px;max-height: 50px;' src='%s'>" % model.get_thumbnail_src()),
        date=lambda view, context, model, name:
        R.string.default_date_format(model.date),
        tags=_tags_formatter
    )
    column_list = ["active", "id", "thumbnail_image", "title", "tags", "date"]
    column_sortable_list = ["active", "id", "title", "date"]

    form_args = dict(
        title=dict(
            render_kw=dict(
                placeholder=R.string.blog_post_title_placeholder
            )
        )
    )
    form_excluded_columns = ["content_html"]
    form_extra_fields = dict(
        thumbnail_filename=build_model_image_upload_field(
            label=R.string.blog_thumbnail_image,
            size=R.dimen.blog_thumbnail_image_size
        ),
        content_markdown=MarkdownTextField(label=R.string.content, example=R.string.blog_post_content_example)
    )
    form_rules = (
        "title",
        "active",
        "date",
        "thumbnail_filename",
        rules.HTML(R.string.blog_thumbnail_text),
        "tags",
        "content_markdown"
    )

    def on_model_change(self, form, model, is_created):
        self.create_wide_thumbnail(model=model)

    @staticmethod
    def create_wide_thumbnail(model):
        if model.has_image(model.thumbnail_filename):
            image = Image.open(join(config.MODEL_IMAGES_FULL_PATH, model.thumbnail_filename))
            image_wide = ImageOps.fit(
                image,
                R.dimen.blog_thumbnail_wide_image_size,
                Image.ANTIALIAS
            )
            with open(join(config.MODEL_IMAGES_FULL_PATH, model.get_thumbnail_wide_filename()), 'wb') as fp:
                image_wide.save(fp, "JPEG")
