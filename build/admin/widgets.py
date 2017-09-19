from flask import render_template


class MarkdownTextWidget:
    def __init__(self):
        pass

    def __call__(self, field, **kwargs):
        print field.description
        return render_template("admin/markdown_text_field.html", field=field)
