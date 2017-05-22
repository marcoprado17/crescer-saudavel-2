from flask_bombril.form_validators.required.required import Required
from models_view.proj_base_view import ProjBaseView
from r import R


class ProductCategoryView(ProjBaseView):
    name = R.string.product_categories
    endpoint = R.string.product_categories_endpoint
    category = R.string.products

    can_delete = False

    column_list = ['active', 'name', 'priority']
    column_filters = ['active']
    column_editable_list = ['name', 'priority', 'active']
    column_descriptions = dict(
        priority=R.string.product_category_priority_tooltip
    )

    form_excluded_columns = ['product_subcategories', 'products']
    form_args = dict(
        priority=dict(
            validators=[Required()]
        )
    )
