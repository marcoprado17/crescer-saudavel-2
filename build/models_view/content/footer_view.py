from flask_admin.form import rules
from models_view.content.base_content_view import BaseContentView
from models_view.proj_base_view import ProjBaseView
from r import R


class FooterView(BaseContentView):
    name = R.string.footer
    endpoint = R.string.footer_endpoint

    column_formatters = dict(
        lower_text_html=ProjBaseView.html_formatter
    )
    column_list = ['lower_text_html']

    form_args = dict(
        lower_text_markdown=dict(
            render_kw=dict(
                example=R.string.footer_lower_text_example
            )
        )
    )
    form_excluded_columns = ["lower_text_html"]
    form_rules = (
        rules.Field('lower_text_markdown', render_field='additional_fields.markdown_text'),
    )
