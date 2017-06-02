from admin.fields import MarkdownTextField
from models_view.content.base_content_view import BaseContentView
from models_view.proj_base_view import ProjBaseView
from r import R


class AboutUsView(BaseContentView):
    name = R.string.about_us
    endpoint = R.string.about_us_endpoint

    column_formatters = dict(
        summary_html=ProjBaseView.html_formatter,
        content_html=ProjBaseView.html_formatter
    )
    column_list = ['summary_html', 'content_html']

    form_excluded_columns = ['summary_html', "content_html"]
    form_extra_fields = dict(
        summary_markdown=MarkdownTextField(label=R.string.summary, example=R.string.about_us_summary_example),
        content_markdown=MarkdownTextField(label=R.string.content, example=R.string.about_us_content_example)
    )
    form_rules = (
        "summary_markdown",
        "content_markdown"
    )
