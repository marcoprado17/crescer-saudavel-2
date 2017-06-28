from wtforms import fields
from admin.widgets import MarkdownTextWidget


class MarkdownTextField(fields.TextAreaField):
    widget = MarkdownTextWidget()

    def __init__(self, example=None, *args, **kwargs):
        super(MarkdownTextField, self).__init__(*args, **kwargs)
        self.example = example
