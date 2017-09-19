from models_view.proj_base_view import ProjBaseView
from r import R


class ProductSubcategoryView(ProjBaseView):
    name = R.string.product_subcategories
    endpoint = R.string.product_subcategories_endpoint
    category = R.string.products

    can_delete = False

    column_editable_list = ["name", "active"]
    column_filters = ["active", "product_category"]
    column_formatters = dict(
        product_category=lambda view, context, model, name:
        model.product_category.name
    )
    column_list = ["id", "active", "product_category", "name"]
    column_searchable_list = ["id", "name"]
    column_sortable_list = ["id", "active", "name"]

    form_excluded_columns = ["products"]
