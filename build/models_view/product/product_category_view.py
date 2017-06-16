from markupsafe import Markup

from flask_bombril.form_validators.required.required import Required
from models_view.proj_base_view import ProjBaseView
from proj_utils import build_model_image_upload_field
from r import R


class ProductCategoryView(ProjBaseView):
    name = R.string.product_categories
    endpoint = R.string.product_categories_endpoint
    category = R.string.products

    can_delete = False

    column_descriptions = dict(
        priority=R.string.product_category_priority_tooltip,
        icon_filename=R.string.menu_icon_tooltip(R.dimen.menu_icon_size)
    )
    column_editable_list = ["name", "priority", "active"]
    column_filters = ["active"]
    column_formatters = dict(
        icon_filename=lambda view, context, model, name:
        Markup("<img style='max-width: 24px;max-height: 24px;' src='%s'>" % model.get_menu_icon_image_src())
    )
    column_list = ["id", "active", "icon_filename", "name", "priority"]
    column_sortable_list = ["id", "active", "name", "priority"]

    form_args = dict(
        priority=dict(
            validators=[Required()]
        )
    )
    form_columns = ["active", "name", "icon_filename", "priority"]
    form_excluded_columns = ["product_subcategories", "products"]
    form_extra_fields = dict(
        icon_filename=build_model_image_upload_field(label=R.string.menu_icon, size=R.dimen.menu_icon_size)
    )
