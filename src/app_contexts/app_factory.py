# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import random
import string
import sys

from flask import session

from models.blog.blog_post import BlogPost
from models.product.product import Product
from models.user.anonymous_user import AnonymousUser
from proj_forms import SubmitForm
from r import R

if sys.version_info.major < 3:
    reload(sys)
sys.setdefaultencoding("utf8")

from flask import Flask, redirect, request

from configs import default_app_config
from configs.instance import instance_app_config
from configs.instance import unit_test_app_config

from proj_extensions import db
from flask_bombril.log import log_request
from flask_bombril.r import R as bombril_R
import flask_whooshalchemy as whooshalchemy


def __create_app(configs):
    static_folder = None
    template_folder = None
    for config in configs:
        if hasattr(config, "STATIC_FULL_PATH"):
            static_folder = config.STATIC_FULL_PATH
        if hasattr(config, "TEMPLATE_FOLDER"):
            template_folder = config.TEMPLATE_FOLDER

    app = Flask(__name__, instance_relative_config=True, static_folder=static_folder, template_folder=template_folder)

    for config in configs:
        app.config.from_object(config)

    # Initializing extensions
    from proj_extensions import bcrypt
    bcrypt.init_app(app)
    from proj_extensions import db
    db.init_app(app)
    from proj_extensions import mail
    mail.init_app(app)
    from proj_extensions import cache
    cache.init_app(app)
    from proj_extensions import login_manager
    login_manager.init_app(app)
    login_manager.login_view = "client_user_management.login"
    login_manager.login_message = R.string.login_message
    login_manager.login_message_category = bombril_R.string.get_message_category(bombril_R.string.static,
                                                                                 bombril_R.string.info)
    login_manager.anonymous_user = AnonymousUser
    whooshalchemy.whoosh_index(app, Product)
    whooshalchemy.whoosh_index(app, BlogPost)
    from proj_extensions import babel
    babel.init_app(app)

    return app


def create_app():
    app = __create_app([default_app_config, instance_app_config])

    @app.route("/")
    def home_redirect():
        return redirect("home")

    # ==================================================================================================================
    #
    #
    #
    #
    # Registering blueprints
    # ==================================================================================================================
    #
    # Components
    #
    from components import components_blueprint
    app.register_blueprint(components_blueprint, url_prefix="/componentes")
    #
    # Admin Routers
    #
    # from routers.admin_attended_cities import admin_attended_cities_blueprint
    # app.register_blueprint(admin_attended_cities_blueprint, url_prefix="/admin/cidades-atendidas")
    # from routers.admin_blog import admin_blog_blueprint
    # app.register_blueprint(admin_blog_blueprint, url_prefix="/admin/blog")
    # from routers.admin_content import admin_content_blueprint
    # app.register_blueprint(admin_content_blueprint, url_prefix="/admin/conteudo")
    # from routers.admin_clients import admin_clients_blueprint
    # app.register_blueprint(admin_clients_blueprint, url_prefix="/admin/clientes")
    # from routers.admin_home import admin_home_blueprint
    # app.register_blueprint(admin_home_blueprint, url_prefix="/admin/home")
    # from routers.admin_images import admin_images_blueprint
    # app.register_blueprint(admin_images_blueprint, url_prefix="/admin/imagens")
    # from routers.admin_orders import admin_orders_blueprint
    # app.register_blueprint(admin_orders_blueprint, url_prefix="/admin/pedidos")
    # from routers.admin_products import admin_products_blueprint
    # app.register_blueprint(admin_products_blueprint, url_prefix="/admin/produtos")
    from admin import admin_proj_blueprint
    app.register_blueprint(admin_proj_blueprint, url_prefix="/admin-proj")
    #
    # Client Routers
    #
    from routers.client_about_us import client_about_us_blueprint
    app.register_blueprint(client_about_us_blueprint, url_prefix="/sobre-nos")
    from routers.client_account import client_account_blueprint
    app.register_blueprint(client_account_blueprint, url_prefix="/minha-conta")
    from routers.blog import client_blog_blueprint
    app.register_blueprint(client_blog_blueprint, url_prefix="/blog")
    from routers.client_cart import client_cart_blueprint
    app.register_blueprint(client_cart_blueprint, url_prefix="/carrinho")
    from routers.client_checkout import client_checkout_blueprint
    app.register_blueprint(client_checkout_blueprint, url_prefix="/finalizacao-de-compra")
    from routers.client_faq import client_faq_blueprint
    app.register_blueprint(client_faq_blueprint, url_prefix="/faq")
    from routers.client_payment import client_payment_blueprint
    app.register_blueprint(client_payment_blueprint, url_prefix="/pagamento")
    from routers.client_dispatch import client_dispatch_blueprint
    app.register_blueprint(client_dispatch_blueprint, url_prefix="/envio")
    from routers.client_exchanges_and_returns import client_exchanges_and_returns_blueprint
    app.register_blueprint(client_exchanges_and_returns_blueprint, url_prefix="/trocas-e-devolucoes")
    from routers.client_home import client_home_blueprint
    app.register_blueprint(client_home_blueprint, url_prefix="/home")
    from routers.client_products import client_products_blueprint
    app.register_blueprint(client_products_blueprint, url_prefix="/produtos")
    from routers.client_search import client_search_blueprint
    app.register_blueprint(client_search_blueprint, url_prefix="/busca")
    from routers.client_user_management import client_user_management_blueprint
    app.register_blueprint(client_user_management_blueprint, url_prefix="/conta")

    #
    # Wrappers
    #
    from wrappers.base import base_blueprint
    app.register_blueprint(base_blueprint, url_prefix="/base")
    # from wrappers.admin_base import admin_base_blueprint
    # app.register_blueprint(admin_base_blueprint, url_prefix="/admin-base")
    from wrappers.client_base import client_base_blueprint
    app.register_blueprint(client_base_blueprint, url_prefix="/client-base")
    #
    # Macros
    #
    from macros import macros_blueprint
    app.register_blueprint(macros_blueprint)
    from flask_bombril.macros import flask_bombril_macros_blueprint
    app.register_blueprint(flask_bombril_macros_blueprint)
    #
    # Email
    #
    from email_blueprint import email_blueprint
    app.register_blueprint(email_blueprint)

    # ==================================================================================================================
    #
    #
    #
    #
    # Registering jinja filters
    # ==================================================================================================================
    from flask_bombril.jinja_filters import assert_defined, assert_callable, call, if_filter, is_static, is_toast, \
        get_level
    app.jinja_env.filters["assert_defined"] = assert_defined
    app.jinja_env.filters["assert_callable"] = assert_callable
    app.jinja_env.filters["call"] = call
    app.jinja_env.filters["if"] = if_filter
    app.jinja_env.filters["is_static"] = is_static
    app.jinja_env.filters["is_toast"] = is_toast
    app.jinja_env.filters["get_level"] = get_level

    # ==================================================================================================================
    #
    #
    #
    #
    # Registering jinja tests
    # ==================================================================================================================
    from flask_bombril.jinja_tests import is_list, is_dict
    app.jinja_env.tests["list"] = is_list
    app.jinja_env.tests["dict"] = is_dict
    # ==================================================================================================================
    #
    #
    #
    #
    # Registering app context_processors
    # ==================================================================================================================
    from r import R
    from flask_bombril import R as bombril_R
    from components.data_providers import admin_navbar_data_provider
    from components.data_providers.client_footer import client_footer_data_provider
    from components.data_providers.client_header import header_data_provider
    from components.data_providers.tags_row import tags_row_data_provider

    def generate_csrf_token():
        if '_csrf_token' not in session:
            session['_csrf_token'] = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(R.dimen.csrf_length))
        return session['_csrf_token']

    @app.context_processor
    def _():
        return dict(
            R=R,
            bombril_R=bombril_R,
            get_components_admin_navbar_data=lambda:admin_navbar_data_provider.get_data(),
            get_components_client_header_data=lambda: header_data_provider.get_data(),
            get_components_client_footer_data=lambda: client_footer_data_provider.get_data(),
            get_components_client_mobile_menu_data=lambda: header_data_provider.get_menu_data(),
            get_components_tags_row_data=lambda: tags_row_data_provider.get_data(),
            submit_form=SubmitForm(),
            csrf_token=generate_csrf_token
        )

    # ==================================================================================================================
    #
    #
    #
    #
    # Configuring Logging
    # ==================================================================================================================
    import logging
    from logging.handlers import TimedRotatingFileHandler
    handler = TimedRotatingFileHandler(
        filename=app.config["LOGGING_FILENAME"],
        when=app.config["LOGGING_WHEN"],
        interval=app.config["LOGGING_INTERVAL"],
        backupCount=app.config["LOGGING_BACKUP_COUNT"]
    )
    formatter = logging.Formatter(app.config["LOGGING_FORMAT"])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    # ==================================================================================================================
    #
    #
    #
    #
    # Registering 500 error handler
    # ==================================================================================================================
    @app.errorhandler(500)
    def handle_error(error):
        db.session.rollback()
        log_request(app.logger.error)
        # TODO: Add home page href
        return R.string.temp_error_html % dict(home_page_href="#"), 500

    # ==================================================================================================================
    #
    #
    #
    #
    # Declaring before request
    # ==================================================================================================================
    @app.before_request
    def before_request():
        db.session.rollback()

    # ==================================================================================================================
    #
    #
    #
    #
    # Declaring after request
    # ==================================================================================================================
    @app.after_request
    def after_request(response):
        db.session.remove()
        return response

    # ==================================================================================================================
    #
    #
    #
    #
    # Declaring admin panel definitions
    # ==================================================================================================================
    from proj_extensions import admin
    from models.order import Order
    from models_view.order_view import OrderView
    from models.city import City
    from models_view.city_view import CityView
    from models.product.product_category import ProductCategory
    from models_view.product.product_category_view import ProductCategoryView
    from models.product.product_subcategory import ProductSubcategory
    from models_view.product.product_subcategory_view import ProductSubcategoryView
    from models.product.product import Product
    from models_view.product.product_view import ProductView
    from models_view.my_admin_index_view import MyAdminIndexView
    from models.blog.blog_tag import BlogTag
    from models_view.blog.blog_tag_view import BlogTagView
    from models.blog.blog_post import BlogPost
    from models_view.blog.blog_post_view import BlogPostView
    from models.images.other_image import OtherImage
    from models_view.images.other_image_view import OtherImageView
    from models.content.about_us import AboutUs
    from models_view.content.about_us_view import AboutUsView
    from models.content.dispatch import Dispatch
    from models_view.content.dispatch_view import DispatchView
    from models.content.exchanges_and_returns import ExchangesAndReturns
    from models_view.content.exchanges_and_returns_view import ExchangesAndReturnsView
    from models.content.faq import Faq
    from models_view.content.faq_view import FaqView
    from models_view.content.footer_view import FooterView
    from models.content.footer import Footer
    from models_view.content.header_view import HeaderView
    from models.content.header import Header
    from models_view.content.payment_view import PaymentView
    from models.content.payment import Payment
    from models.content.contact import Contact
    from models_view.content.contact_view import ContactView
    from models.content.home_content import HomeContent
    from models_view.content.home_content_view import HomeContentView
    from models.content.tags_row import TagsRow
    from models_view.content.tags_row_view import TagsRowView
    from models.user.user import User
    from models_view.user_view import UserView

    admin.init_app(app, index_view=MyAdminIndexView())

    admin.add_view(CityView(City, db.session))
    admin.add_view(ProductCategoryView(ProductCategory, db.session))
    admin.add_view(ProductSubcategoryView(ProductSubcategory, db.session))
    admin.add_view(ProductView(Product, db.session))
    admin.add_view(OtherImageView(OtherImage, db.session))
    admin.add_view(BlogPostView(BlogPost, db.session))
    admin.add_view(BlogTagView(BlogTag, db.session))
    admin.add_view(UserView(User, db.session))
    admin.add_view(OrderView(Order, db.session))
    admin.add_view(AboutUsView(AboutUs, db.session))
    admin.add_view(DispatchView(Dispatch, db.session))
    admin.add_view(ExchangesAndReturnsView(ExchangesAndReturns, db.session))
    admin.add_view(FaqView(Faq, db.session))
    admin.add_view(FooterView(Footer, db.session))
    admin.add_view(HeaderView(Header, db.session))
    admin.add_view(PaymentView(Payment, db.session))
    admin.add_view(ContactView(Contact, db.session))
    admin.add_view(HomeContentView(HomeContent, db.session))
    admin.add_view(TagsRowView(TagsRow, db.session))

    from proj_extensions import babel

    @babel.localeselector
    def get_locale():
        if request.args.get('lang'):
            session['lang'] = request.args.get('lang')
        return session.get('lang', 'pt_BR')

    return app


def create_unit_test_app():
    app = __create_app([default_app_config, instance_app_config, unit_test_app_config])

    return app
