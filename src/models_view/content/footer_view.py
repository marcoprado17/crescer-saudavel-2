from admin.fields import MarkdownTextField
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

    form_excluded_columns = ["lower_text_html"]
    form_extra_fields = dict(
        lower_text_markdown=MarkdownTextField(label=R.string.lower_text, example=R.string.lower_text_example),
    )
    form_rules = (
        "lower_text_markdown",
    )
