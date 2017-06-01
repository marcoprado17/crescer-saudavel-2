from models_view.content.base_content_view import BaseContentView
from r import R


class HeaderView(BaseContentView):
    name = R.string.header
    endpoint = R.string.header_endpoint

    column_editable_list = ['n_visible_categories']
    column_list = ['n_visible_categories']

    form_args = dict(
        n_visible_categories=dict(
            render_kw=dict(
                placeholder=R.string.n_visible_categories_placeholder
            )
        )
    )
