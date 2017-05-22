from flask_admin.form import rules
from werkzeug.utils import secure_filename
from models.product_category import ProductCategory
from models_view.proj_base_view import ProjBaseView
from r import R
from flask_admin import form
from configs import default_app_config as config
from os.path import join, splitext
from uuid import uuid4


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
    column_list = ['active', 'title']
    column_filters = ['active']
    column_editable_list = ['title', 'active']
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
        rules.FieldSet(('image_1_filename', 'image_2_filename', 'image_3_filename', 'image_4_filename'),
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
    column_descriptions = dict(
        price=R.string.product_price_description,
        min_available=R.string.min_available_description
    )

    name = R.string.products
    endpoint = R.string.products_endpoint
    category = R.string.products
