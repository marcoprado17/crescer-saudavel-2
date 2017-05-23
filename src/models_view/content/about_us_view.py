from flask_admin.form import rules
from models_view.content.base_content_view import BaseContentView
from models_view.proj_base_view import ProjBaseView
from r import R


class AboutUsView(BaseContentView):
    name = R.string.about_us
    endpoint = R.string.about_us_endpoint

    column_list = ['summary_html', 'content_html']
    column_formatters = dict(
        summary_html=ProjBaseView.html_formatter,
        content_html=ProjBaseView.html_formatter
    )

    form_excluded_columns = ['summary_html', "content_html"]
    form_args = dict(
        summary_markdown=dict(
            render_kw=dict(
                example=R.string.about_us_summary_example
            )
        ),
        content_markdown=dict(
            render_kw=dict(
                example=R.string.about_us_content_example
            )
        )
    )
    form_rules = (
        rules.Field('summary_markdown', render_field='markdown_text'),
        rules.Field('content_markdown', render_field='markdown_text'),
    )
