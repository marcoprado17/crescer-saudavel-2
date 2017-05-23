from flask_admin.form import rules
from markupsafe import Markup
from werkzeug.utils import secure_filename
from models_view.proj_base_view import ProjBaseView
from r import R
from flask_admin import form
from configs import default_app_config as config
from os.path import join, splitext
from uuid import uuid4


def build_image_upload_field_for_blog_thumbnail_images(label):
    def namegen(_, file_data):
        extension = splitext(file_data.filename)[-1]
        return secure_filename(str(uuid4()) + extension)

    return form.ImageUploadField(label,
                                 namegen=namegen,
                                 base_path=config.BLOG_THUMBNAIL_IMAGES_FULL_PATH,
                                 size=(config.BLOG_THUMBNAIL_IMAGE_WIDTH, config.BLOG_THUMBNAIL_IMAGE_HEIGHT),
                                 url_relative_path=join(
                                     config.IMAGES_FOLDER,
                                     config.BLOG_THUMBNAIL_IMAGES_FOLDER,
                                     config.BLOG_THUMBNAIL_IMAGES_FOLDER))


class BlogPostView(ProjBaseView):
    def _image_formatter(view, context, model, name):
        return Markup("<img style='max-width: 90px;max-height: 50px;' src='%s'>" % model.get_thumbnail_src())

    def _date_formatter(view, context, model, name):
        return R.string.default_date_format(model.date)

    name = R.string.blog_posts
    endpoint = R.string.blog_posts_endpoint
    category = R.string.blog

    can_delete = False

    column_list = ['active', 'image', 'title', 'date']
    column_filters = ['active']
    column_editable_list = ['active']
    column_formatters = dict(
        image=_image_formatter,
        date=_date_formatter
    )

    form_excluded_columns = ['summary_html', "content_html"]
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
    form_rules = (
        'title',
        'active',
        'date',
        'thumbnail_filename',
        rules.Text(R.string.blog_thumbnail_text, escape=False),
        rules.Field('summary_markdown', render_field='markdown_text'),
        rules.Field('content_markdown', render_field='markdown_text'),
    )
    form_extra_fields = dict(
        thumbnail_filename=build_image_upload_field_for_blog_thumbnail_images(R.string.thumbnail),
    )
