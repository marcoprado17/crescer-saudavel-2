from models_view.proj_base_view import ProjBaseView
from r import R


class ProductSubcategoryView(ProjBaseView):
    name = R.string.product_subcategories
    endpoint = R.string.product_subcategories_endpoint
    category = R.string.products

    can_delete = False

    column_list = ['active', 'product_category', 'name']
    column_filters = ['active', 'product_category']
    column_editable_list = ['name', 'product_category', 'active']

    form_excluded_columns = ['products']
