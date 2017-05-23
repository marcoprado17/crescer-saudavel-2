from os.path import join, splitext
from uuid import uuid4

from flask_admin import form
from flask_admin.form import rules
from markupsafe import Markup
from werkzeug.utils import secure_filename

from configs import default_app_config as config
from models.product.product_category import ProductCategory
from models_view.proj_base_view import ProjBaseView
from r import R


def build_image_upload_field_for_product_images(label):
    def namegen(_, file_data):
        extension = splitext(file_data.filename)[-1]
        return secure_filename(str(uuid4()) + extension)

    return form.ImageUploadField(label,
                                 namegen=namegen,
                                 base_path=config.PRODUCT_IMAGES_FULL_PATH,
                                 size=(config.PRODUCT_IMAGE_WIDTH, config.PRODUCT_IMAGE_HEIGHT),
                                 url_relative_path=join(
                                     config.IMAGES_FOLDER,
                                     config.PRODUCT_IMAGES_FOLDER,
                                     config.PRODUCT_IMAGES_FOLDER))


class ProductView(ProjBaseView):
    def _image_formatter(view, context, model, name):
        return Markup("<img style='max-width: 64px;max-height: 64px;' src='%s'>" % model.get_image_n_src(1))

    def _price_with_discount_formatter(view, context, model, name):
        if model.has_discount:
            return R.string.format_price(model.get_price_with_discount())
        else:
            return R.string.empty_symbol

    def _price_formatter(view, context, model, name):
        return R.string.format_price(model.price)

    def _subcategory_formatter(view, context, model, name):
        if model.subcategory is not None:
            return model.subcategory.name
        else:
            return R.string.empty_symbol

    def _n_units_available_formatter(view, context, model, name):
        n_units_available = model.get_n_units_available()
        if n_units_available is not None:
            return n_units_available
        else:
            return R.string.empty_symbol

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

    name = R.string.products
    endpoint = R.string.products_endpoint
    category = R.string.products

    can_delete = False

    column_list = ['active', 'image', 'category', 'subcategory', 'title', 'price', 'price_with_discount', 'stock', 'reserved', 'n_units_available', 'min_available']
    column_filters = ['active', 'category', 'subcategory', 'price', 'stock', 'reserved', 'min_available']
    column_editable_list = ['active', 'stock']
    column_formatters = dict(
        image=_image_formatter,
        price_with_discount=_price_with_discount_formatter,
        price=_price_formatter,
        subcategory=_subcategory_formatter,
        n_units_available=_n_units_available_formatter
    )
    column_descriptions = dict(
        price=R.string.product_price_description,
        min_available=R.string.min_available_description,
        reserved=R.string.reserved_description,
    )

    form_excluded_columns = ['sales_number', "summary_html"]
    form_args = dict(
        title=dict(
            render_kw=dict(
                placeholder=R.string.product_title_placeholder
            )
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
        rules.FieldSet((rules.Text(R.string.product_images_text, escape=False), 'image_1_filename', 'image_2_filename', 'image_3_filename', 'image_4_filename'),
                       header=R.string.images),
        rules.FieldSet(
            ('tab_1_active', 'tab_1_title', rules.Field('tab_1_content_markdown', render_field='markdown_text')),
            header=R.string.tab_n(1)),
        rules.FieldSet(
            ('tab_2_active', 'tab_2_title', rules.Field('tab_2_content_markdown', render_field='markdown_text')),
            header=R.string.tab_n(2)),
        rules.FieldSet(
            ('tab_3_active', 'tab_3_title', rules.Field('tab_3_content_markdown', render_field='markdown_text')),
            header=R.string.tab_n(3)),
        rules.FieldSet(
            ('tab_4_active', 'tab_4_title', rules.Field('tab_4_content_markdown', render_field='markdown_text')),
            header=R.string.tab_n(4)),
        rules.FieldSet(
            ('tab_5_active', 'tab_5_title', rules.Field('tab_5_content_markdown', render_field='markdown_text')),
            header=R.string.tab_n(5))
    )
    form_extra_fields = dict(
        image_1_filename=build_image_upload_field_for_product_images(R.string.image_1),
        image_2_filename=build_image_upload_field_for_product_images(R.string.image_2),
        image_3_filename=build_image_upload_field_for_product_images(R.string.image_3),
        image_4_filename=build_image_upload_field_for_product_images(R.string.image_4)
    )
