from flask_bombril.form_validators.required.required import Required
from flask_bombril.utils.utils import merge_dicts
from models.base import ProjBaseView
from r import R


class ProductCategoryView(ProjBaseView):
    can_delete = False
    column_labels = merge_dicts(ProjBaseView.column_labels, dict(active=R.string.active_in_female))
    column_list = ['active', 'name', 'priority']
    column_filters = ['active']
    column_editable_list = ['name', 'priority', 'active']
    form_excluded_columns = ['product_subcategories', 'products']
    form_args = dict(
        priority=dict(
            validators=[Required()]
        )
    )
    column_descriptions = dict(
        priority=R.string.product_category_priority_tooltip
    )

    def __init__(self, *args, **kwargs):
        kwargs["name"] = R.string.product_categories
        kwargs["endpoint"] = R.string.product_categories.lower().replace(' ', '-')
        kwargs["category"] = R.string.products
        super(ProductCategoryView, self).__init__(*args, **kwargs)
