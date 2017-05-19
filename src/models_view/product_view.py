from flask_admin.form import rules
from flask_bombril.form_validators.required.required import Required
from flask_bombril.utils.utils import merge_dicts
from models.product_category import ProductCategory
from models_view.proj_base_view import ProjBaseView
from r import R


class ProductView(ProjBaseView):
    @staticmethod
    def get_form_widget_args():
        dynamic_choices_data = dict()
        for product_category in ProductCategory.get_all():
            product_subcategories = []
            for product_subcategory in product_category.product_subcategories:
                product_subcategories.append([str(product_subcategory.id), str(product_subcategory.name)])
            dynamic_choices_data[str(product_category.id)] = product_subcategories
        return dict(
            subcategory={
                "class": "dynamic",
                "dynamic-choices-data": str(dynamic_choices_data).replace('\'', '\"'),
                "determinant-select-id": "category"
            }
        )

    can_delete = False
    column_labels = merge_dicts(ProjBaseView.column_labels)
    column_list = ['active', 'title']
    column_filters = ['active']
    column_editable_list = ['title', 'active']
    form_excluded_columns = ['sales_number', "summary_html"]
    form_args = dict(
        price=dict(
            validators=[Required()]
        ),
        summary_markdown=dict(
            render_kw=dict(
                example=R.string.product_example_summary
            )
        ),
    )
    form_widget_args = get_form_widget_args
    form_rules = (
        'title',
        'active',
        'category',
        'subcategory',
        rules.Field('summary_markdown', render_field='markdown_text'),
        'price',
        'has_discount',
        'discount_percentage',
        'stock',
        'min_available',
        'images'
    )
    column_descriptions = dict(
        price=R.string.product_price_tooltip,
        min_available=R.string.min_available_tooltip
    )

    def __init__(self, *args, **kwargs):
        kwargs["name"] = R.string.products
        kwargs["endpoint"] = R.string.products.lower()
        kwargs["category"] = R.string.products
        super(ProductView, self).__init__(*args, **kwargs)
