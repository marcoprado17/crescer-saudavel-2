from os.path import join, splitext
from uuid import uuid4
from flask_admin import form
from flask_admin.contrib.sqla.ajax import QueryAjaxModelLoader
from flask_admin.form import rules
from markupsafe import Markup
from werkzeug.utils import secure_filename
from configs import default_app_config as config
from models.product.product_category import ProductCategory
from models.product.product_subcategory import ProductSubcategory
from models_view.content.base_content_view import BaseContentView
from proj_extensions import db
from r import R
from flask_admin.model.ajax import DEFAULT_PAGE_SIZE
from sqlalchemy import or_, and_, cast, String


class QuerySubcategoriesForMoreCategoriesSection(QueryAjaxModelLoader):
    def __init__(self, name):
        super(QuerySubcategoriesForMoreCategoriesSection, self).__init__(name, db.session, ProductSubcategory, fields=["id", "name"])

    def get_list(self, term, offset=0, limit=DEFAULT_PAGE_SIZE, v0=None, v1=None, v2=None):
        query = self.session.query(self.model)

        try:
            v0 = int(v0)
        except:
            return []

        print "v0: " + str(v0)

        query = query.filter(ProductSubcategory.product_category_id == v0)

        filters = (cast(field, String).ilike(u'%%%s%%' % term) for field in self._cached_fields)
        query = query.filter(or_(*filters))

        if self.filters:
            filters = ["%s.%s" % (self.model.__name__.lower(), value) for value in self.filters]
            query = query.filter(and_(*filters))

        if self.order_by:
            query = query.order_by(self.order_by)

        return query.offset(offset).limit(limit).all()


def build_image_upload_field_for_carousel_images(label):
    def namegen(_, file_data):
        extension = splitext(file_data.filename)[-1]
        return secure_filename(str(uuid4()) + extension)

    return form.ImageUploadField(label,
                                 namegen=namegen,
                                 base_path=config.CAROUSEL_IMAGES_FULL_PATH,
                                 size=(config.CAROUSEL_IMAGE_WIDTH, config.CAROUSEL_IMAGE_HEIGHT),
                                 url_relative_path=join(
                                     config.IMAGES_FOLDER,
                                     config.CAROUSEL_IMAGES_FOLDER,
                                     config.CAROUSEL_IMAGES_FOLDER))


def build_image_upload_field_for_more_categories_images(label):
    def namegen(_, file_data):
        extension = splitext(file_data.filename)[-1]
        return secure_filename(str(uuid4()) + extension)

    return form.ImageUploadField(label,
                                 namegen=namegen,
                                 base_path=config.MORE_CATEGORIES_IMAGES_FULL_PATH,
                                 size=(config.MORE_CATEGORIES_IMAGE_WIDTH, config.MORE_CATEGORIES_IMAGE_HEIGHT),
                                 url_relative_path=join(
                                     config.IMAGES_FOLDER,
                                     config.MORE_CATEGORIES_IMAGES_FOLDER,
                                     config.MORE_CATEGORIES_IMAGES_FOLDER))


class HomeContentView(BaseContentView):
    def _carousel_image_formatter(view, context, model, name):
        n = [int(s) for s in name.split('_') if s.isdigit()][0]
        return Markup("<img style='max-width: 256px;max-height: 256px;' src='%s'>" % model.get_carousel_n_img_src(n))

    name = R.string.home_content
    endpoint = R.string.home_content_endpoint
    category = R.string.content

    can_delete = False
    can_view_details = True

    column_list = ["carousel_1_image_filename"]
    column_formatters = dict(
        carousel_1_image_filename=_carousel_image_formatter,
        carousel_2_image_filename=_carousel_image_formatter,
        carousel_3_image_filename=_carousel_image_formatter

    )

    carousel_title_arg = dict(
        render_kw=dict(
            placeholder=R.string.carousel_title_placeholder
        )
    )
    carousel_subtitle_arg = dict(
        render_kw=dict(
            placeholder=R.string.carousel_subtitle_placeholder
        )
    )
    carousel_link_arg = dict(
        render_kw=dict(
            placeholder=R.string.carousel_link_placeholder
        )
    )
    product_section_name_arg = dict(
        render_kw=dict(
            placeholder=R.string.product_section_name_placeholder
        )
    )
    product_section_link_arg = dict(
        render_kw=dict(
            placeholder=R.string.product_section_link_placeholder
        )
    )
    form_args = dict(
        carousel_1_title=carousel_title_arg,
        carousel_2_title=carousel_title_arg,
        carousel_3_title=carousel_title_arg,
        carousel_1_subtitle=carousel_subtitle_arg,
        carousel_2_subtitle=carousel_subtitle_arg,
        carousel_3_subtitle=carousel_subtitle_arg,
        carousel_1_link=carousel_link_arg,
        carousel_2_link=carousel_link_arg,
        carousel_3_link=carousel_link_arg,
        product_section_1_name=product_section_name_arg,
        product_section_1_link=product_section_link_arg,
        more_categories_section_category_1=dict(
            render_kw={
                "data-determinant-to": "#more_categories_section_category_1_subcategories"
            }
        ),
        more_categories_section_category_1_subcategories=dict(
            render_kw={
                "v0-data-depends-on": "#more_categories_section_category_1",
            }
        )
    )
    form_rules = (
        rules.FieldSet((
            "carousel_1_active",
            "carousel_1_title",
            "carousel_1_subtitle",
            "carousel_1_link",
            "carousel_1_image_filename", rules.HTML(R.string.carousel_image_text)),
            header=R.string.get_carousel_n(1)),
        rules.FieldSet((
            "carousel_2_active",
            "carousel_2_title",
            "carousel_2_subtitle",
            "carousel_2_link",
            "carousel_2_image_filename", rules.HTML(R.string.carousel_image_text)),
            header=R.string.get_carousel_n(2)),
        rules.FieldSet((
            "carousel_3_active",
            "carousel_3_title",
            "carousel_3_subtitle",
            "carousel_3_link",
            "carousel_3_image_filename", rules.HTML(R.string.carousel_image_text)),
            header=R.string.get_carousel_n(3)),
        rules.FieldSet((
            "product_section_1_active",
            "product_section_1_name",
            "product_section_1_link",
            "products_of_section_1"),
            header=R.string.get_product_section_n(1)),
        rules.FieldSet((
            "product_section_2_active",
            "product_section_2_name",
            "product_section_2_link",
            "products_of_section_2"),
            header=R.string.get_product_section_n(2)),
        rules.FieldSet((
            "product_section_3_active",
            "product_section_3_name",
            "product_section_3_link",
            "products_of_section_3"),
            header=R.string.get_product_section_n(3)),
        rules.FieldSet((
            "product_section_4_active",
            "product_section_4_name",
            "product_section_4_link",
            "products_of_section_4"),
            header=R.string.get_product_section_n(4)),
        rules.FieldSet((
            "product_section_5_active",
            "product_section_5_name",
            "product_section_5_link",
            "products_of_section_5"),
            header=R.string.get_product_section_n(5)),
        rules.FieldSet((
            "more_categories_section_category_1",
            "more_categories_section_category_1_subcategories",
            "more_categories_section_category_1_image_filename", rules.HTML(R.string.more_categories_image_text)),
            header=R.string.get_additional_categories(1))
    )
    form_extra_fields = dict(
        carousel_1_image_filename=build_image_upload_field_for_carousel_images(R.dict.column_labels["carousel_1_image_filename"]),
        carousel_2_image_filename=build_image_upload_field_for_carousel_images(R.dict.column_labels["carousel_2_image_filename"]),
        carousel_3_image_filename=build_image_upload_field_for_carousel_images(R.dict.column_labels["carousel_3_image_filename"]),
        more_categories_section_category_1_image_filename=build_image_upload_field_for_more_categories_images(R.dict.column_labels["more_categories_section_category_1_image_filename"]),
    )
    product_section_ajax_dic = dict(
        fields=["title", "id"],
        page_size=10
    )
    product_category_ajax_dic = dict(
        fields=["name", "id"],
        page_size=10
    )
    form_ajax_refs = dict(
        products_of_section_1=product_section_ajax_dic,
        products_of_section_2=product_section_ajax_dic,
        products_of_section_3=product_section_ajax_dic,
        products_of_section_4=product_section_ajax_dic,
        products_of_section_5=product_section_ajax_dic,
        more_categories_section_category_1=product_category_ajax_dic,
        more_categories_section_category_1_subcategories=QuerySubcategoriesForMoreCategoriesSection('more_categories_section_category_1_subcategories')
    )
