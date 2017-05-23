from flask_admin.form import rules
from models_view.content.base_content_view import BaseContentView
from models_view.proj_base_view import ProjBaseView
from r import R


class FaqView(BaseContentView):
    name = R.string.faq
    endpoint = R.string.faq_endpoint

    column_list = ['content_html']
    column_formatters = dict(
        content_html=ProjBaseView.html_formatter
    )

    form_excluded_columns = ["content_html"]
    form_args = dict(
        content_markdown=dict(
            render_kw=dict(
                example=R.string.faq_content_example
            )
        )
    )
    form_rules = (
        rules.Field('content_markdown', render_field='markdown_text'),
    )
