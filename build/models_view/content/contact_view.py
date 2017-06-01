from flask_admin.form import rules
from models_view.content.base_content_view import BaseContentView
from models_view.proj_base_view import ProjBaseView
from r import R


class ContactView(BaseContentView):
    name = R.string.contact
    endpoint = R.string.contact_endpoint

    can_view_details = True

    column_details_exclude_list = ["address_markdown"]
    column_formatters = dict(
        address_html=ProjBaseView.html_formatter
    )
    column_list = [
        'address_html',
        'tel',
        'email',
        'facebook_active',
        'youtube_active',
        'twitter_active',
        'googleplus_active',
        'pintrest_active'
    ]

    form_args = dict(
        address_markdown=dict(
            render_kw=dict(
                example=R.string.address_example
            )
        ),
        tel=dict(
            render_kw=dict(
                placeholder=R.string.tel_placeholder
            )
        ),
        email=dict(
            render_kw=dict(
                placeholder=R.string.email_placeholder
            )
        ),
        facebook_link=dict(
            render_kw=dict(
                placeholder=R.string.facebook_link_placeholder
            )
        ),
        youtube_link=dict(
            render_kw=dict(
                placeholder=R.string.youtube_link_placeholder
            )
        ),
        twitter_link=dict(
            render_kw=dict(
                placeholder=R.string.twitter_link_placeholder
            )
        ),
        googleplus_link=dict(
            render_kw=dict(
                placeholder=R.string.googleplus_link_placeholder
            )
        ),
        pintrest_link=dict(
            render_kw=dict(
                placeholder=R.string.pintrest_link_placeholder
            )
        )
    )
    form_excluded_columns = ["address_html"]
    form_rules = (
        rules.FieldSet((
            rules.Field('address_markdown', render_field='markdown_text'),
            'tel',
            'email'),
            header=R.string.main_info),
        rules.FieldSet((
            'facebook_active',
            'facebook_link'),
            header=R.string.facebook),
        rules.FieldSet((
            'youtube_active',
            'youtube_link'),
            header=R.string.youtube),
        rules.FieldSet((
            'twitter_active',
            'twitter_link'),
            header=R.string.twitter),
        rules.FieldSet((
            'googleplus_active',
            'googleplus_link'),
            header=R.string.google_plus),
        rules.FieldSet((
            'pintrest_active',
            'pintrest_link'),
            header=R.string.pintrest),
    )
