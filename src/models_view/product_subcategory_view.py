from flask_bombril.utils.utils import merge_dicts
from models.base import ProjBaseView
from r import R


class ProductSubcategoryView(ProjBaseView):
    column_labels = merge_dicts(ProjBaseView.column_labels, dict(active=R.string.active_in_female))
    column_list = ['active', 'name', 'product_category']
    column_filters = ['active', 'product_category']
    column_editable_list = ['name', 'product_category', 'active']
    form_excluded_columns = ['products']

    def __init__(self, *args, **kwargs):
        kwargs["name"] = R.string.product_subcategories
        kwargs["endpoint"] = R.string.product_subcategories.lower().replace(' ', '-')
        kwargs["category"] = R.string.products
        super(ProductSubcategoryView, self).__init__(*args, **kwargs)
