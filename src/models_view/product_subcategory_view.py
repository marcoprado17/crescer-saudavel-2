from models_view.proj_base_view import ProjBaseView
from r import R


class ProductSubcategoryView(ProjBaseView):
    can_delete = False

    column_list = ['active', 'product_category', 'name']
    column_filters = ['active', 'product_category']
    column_editable_list = ['name', 'product_category', 'active']

    form_excluded_columns = ['products']

    def __init__(self, *args, **kwargs):
        kwargs["name"] = R.string.product_subcategories
        kwargs["endpoint"] = R.string.product_subcategories.lower().replace(' ', '-')
        kwargs["category"] = R.string.products
        super(ProductSubcategoryView, self).__init__(*args, **kwargs)
