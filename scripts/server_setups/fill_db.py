# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 12/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import datetime
import random
import sys

sys.path.append("/vagrant")
sys.path.append("/vagrant/build")
sys.path.append("/vagrant/build/flask-admin")

from decimal import Decimal
from app_contexts.app import app
from proj_extensions import db
from models.content.about_us import AboutUs
from models.blog.blog_post import BlogPost
from models.content.contact import Contact
from models.content.footer import Footer
from models.content.home_content import HomeContent
from models.product.product import Product
from models.product.product_category import ProductCategory
from models.content.tags_row import TagsRow
from models.city import City
from models.order import Order
from models.product.product_subcategory import ProductSubcategory
from models.state import State
from models.user.user import User
from random_bombril import get_random_string, get_random_price, get_random_phrase, get_random_cep, get_random_tel, \
    get_random_datetime, get_random_date
from models.blog.blog_tag import BlogTag
from models.images.other_image import OtherImage
from r import R
from proj_utils import parse_markdown


n_product_categories = 25
n_product_subcategories = 200
n_products = 800
n_clients = 200
n_orders = 500
n_blog_tags = 20
n_blog_posts = 300

title_key_words = [
    "banana",
    "maça",
    "papinha",
    "sobremesa",
    "arroz",
    "doce",
    "salgado",
    "azul",
    "amarelo",
    "vermelho",
    "laranja"
]

text_key_words = [
    "é",
    "pois",
    "não",
    "sim",
    "talvez",
    "oi",
    "olá",
    "hoje",
    "eu",
    "você",
    "amanhã",
    "enquanto",
    "matemática",
    "ciência",
    "física",
    "química",
    "lenço",
    "copo",
    "papel",
    "livro",
    "digestão",
    "bebê"
]

datetime_1 = datetime.datetime.now() - datetime.timedelta(days=90)
datetime_2 = datetime.datetime.now() - datetime.timedelta(days=60)
datetime_3 = datetime.datetime.now() - datetime.timedelta(days=30)
datetime_4 = datetime.datetime.now()


def fill_db():
    with app.app_context():
        create_blog_link_example_image()
        create_cute_baby_image()

        create_random_product_categories()
        create_random_product_subcategories()
        create_random_products()
        create_specif_cities()
        create_random_clients()
        create_random_orders()
        create_random_blog_tags()
        create_random_blog_posts()

        create_footer_data()
        create_contact_data()
        create_about_us_data()
        create_tags_row_data()
        create_home_content_data()


def create_blog_link_example_image():
    db.session.add(OtherImage(filename="post_link_example.jpg"))
    print "OtherImage post_link_example.jpg created."
    db.session.commit()


def create_cute_baby_image():
    db.session.add(OtherImage(filename="bebe_fofo.jpg"))
    print "OtherImage bebe_fofo.jpg created."
    db.session.commit()


def create_random_product_categories():
    for i in range(0, n_product_categories):
        db.session.add(get_random_product_category())
        print "Product category " + str(i) + " created."
    db.session.commit()


def get_random_product_category():
    return ProductCategory(
        name=get_random_string(random.randint(4, 8))[0:R.dimen.product_category_name_max_length],
        active=random.choice([True, False])
    )


def create_random_product_subcategories():
    for i in range(0, n_product_subcategories):
        db.session.add(get_random_product_subcategory())
        print "Product subcategory " + str(i) + " created."
    db.session.commit()


def get_random_product_subcategory():
    return ProductSubcategory(
        name=get_random_string(random.randint(4, 8))[0:R.dimen.product_subcategory_name_max_length],
        active=random.choice([True, False]),
        product_category_id=get_random_valid_product_category_id_or_none()
    )


def create_random_products():
    for i in range(0, n_products):
        db.session.add(get_random_product())
        print "Product " + str(i) + " created."
    db.session.commit()


def get_random_product():
    random_value = random.uniform(0, 1)
    subcategory_id = None
    if random_value < 0.75:
        category_id = get_random_valid_product_category_id_or_none(),
        subcategory_id = get_random_valid_product_subcategory_id_or_none(category_id=category_id),
    else:
        category_id = get_random_valid_product_category_id_or_none(),

    stock = random.randint(0, 500)

    has_discount = random.choice([True, False])
    discount_percentage = 0
    if has_discount:
        discount_percentage = random.choice(range(1, 71))

    return Product(
        active=(random.uniform(0, 1) < 0.5),
        title=random.choice(title_key_words) + " " + get_random_phrase((3, 9 + 1), (1, 5 + 1))[
                                                     0:R.dimen.product_title_max_length],
        category_id=category_id,
        subcategory_id=subcategory_id,
        price=Decimal(get_random_price()),
        has_discount=has_discount,
        discount_percentage=discount_percentage,
        stock=stock,
        min_available=random.randint(2, 20),
        summary_markdown=random.choice(text_key_words) + " " + get_random_phrase((4, 10 + 1), (20, 40 + 1)),
        sales_number=random.randint(0, 500)
    )


def create_specif_cities():
    sp_id = State.query.filter(State.name == "SP").one_or_none().id
    db.session.add(City(state_id=sp_id, name="São José dos Campos", active=True))
    db.session.add(City(state_id=sp_id, name="Jacareí", active=True))
    db.session.add(City(state_id=sp_id, name="Santo André", active=True))
    db.session.add(City(state_id=sp_id, name="São Paulo", active=False))
    db.session.add(City(state_id=sp_id, name="São Bernardo do Campo", active=False))

    rj_id = State.query.filter(State.name == "RJ").one_or_none().id
    db.session.add(City(state_id=rj_id, name="Rio de Janeiro", active=True))

    mg_id = State.query.filter(State.name == "MG").one_or_none().id
    db.session.add(City(state_id=mg_id, name="Belo Horizonte", active=True))
    db.session.add(City(state_id=mg_id, name="Juiz de Fora", active=True))
    db.session.add(City(state_id=mg_id, name="Contagem", active=False))

    go_id = State.query.filter(State.name == "GO").one_or_none().id
    db.session.add(City(state_id=go_id, name="Goiânia", active=True))
    db.session.add(City(state_id=go_id, name="Anápolis", active=True))
    db.session.add(City(state_id=go_id, name="Trindade", active=False))

    db.session.commit()

    print "Cities created."


def create_random_clients():
    for i in range(0, n_clients):
        db.session.add(get_random_client())
        print "Client " + str(i) + " created."
    db.session.commit()


def get_random_client():
    email_confirmed = random.uniform(0, 1) < 0.7
    address_fields = dict()
    if email_confirmed and random.uniform(0, 1) < 0.6:
        state_id = get_random_valid_state_id_or_none()
        address_fields = dict(
            first_name=get_random_phrase((3, 6 + 1), (1, 3 + 1))[0:R.dimen.first_name_max_length],
            last_name=get_random_phrase((3, 6 + 1), (1, 3 + 1))[0:R.dimen.last_name_max_length],
            state_id=state_id,
            city_id=get_random_valid_city_id_or_none(state_id),
            address=get_random_phrase((3, 10 + 1), (3, 12 + 1))[0:R.dimen.address_max_length],
            address_number=random.randint(1, 5000),
            address_complement=get_random_phrase((3, 6 + 1), (0, 6 + 1))[0:R.dimen.address_complement_max_length],
            cep=get_random_cep()[0:R.dimen.cep_max_length],
            tel=get_random_tel()[0:R.dimen.tel_max_length]
        )

    return User(
        email=(get_random_string(random.randint(4, 8)) + "@" + get_random_string(random.randint(4, 8)) + ".com")[
              0:R.dimen.email_max_length],
        password=get_random_string(random.randint(6, 32))[0:R.dimen.password_max_length],
        email_confirmed=email_confirmed,
        register_datetime=get_random_datetime(datetime_1, datetime_4),
        **address_fields
    )


def create_random_orders():
    for i in range(0, n_orders):
        try:
            create_random_order()
            print "Order " + str(i) + " created."
        except Exception as e:
            print "Order " + str(i) + " creation fail."


def create_random_order():
    status = random.choice(
        filter(lambda order_status_id: order_status_id != R.id.ORDER_STATUS_ANY, Order.order_status_map.keys()))
    Order.create_new(
        client_id=get_random_valid_client_id_or_none(address_defined=True),
        status=status,
        product_ids_and_amount=get_random_product_ids_and_amount(),
        **get_random_order_datetimes(status)
    )


def get_random_product_ids_and_amount():
    product_ids_and_amount = []
    n_products_in_order = random.randint(1, 10)
    products = Product.query.all()
    random.shuffle(products)
    chosen_products = products[0:n_products_in_order]
    for product in chosen_products:
        amount = random.randint(1, product.get_n_units_available())
        product_ids_and_amount.append((product.id, amount))
    assert len(product_ids_and_amount) >= 1
    return product_ids_and_amount


def get_random_order_datetimes(status):
    order_datetimes = dict(
        paid_datetime=get_random_datetime(datetime_1, datetime_2 - datetime.timedelta(1))
    )
    if status == R.id.ORDER_STATUS_SENT:
        order_datetimes["sent_datetime"] = get_random_datetime(datetime_2, datetime_3 - datetime.timedelta(1))
    elif status == R.id.ORDER_STATUS_DELIVERED:
        order_datetimes["sent_datetime"] = get_random_datetime(datetime_2, datetime_3 - datetime.timedelta(1))
        order_datetimes["delivered_datetime"] = get_random_datetime(datetime_3, datetime_4)
    return order_datetimes


def create_random_blog_tags():
    for i in range(0, n_blog_tags):
        db.session.add(get_random_blog_tag())
        print "Blog tag " + str(i) + " created."
    db.session.commit()


def get_random_blog_tag():
    return BlogTag(
        name=get_random_string(12),
        active=random.choice([True, False])
    )


def create_random_blog_posts():
    for i in range(0, n_blog_posts):
        db.session.add(get_random_blog_post())
        print "Blog post " + str(i) + " created."
    db.session.commit()


def get_random_blog_post():
    n_tags = min(random.choice(range(0, 5+1)), BlogTag.count()+1)
    blog_tags = BlogTag.query.all()
    random.shuffle(blog_tags)
    return BlogPost(
        active=random.choice([True, False]),
        title=random.choice(title_key_words) + " " + get_random_phrase((3, 8), (3, 6)),
        date=get_random_date(datetime_1, datetime_2),
        summary_markdown=random.choice(text_key_words) + " " + get_random_phrase((3, 8), (16, 30)),
        content_markdown=random.choice(text_key_words) + " " + get_random_phrase((3, 8), (50, 150)),
        tags=blog_tags[0:n_tags]
    )


def get_random_valid_product_category_id_or_none():
    try:
        return random.choice(ProductCategory.query.with_entities(ProductCategory.id).all())
    except:
        return None


def get_random_valid_product_subcategory_id_or_none(category_id):
    try:
        product_subcategories = ProductSubcategory.query.filter(
            ProductSubcategory.product_category_id == category_id).with_entities(
            ProductSubcategory.id).all()
        return random.choice(product_subcategories)
    except:
        return None


def get_random_valid_state_id_or_none():
    try:
        return random.choice(State.query.with_entities(State.id).all())
    except:
        return None


def get_random_valid_client_id_or_none(address_defined):
    try:
        q = User.query
        if address_defined:
            q = q.filter(User.address != None)
        return random.choice(q.with_entities(User.id).all())
    except:
        return None


def get_random_valid_city_id_or_none(state_id):
    try:
        return random.choice(City.query.filter(City.state_id == state_id).with_entities(City.id).all())
    except Exception:
        return None


def create_footer_data():
    footer = Footer.get()

    footer.lower_text_markdown = R.string.footer_lower_text_example
    footer.lower_text_html = parse_markdown(footer.lower_text_markdown)

    db.session.add(footer)
    db.session.commit()


def create_contact_data():
    contact = Contact.get()

    contact.address_markdown = R.string.address_example
    contact.address_html = parse_markdown(contact.address_markdown)
    contact.tel = R.string.tel_example
    contact.email = R.string.email_example

    contact.facebook_active = True
    contact.facebook_link = R.string.facebook_link_example

    contact.youtube_active = True
    contact.youtube_link = R.string.youtube_link_example

    contact.twitter_active = True
    contact.twitter_link = R.string.twitter_link_example

    db.session.add(contact)
    db.session.commit()


def create_about_us_data():
    about_us = AboutUs.get()

    about_us.summary_markdown = R.string.about_us_summary_example
    about_us.summary_html = parse_markdown(about_us.summary_markdown)
    about_us.content_markdown = R.string.about_us_content_example
    about_us.content_html = parse_markdown(about_us.content_markdown)

    db.session.add(about_us)
    db.session.commit()


def create_tags_row_data():
    tags_row = TagsRow.get()

    tags_row.tag_1_image = "stork.png"
    tags_row.tag_1_title = "Frete grátis"
    tags_row.tag_1_subtitle = "Para São José dos Campos para compras acima de R$ 50,00"

    tags_row.tag_2_image = "stork.png"
    tags_row.tag_2_title = "Frete grátis"
    tags_row.tag_2_subtitle = "Para São José dos Campos para compras acima de R$ 50,00"

    tags_row.tag_3_image = "stork.png"
    tags_row.tag_3_title = "Frete grátis"
    tags_row.tag_3_subtitle = "Para São José dos Campos para compras acima de R$ 50,00"

    db.session.add(tags_row)
    db.session.commit()


def create_home_content_data():
    home_content = HomeContent.get()

    home_content.carousel_1_active = True
    home_content.carousel_1_title = "Título 1"
    home_content.carousel_1_subtitle = "Subtítulo 1"
    home_content.carousel_1_link = "/blog"

    home_content.carousel_2_active = True
    home_content.carousel_2_title = "Título 2"

    products = Product.query.filter(Product.is_available_to_client == True, Product.has_discount == False).all()

    if len(products) > 0:
        home_content.product_section_1_active = True
        home_content.product_section_1_name = "Novidades"
        home_content.product_section_1_link = "/produtos"
        home_content.product_section_1_product_1_id = random.choice(products).id
        home_content.product_section_1_product_2_id = random.choice(products).id
        home_content.product_section_1_product_3_id = random.choice(products).id
        home_content.product_section_1_product_4_id = random.choice(products).id
        home_content.product_section_1_product_5_id = random.choice(products).id
        home_content.product_section_1_product_6_id = random.choice(products).id
        home_content.product_section_1_product_7_id = random.choice(products).id
        home_content.product_section_1_product_8_id = random.choice(products).id
        home_content.product_section_1_product_9_id = random.choice(products).id
        home_content.product_section_1_product_10_id = random.choice(products).id
        home_content.product_section_1_product_11_id = random.choice(products).id
        home_content.product_section_1_product_12_id = random.choice(products).id

    products = Product.query.filter(Product.is_available_to_client == True, Product.has_discount == True).all()

    if len(products) > 0:
        home_content.product_section_2_active = True
        home_content.product_section_2_name = "Promoções"
        home_content.product_section_2_link = "/produtos"
        home_content.product_section_2_product_1_id = random.choice(products).id
        home_content.product_section_2_product_2_id = random.choice(products).id
        home_content.product_section_2_product_3_id = random.choice(products).id
        home_content.product_section_2_product_4_id = random.choice(products).id
        home_content.product_section_2_product_5_id = random.choice(products).id
        home_content.product_section_2_product_6_id = random.choice(products).id
        home_content.product_section_2_product_7_id = random.choice(products).id
        home_content.product_section_2_product_8_id = random.choice(products).id
        home_content.product_section_2_product_9_id = random.choice(products).id
        home_content.product_section_2_product_10_id = random.choice(products).id
        home_content.product_section_2_product_11_id = random.choice(products).id
        home_content.product_section_2_product_12_id = random.choice(products).id

    categories = ProductCategory.query.filter(ProductCategory.active == True).all()

    if len(categories) >= 1:
        category = categories[0]
        home_content.more_categories_section_category_1_id = category.id
        home_content.more_categories_section_category_1_image = "baby-1.png"
        active_subcategories = []
        for subcategory in category.product_subcategories:
            if subcategory.active:
                active_subcategories.append(subcategory)
        if len(active_subcategories) >= 1:
            home_content.more_categories_section_subcategory_1_of_category_1_id = active_subcategories[0].id
        if len(active_subcategories) >= 2:
            home_content.more_categories_section_subcategory_2_of_category_1_id = active_subcategories[1].id
        if len(active_subcategories) >= 3:
            home_content.more_categories_section_subcategory_3_of_category_1_id = active_subcategories[2].id
        if len(active_subcategories) >= 4:
            home_content.more_categories_section_subcategory_4_of_category_1_id = active_subcategories[3].id
        if len(active_subcategories) >= 5:
            home_content.more_categories_section_subcategory_5_of_category_1_id = active_subcategories[4].id

    if len(categories) >= 2:
        category = categories[1]
        home_content.more_categories_section_category_2_id = category.id
        home_content.more_categories_section_category_2_image = "baby-2.png"
        active_subcategories = []
        for subcategory in category.product_subcategories:
            if subcategory.active:
                active_subcategories.append(subcategory)
        if len(active_subcategories) >= 1:
            home_content.more_categories_section_subcategory_1_of_category_2_id = active_subcategories[0].id
        if len(active_subcategories) >= 2:
            home_content.more_categories_section_subcategory_2_of_category_2_id = active_subcategories[1].id
        if len(active_subcategories) >= 3:
            home_content.more_categories_section_subcategory_3_of_category_2_id = active_subcategories[2].id
        if len(active_subcategories) >= 4:
            home_content.more_categories_section_subcategory_4_of_category_2_id = active_subcategories[3].id
        if len(active_subcategories) >= 5:
            home_content.more_categories_section_subcategory_5_of_category_2_id = active_subcategories[4].id

    if len(categories) >= 3:
        category = categories[2]
        home_content.more_categories_section_category_3_id = category.id
        home_content.more_categories_section_category_3_image = "baby-3.png"
        active_subcategories = []
        for subcategory in category.product_subcategories:
            if subcategory.active:
                active_subcategories.append(subcategory)
        if len(active_subcategories) >= 1:
            home_content.more_categories_section_subcategory_1_of_category_3_id = active_subcategories[0].id
        if len(active_subcategories) >= 2:
            home_content.more_categories_section_subcategory_2_of_category_3_id = active_subcategories[1].id
        if len(active_subcategories) >= 3:
            home_content.more_categories_section_subcategory_3_of_category_3_id = active_subcategories[2].id
        if len(active_subcategories) >= 4:
            home_content.more_categories_section_subcategory_4_of_category_3_id = active_subcategories[3].id
        if len(active_subcategories) >= 5:
            home_content.more_categories_section_subcategory_5_of_category_3_id = active_subcategories[4].id

    if len(categories) >= 4:
        category = categories[3]
        home_content.more_categories_section_category_4_id = category.id
        home_content.more_categories_section_category_4_image = "baby-4.png"
        active_subcategories = []
        for subcategory in category.product_subcategories:
            if subcategory.active:
                active_subcategories.append(subcategory)
        if len(active_subcategories) >= 1:
            home_content.more_categories_section_subcategory_1_of_category_4_id = active_subcategories[0].id
        if len(active_subcategories) >= 2:
            home_content.more_categories_section_subcategory_2_of_category_4_id = active_subcategories[1].id
        if len(active_subcategories) >= 3:
            home_content.more_categories_section_subcategory_3_of_category_4_id = active_subcategories[2].id
        if len(active_subcategories) >= 4:
            home_content.more_categories_section_subcategory_4_of_category_4_id = active_subcategories[3].id
        if len(active_subcategories) >= 5:
            home_content.more_categories_section_subcategory_5_of_category_4_id = active_subcategories[4].id

    if len(categories) >= 5:
        category = categories[4]
        home_content.more_categories_section_category_5_id = category.id
        home_content.more_categories_section_category_5_image = "baby-5.png"
        active_subcategories = []
        for subcategory in category.product_subcategories:
            if subcategory.active:
                active_subcategories.append(subcategory)
        if len(active_subcategories) >= 1:
            home_content.more_categories_section_subcategory_1_of_category_5_id = active_subcategories[0].id
        if len(active_subcategories) >= 2:
            home_content.more_categories_section_subcategory_2_of_category_5_id = active_subcategories[1].id
        if len(active_subcategories) >= 3:
            home_content.more_categories_section_subcategory_3_of_category_5_id = active_subcategories[2].id
        if len(active_subcategories) >= 4:
            home_content.more_categories_section_subcategory_4_of_category_5_id = active_subcategories[3].id
        if len(active_subcategories) >= 5:
            home_content.more_categories_section_subcategory_5_of_category_5_id = active_subcategories[4].id

    if len(categories) >= 6:
        category = categories[5]
        home_content.more_categories_section_category_6_id = category.id
        home_content.more_categories_section_category_6_image = "baby-6.png"
        active_subcategories = []
        for subcategory in category.product_subcategories:
            if subcategory.active:
                active_subcategories.append(subcategory)
        if len(active_subcategories) >= 1:
            home_content.more_categories_section_subcategory_1_of_category_6_id = active_subcategories[0].id
        if len(active_subcategories) >= 2:
            home_content.more_categories_section_subcategory_2_of_category_6_id = active_subcategories[1].id
        if len(active_subcategories) >= 3:
            home_content.more_categories_section_subcategory_3_of_category_6_id = active_subcategories[2].id
        if len(active_subcategories) >= 4:
            home_content.more_categories_section_subcategory_4_of_category_6_id = active_subcategories[3].id
        if len(active_subcategories) >= 5:
            home_content.more_categories_section_subcategory_5_of_category_6_id = active_subcategories[4].id

    blog_posts = BlogPost.query.filter(BlogPost.active == True).all()

    if len(blog_posts) >= 1:
        home_content.blog_section_1_active = True
        home_content.blog_section_1_name = "Novidades do blog"
        home_content.blog_section_1_link = "/blog"
        home_content.blog_section_1_post_1_id = blog_posts[0].id
        if len(blog_posts) >= 2:
            home_content.blog_section_1_post_2_id = blog_posts[1].id

    db.session.add(home_content)
    db.session.commit()


if __name__ == "__main__":
    fill_db()
