from flask_admin.contrib.sqla.ajax import QueryAjaxModelLoader
from flask_admin.form import rules
from markupsafe import Markup
from models.product.product_subcategory import ProductSubcategory
from models_view.content.base_content_view import BaseContentView
from proj_extensions import db
from proj_utils import build_model_image_upload_field
from r import R
from flask_admin.model.ajax import DEFAULT_PAGE_SIZE
from sqlalchemy import or_, and_, cast, String


class QuerySubcategoriesForMoreCategoriesSection(QueryAjaxModelLoader):
    def __init__(self, name):
        super(QuerySubcategoriesForMoreCategoriesSection, self).__init__(name, db.session, ProductSubcategory,
                                                                         fields=["id", "name"])

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


class HomeContentView(BaseContentView):
    # noinspection PyMethodMayBeStatic
    def _carousel_image_formatter(self, _, model, name):
        n = [int(s) for s in name.split('_') if s.isdigit()][0]
        return Markup("<img style='max-width: 256px;max-height: 256px;' src='%s'>" % model.get_carousel_n_img_src(n))

    # noinspection PyMethodMayBeStatic
    def _more_categories_image_formatter(self, _, model, name):
        n = [int(s) for s in name.split('_') if s.isdigit()][0]
        return Markup(
            "<img style='max-width: 128px;max-height: 128px;' src='%s'>" % model.get_more_categories_n_img_src(n))

    name = R.string.home_content
    endpoint = R.string.home_content_endpoint
    category = R.string.content

    can_delete = False
    can_view_details = True

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
    product_section_ajax_dic = {
        "fields": ["title", "id"],
        "page_size": 10
    }
    product_category_ajax_dic = {
        "fields": ["name", "id"],
        "page_size": 10
    }
    blog_post_ajax_dic = {
        "fields": ["title", "id"],
        "page_size": 10
    }

    column_formatters = dict(
        carousel_1_image_filename=_carousel_image_formatter,
        carousel_2_image_filename=_carousel_image_formatter,
        carousel_3_image_filename=_carousel_image_formatter,
        more_categories_section_category_1_image_filename=_more_categories_image_formatter,
        more_categories_section_category_2_image_filename=_more_categories_image_formatter,
        more_categories_section_category_3_image_filename=_more_categories_image_formatter,
        more_categories_section_category_4_image_filename=_more_categories_image_formatter,
        more_categories_section_category_5_image_filename=_more_categories_image_formatter,
        more_categories_section_category_6_image_filename=_more_categories_image_formatter,
    )
    column_list = [
        "carousel_1_active",
        "carousel_1_title",
        "product_section_1_active",
        "product_section_1_name",
        "blog_section_1_active",
        "blog_section_1_name"
    ]

    form_ajax_refs = {
        "products_of_section_1": product_section_ajax_dic,
        "products_of_section_2": product_section_ajax_dic,
        "products_of_section_3": product_section_ajax_dic,
        "products_of_section_4": product_section_ajax_dic,
        "products_of_section_5": product_section_ajax_dic,
        "more_categories_section_category_1": product_category_ajax_dic,
        "more_categories_section_category_1_subcategories": QuerySubcategoriesForMoreCategoriesSection(
            "more_categories_section_category_1_subcategories"),
        "more_categories_section_category_2": product_category_ajax_dic,
        "more_categories_section_category_2_subcategories": QuerySubcategoriesForMoreCategoriesSection(
            "more_categories_section_category_2_subcategories"),
        "more_categories_section_category_3": product_category_ajax_dic,
        "more_categories_section_category_3_subcategories": QuerySubcategoriesForMoreCategoriesSection(
            "more_categories_section_category_3_subcategories"),
        "more_categories_section_category_4": product_category_ajax_dic,
        "more_categories_section_category_4_subcategories": QuerySubcategoriesForMoreCategoriesSection(
            "more_categories_section_category_4_subcategories"),
        "more_categories_section_category_5": product_category_ajax_dic,
        "more_categories_section_category_5_subcategories": QuerySubcategoriesForMoreCategoriesSection(
            "more_categories_section_category_5_subcategories"),
        "more_categories_section_category_6": product_category_ajax_dic,
        "more_categories_section_category_6_subcategories": QuerySubcategoriesForMoreCategoriesSection(
            "more_categories_section_category_6_subcategories"),
        "blog_section_1_post_1": blog_post_ajax_dic,
        "blog_section_1_post_2": blog_post_ajax_dic,
        "blog_section_2_post_1": blog_post_ajax_dic,
        "blog_section_2_post_2": blog_post_ajax_dic,
        "blog_section_3_post_1": blog_post_ajax_dic,
        "blog_section_3_post_2": blog_post_ajax_dic,
    }
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
        ),
        more_categories_section_category_2=dict(
            render_kw={
                "data-determinant-to": "#more_categories_section_category_2_subcategories"
            }
        ),
        more_categories_section_category_2_subcategories=dict(
            render_kw={
                "v0-data-depends-on": "#more_categories_section_category_2",
            }
        ),
        more_categories_section_category_3=dict(
            render_kw={
                "data-determinant-to": "#more_categories_section_category_3_subcategories"
            }
        ),
        more_categories_section_category_3_subcategories=dict(
            render_kw={
                "v0-data-depends-on": "#more_categories_section_category_3",
            }
        ),
        more_categories_section_category_4=dict(
            render_kw={
                "data-determinant-to": "#more_categories_section_category_4_subcategories"
            }
        ),
        more_categories_section_category_4_subcategories=dict(
            render_kw={
                "v0-data-depends-on": "#more_categories_section_category_4",
            }
        ),
        more_categories_section_category_5=dict(
            render_kw={
                "data-determinant-to": "#more_categories_section_category_5_subcategories"
            }
        ),
        more_categories_section_category_5_subcategories=dict(
            render_kw={
                "v0-data-depends-on": "#more_categories_section_category_5",
            }
        ),
        more_categories_section_category_6=dict(
            render_kw={
                "data-determinant-to": "#more_categories_section_category_6_subcategories"
            }
        ),
        more_categories_section_category_6_subcategories=dict(
            render_kw={
                "v0-data-depends-on": "#more_categories_section_category_6",
            }
        ),
    )
    form_extra_fields = dict(
        carousel_1_image_filename=build_model_image_upload_field(
            label=R.dict.column_labels["carousel_1_image_filename"], size=R.dimen.carousel_image_size),
        carousel_2_image_filename=build_model_image_upload_field(
            label=R.dict.column_labels["carousel_2_image_filename"], size=R.dimen.carousel_image_size),
        carousel_3_image_filename=build_model_image_upload_field(
            label=R.dict.column_labels["carousel_3_image_filename"], size=R.dimen.carousel_image_size),
        more_categories_section_category_1_image_filename=build_model_image_upload_field(
            label=R.dict.column_labels["more_categories_section_category_1_image_filename"],
            size=R.dimen.more_categories_image_size),
        more_categories_section_category_2_image_filename=build_model_image_upload_field(
            label=R.dict.column_labels["more_categories_section_category_2_image_filename"],
            size=R.dimen.more_categories_image_size),
        more_categories_section_category_3_image_filename=build_model_image_upload_field(
            label=R.dict.column_labels["more_categories_section_category_3_image_filename"],
            size=R.dimen.more_categories_image_size),
        more_categories_section_category_4_image_filename=build_model_image_upload_field(
            label=R.dict.column_labels["more_categories_section_category_4_image_filename"],
            size=R.dimen.more_categories_image_size),
        more_categories_section_category_5_image_filename=build_model_image_upload_field(
            label=R.dict.column_labels["more_categories_section_category_5_image_filename"],
            size=R.dimen.more_categories_image_size),
        more_categories_section_category_6_image_filename=build_model_image_upload_field(
            label=R.dict.column_labels["more_categories_section_category_6_image_filename"],
            size=R.dimen.more_categories_image_size)
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
            header=R.string.get_additional_categories(1)),
        rules.FieldSet((
            "more_categories_section_category_2",
            "more_categories_section_category_2_subcategories",
            "more_categories_section_category_2_image_filename", rules.HTML(R.string.more_categories_image_text)),
            header=R.string.get_additional_categories(2)),
        rules.FieldSet((
            "more_categories_section_category_3",
            "more_categories_section_category_3_subcategories",
            "more_categories_section_category_3_image_filename", rules.HTML(R.string.more_categories_image_text)),
            header=R.string.get_additional_categories(3)),
        rules.FieldSet((
            "more_categories_section_category_4",
            "more_categories_section_category_4_subcategories",
            "more_categories_section_category_4_image_filename", rules.HTML(R.string.more_categories_image_text)),
            header=R.string.get_additional_categories(4)),
        rules.FieldSet((
            "more_categories_section_category_5",
            "more_categories_section_category_5_subcategories",
            "more_categories_section_category_5_image_filename", rules.HTML(R.string.more_categories_image_text)),
            header=R.string.get_additional_categories(5)),
        rules.FieldSet((
            "more_categories_section_category_6",
            "more_categories_section_category_6_subcategories",
            "more_categories_section_category_6_image_filename", rules.HTML(R.string.more_categories_image_text)),
            header=R.string.get_additional_categories(6)),
        rules.FieldSet((
            "blog_section_1_active",
            "blog_section_1_name",
            "blog_section_1_link",
            "blog_section_1_post_1",
            "blog_section_1_post_2"),
            header=R.string.get_blog_section_n(1)),
        rules.FieldSet((
            "blog_section_2_active",
            "blog_section_2_name",
            "blog_section_2_link",
            "blog_section_2_post_1",
            "blog_section_2_post_2"),
            header=R.string.get_blog_section_n(2)),
        rules.FieldSet((
            "blog_section_3_active",
            "blog_section_3_name",
            "blog_section_3_link",
            "blog_section_3_post_1",
            "blog_section_3_post_2"),
            header=R.string.get_blog_section_n(3))
    )
