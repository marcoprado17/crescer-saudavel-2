from flask_admin.contrib.sqla.ajax import QueryAjaxModelLoader
from flask_admin.form import rules
from flask_admin.model.ajax import DEFAULT_PAGE_SIZE
from markupsafe import Markup
from sqlalchemy import cast, String, or_, and_
from configs import default_app_config as config
from models.product.product_subcategory import ProductSubcategory
from models_view.proj_base_view import ProjBaseView
from proj_extensions import db
from proj_utils import build_image_upload_field
from r import R


class QuerySubcategoriesForCategory(QueryAjaxModelLoader):
    def __init__(self, name):
        super(QuerySubcategoriesForCategory, self).__init__(name, db.session, ProductSubcategory, fields=["id", "name"])

    def get_list(self, term, offset=0, limit=DEFAULT_PAGE_SIZE, v0=None, v1=None, v2=None):
        query = self.session.query(self.model)

        try:
            v0 = int(v0)
        except ValueError:
            return []

        query = query.filter(ProductSubcategory.product_category_id == v0)

        filters = (cast(field, String).ilike(u'%%%s%%' % term) for field in self._cached_fields)
        query = query.filter(or_(*filters))

        if self.filters:
            filters = ["%s.%s" % (self.model.__name__.lower(), value) for value in self.filters]
            query = query.filter(and_(*filters))

        if self.order_by:
            query = query.order_by(self.order_by)

        return query.offset(offset).limit(limit).all()


class ProductView(ProjBaseView):
    name = R.string.products
    endpoint = R.string.products_endpoint
    category = R.string.products

    can_delete = False
    can_view_details = True

    image_upload_field_args = dict(
        full_path=config.PRODUCT_IMAGES_FULL_PATH,
        folder=config.PRODUCT_IMAGES_FOLDER,
        width=config.PRODUCT_IMAGE_WIDTH,
        height=config.PRODUCT_IMAGE_HEIGHT
    )

    column_descriptions = dict(
        price=R.string.product_price_description,
        min_available=R.string.min_available_description,
        reserved=R.string.reserved_description,
    )
    column_details_exclude_list = [
        "summary_markdown",
        "tab_1_content_markdown",
        "tab_2_content_markdown",
        "tab_3_content_markdown",
        "tab_4_content_markdown",
        "tab_5_content_markdown"
    ]
    column_editable_list = ["active", "stock"]
    column_filters = ["active", "category", "subcategory", "price", "stock", "reserved", "min_available"]
    column_formatters = dict(
        image=lambda view, context, model, name:
        Markup("<img style='max-width: 64px;max-height: 64px;' src='%s'>" % model.get_image_n_src(1)),
        image_1_filename=lambda view, context, model, name:
        Markup("<img style='max-width: 64px;max-height: 64px;' src='%s'>" % model.get_image_n_src(1)),
        image_2_filename=lambda view, context, model, name:
        Markup("<img style='max-width: 64px;max-height: 64px;' src='%s'>" % model.get_image_n_src(2)),
        image_3_filename=lambda view, context, model, name:
        Markup("<img style='max-width: 64px;max-height: 64px;' src='%s'>" % model.get_image_n_src(3)),
        image_4_filename=lambda view, context, model, name:
        Markup("<img style='max-width: 64px;max-height: 64px;' src='%s'>" % model.get_image_n_src(4)),
        price_with_discount=lambda view, context, model, name:
        R.string.format_price(model.get_price_with_discount()) if model.has_discount else R.string.empty_symbol,
        price=lambda view, context, model, name:
        R.string.format_price(model.price),
        category=lambda view, context, model, name:
        model.category.name if (model.category is not None) else R.string.empty_symbol,
        subcategory=lambda view, context, model, name:
        model.subcategory.name if (model.subcategory is not None) else R.string.empty_symbol,
        n_units_available=lambda view, context, model, name:
        model.get_n_units_available() if (model.get_n_units_available() is not None) else R.string.empty_symbol,
        summary_html=ProjBaseView.html_formatter,
        tab_1_content_html=ProjBaseView.html_formatter,
        tab_2_content_html=ProjBaseView.html_formatter,
        tab_3_content_html=ProjBaseView.html_formatter,
        tab_4_content_html=ProjBaseView.html_formatter,
        tab_5_content_html=ProjBaseView.html_formatter,
    )
    column_list = [
        "id",
        "active",
        "image",
        "category",
        "subcategory",
        "title",
        "price",
        "price_with_discount",
        "stock",
        "reserved"
    ]
    column_sortable_list = [
        "id",
        "active",
        "title",
        "price",
        "stock",
        "reserved"
    ]

    form_ajax_refs = {
        "category": {
            "fields": ["name", "id"],
            "size": 10
        },
        "subcategory": QuerySubcategoriesForCategory("subcategory")
    }
    form_args = dict(
        title=dict(
            render_kw=dict(
                placeholder=R.string.product_title_placeholder
            )
        ),
        category=dict(
            render_kw={
                "data-determinant-to": "#subcategory"
            }
        ),
        subcategory=dict(
            render_kw={
                "v0-data-depends-on": "#category",
            }
        ),
        price=dict(
            render_kw=dict(
                placeholder=R.string.product_price_placeholder
            )
        ),
        stock=dict(
            render_kw=dict(
                placeholder=R.string.product_stock_quantity_placeholder
            )
        ),
        min_available=dict(
            render_kw=dict(
                placeholder=R.string.product_stop_sell_stock_quantity_placeholder
            )
        ),
        summary_markdown=dict(
            render_kw=dict(
                example=R.string.product_example_summary
            )
        ),
        tab_1_title=dict(
            render_kw=dict(
                placeholder=R.string.tab_title_placeholder
            )
        ),
        tab_1_content_markdown=dict(
            render_kw=dict(
                example=R.string.tab_content_example
            )
        ),
        tab_2_title=dict(
            render_kw=dict(
                placeholder=R.string.tab_title_placeholder
            )
        ),
        tab_2_content_markdown=dict(
            render_kw=dict(
                example=R.string.tab_content_example
            )
        ),
        tab_3_title=dict(
            render_kw=dict(
                placeholder=R.string.tab_title_placeholder
            )
        ),
        tab_3_content_markdown=dict(
            render_kw=dict(
                example=R.string.tab_content_example
            )
        ),
        tab_4_title=dict(
            render_kw=dict(
                placeholder=R.string.tab_title_placeholder
            )
        ),
        tab_4_content_markdown=dict(
            render_kw=dict(
                example=R.string.tab_content_example
            )
        ),
        tab_5_title=dict(
            render_kw=dict(
                placeholder=R.string.tab_title_placeholder
            )
        ),
        tab_5_content_markdown=dict(
            render_kw=dict(
                example=R.string.tab_content_example
            )
        ),
    )
    form_excluded_columns = ["sales_number", "summary_html"]
    form_extra_fields = dict(
        image_1_filename=build_image_upload_field(label=R.string.image_1, **image_upload_field_args),
        image_2_filename=build_image_upload_field(label=R.string.image_2, **image_upload_field_args),
        image_3_filename=build_image_upload_field(label=R.string.image_3, **image_upload_field_args),
        image_4_filename=build_image_upload_field(label=R.string.image_4, **image_upload_field_args),
    )
    form_rules = (
        "active",
        "title",
        "category",
        "subcategory",
        rules.Field("summary_markdown", render_field="markdown_text"),
        "price",
        "has_discount",
        "discount_percentage",
        "stock",
        "min_available",
        rules.FieldSet((
            rules.Text(R.string.product_images_text, escape=False),
            "image_1_filename",
            "image_2_filename",
            "image_3_filename",
            "image_4_filename"),
            header=R.string.images),
        rules.FieldSet(
            ("tab_1_active", "tab_1_title", rules.Field("tab_1_content_markdown", render_field="markdown_text")),
            header=R.string.tab_n(1)),
        rules.FieldSet(
            ("tab_2_active", "tab_2_title", rules.Field("tab_2_content_markdown", render_field="markdown_text")),
            header=R.string.tab_n(2)),
        rules.FieldSet(
            ("tab_3_active", "tab_3_title", rules.Field("tab_3_content_markdown", render_field="markdown_text")),
            header=R.string.tab_n(3)),
        rules.FieldSet(
            ("tab_4_active", "tab_4_title", rules.Field("tab_4_content_markdown", render_field="markdown_text")),
            header=R.string.tab_n(4)),
        rules.FieldSet(
            ("tab_5_active", "tab_5_title", rules.Field("tab_5_content_markdown", render_field="markdown_text")),
            header=R.string.tab_n(5))
    )
