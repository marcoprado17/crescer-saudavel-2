from models_view.proj_base_view import ProjBaseView
from r import R


class BlogTagView(ProjBaseView):

    name = R.string.blog_tags
    endpoint = R.string.blog_tags_endpoint
    category = R.string.blog

    can_delete = False

    column_list = ['active', 'name']
    column_filters = ['active']
    column_editable_list = ['active']

    form_args = dict(
        name=dict(
            render_kw=dict(
                placeholder=R.string.blog_tag_name_placeholder
            )
        ),
    )
    form_excluded_columns = ['blog_posts']
