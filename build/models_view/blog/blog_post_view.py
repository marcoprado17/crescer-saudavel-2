from flask_admin.form import rules
from markupsafe import Markup
from os.path import join

from models_view.proj_base_view import ProjBaseView
from proj_utils import build_image_upload_field
from r import R
from configs import default_app_config as config
from PIL import Image, ImageOps


class BlogPostView(ProjBaseView):
    name = R.string.blog_posts
    endpoint = R.string.blog_posts_endpoint
    category = R.string.blog

    can_delete = False

    column_editable_list = ["active"]
    column_filters = ["active"]
    column_formatters = dict(
        thumbnail_image=lambda view, context, model, name:
        Markup("<img style='max-width: 90px;max-height: 50px;' src='%s'>" % model.get_thumbnail_src()),
        date=lambda view, context, model, name:
        R.string.default_date_format(model.date)
    )
    column_list = ["active", "thumbnail_image", "title", "date"]

    form_args = dict(
        title=dict(
            render_kw=dict(
                placeholder=R.string.blog_post_title_placeholder
            )
        ),
        summary_markdown=dict(
            render_kw=dict(
                example=R.string.blog_post_summary_example
            )
        ),
        content_markdown=dict(
            render_kw=dict(
                example=R.string.blog_post_content_example
            )
        )
    )
    form_excluded_columns = ["summary_html", "content_html"]
    form_extra_fields = dict(
        thumbnail_filename=build_image_upload_field(
            label=R.string.blog_thumbnail_image,
            full_path=config.BLOG_THUMBNAIL_IMAGES_FULL_PATH,
            folder=config.BLOG_THUMBNAIL_IMAGES_FOLDER,
            width=config.BLOG_THUMBNAIL_IMAGE_WIDTH,
            height=config.BLOG_THUMBNAIL_IMAGE_HEIGHT
        ),
    )
    form_rules = (
        "title",
        "active",
        "date",
        "thumbnail_filename",
        rules.HTML(R.string.blog_thumbnail_text),
        "tags",
        rules.Field("summary_markdown", render_field="additional_fields.markdown_text"),
        rules.Field("content_markdown", render_field="additional_fields.markdown_text"),
    )

    def on_model_change(self, form, model, is_created):
        if model.has_thumbnail_image():
            image = Image.open(join(config.BLOG_THUMBNAIL_IMAGES_FULL_PATH, model.thumbnail_filename))
            image_wide = ImageOps.fit(
                image,
                (config.BLOG_THUMBNAIL_WIDE_IMAGE_WIDTH, config.BLOG_THUMBNAIL_WIDE_IMAGE_HEIGHT),
                Image.ANTIALIAS
            )
            with open(join(config.BLOG_THUMBNAIL_IMAGES_FULL_PATH, model.get_thumbnail_wide_filename()), 'wb') as fp:
                image_wide.save(fp, "JPEG")
