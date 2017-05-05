# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 13/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import os
import random
import string
from decimal import Decimal

import datetime
from flask import current_app

from models.dispatch import Dispatch
from models.exchanges_and_returns import ExchangesAndReturns
from models.header import Header
from models.newsletter_emails import NewsletterEmails
from models.payment import Payment
from models.tags_row import TagsRow
from proj_extensions import db
from models.about_us import AboutUs
from models.blog_post import BlogPost
from models.city import City
from models.user import User
from models.contact import Contact
from models.faq import Faq
from models.footer import Footer
from models.home_content import HomeContent
from models.order import Order
from models.product import Product
from models.product_category import ProductCategory
from models.product_subcategory import ProductSubcategory
from models.state import State
from r import R

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


def create_states():
    db.session.add(State(name="SP"))
    db.session.add(State(name="RJ"))
    db.session.add(State(name="MG"))
    db.session.add(State(name="GO"))
    db.session.add(State(name="AC"))
    db.session.add(State(name="AL"))
    db.session.add(State(name="AP"))
    db.session.add(State(name="AM"))
    db.session.add(State(name="BA"))
    db.session.add(State(name="CE"))
    db.session.add(State(name="DF"))
    db.session.add(State(name="ES"))
    db.session.add(State(name="MA"))
    db.session.add(State(name="MT"))
    db.session.add(State(name="MS"))
    db.session.add(State(name="PA"))
    db.session.add(State(name="PB"))
    db.session.add(State(name="PR"))
    db.session.add(State(name="PE"))
    db.session.add(State(name="PI"))
    db.session.add(State(name="RN"))
    db.session.add(State(name="RS"))
    db.session.add(State(name="RO"))
    db.session.add(State(name="RR"))
    db.session.add(State(name="SC"))
    db.session.add(State(name="SE"))
    db.session.add(State(name="TO"))
    db.session.commit()
    print "States created."


def create_home_content():
    home_content = HomeContent()
    db.session.add(home_content)
    db.session.commit()
    print "Home content created."
    return home_content


def create_newsletter_emails():
    newsletter_emails = NewsletterEmails()
    db.session.add(newsletter_emails)
    db.session.commit()
    print "Newsletter emails created."
    return newsletter_emails


def create_tags_row():
    tags_row = TagsRow()
    db.session.add(tags_row)
    db.session.commit()
    print "Tags row created."
    return tags_row


def create_contact():
    contact = Contact()
    db.session.add(contact)
    db.session.commit()
    print "Contact created."
    return contact


def create_about_us():
    about_us = AboutUs()
    db.session.add(about_us)
    db.session.commit()
    print "AboutUs created."
    return about_us


def create_faq():
    faq = Faq()
    db.session.add(faq)
    db.session.commit()
    print "Faq created."
    return faq


def create_payment():
    payment = Payment()
    db.session.add(payment)
    db.session.commit()
    print "Payment created."
    return payment


def create_dispatch():
    dispatch = Dispatch()
    db.session.add(dispatch)
    db.session.commit()
    print "Dispatch created."
    return dispatch


def create_exchanges_and_returns():
    exchanges_and_returns = ExchangesAndReturns()
    db.session.add(exchanges_and_returns)
    db.session.commit()
    print "ExchangesAndReturns created."
    return exchanges_and_returns


def create_header():
    header = Header()
    db.session.add(header)
    db.session.commit()
    print "Header created."
    return header


def create_footer():
    footer = Footer()
    db.session.add(footer)
    db.session.commit()
    print "Footer created."
    return footer


def create_random_product_categories():
    for i in range(0, 25):
        db.session.add(get_random_product_category())
        print "Product category " + str(i) + " created."
    db.session.commit()


def create_random_product_subcategories():
    for i in range(0, 150):
        db.session.add(get_random_product_subcategory())
        print "Product subcategory " + str(i) + " created."
    db.session.commit()


def create_random_products():
    for i in range(0, 300):
        db.session.add(get_random_product())
        print "Product " + str(i) + " created."
    db.session.commit()


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
    for i in range(0, 300):
        db.session.add(get_random_client())
        print "Client " + str(i) + " created."
    db.session.commit()


def create_random_orders():
    for i in range(0, 50):
        try:
            create_random_order()
            print "Order " + str(i) + " created."
        except Exception as e:
            print "Order " + str(i) + " creation fail."


def create_random_blog_posts():
    for i in range(0, 300):
        db.session.add(get_random_blog_post())
        print "Blog post " + str(i) + " created."
    db.session.commit()


def get_random_blog_post():
    return BlogPost(
        active=random.choice([True, False]),
        title=random.choice(title_key_words) + " " + get_random_phrase((3,8), (3, 6)),
        datetime=get_random_datetime(datetime_1, datetime_2),
        thumbnail=get_random_image_name(),
        summary_markdown=random.choice(text_key_words) + " " + get_random_phrase((3,8), (16, 30)),
        content_markdown=random.choice(text_key_words) + " " + get_random_phrase((3,8), (50, 150))
    )


def create_random_order():
    status = random.choice(
        filter(lambda order_status_id: order_status_id != R.id.ORDER_STATUS_ANY, Order.order_status_map.keys()))
    Order.create_new(
        client_id=get_valid_client_id(address_defined=True),
        status=status,
        amount_by_product_id=get_amount_by_product_id(),
        **get_order_datetimes(status)
    )


def get_amount_by_product_id():
    amount_by_product_id = {}
    n_products = random.randint(1, 10)
    products = Product.query.all()
    random.shuffle(products)
    chosen_products = products[0:n_products]
    for product in chosen_products:
        amount = random.randint(1, product.available)
        amount_by_product_id[product.id] = amount
    assert len(amount_by_product_id) >= 1
    return amount_by_product_id


datetime_1 = datetime.datetime.now() - datetime.timedelta(days=90)
datetime_2 = datetime.datetime.now() - datetime.timedelta(days=60)
datetime_3 = datetime.datetime.now() - datetime.timedelta(days=30)
datetime_4 = datetime.datetime.now()


def get_order_datetimes(status):
    order_datetimes = dict(
        paid_datetime=get_random_datetime(datetime_1, datetime_2 - datetime.timedelta(1))
    )
    if status == R.id.ORDER_STATUS_SENT:
        order_datetimes["sent_datetime"] = get_random_datetime(datetime_2, datetime_3 - datetime.timedelta(1))
    elif status == R.id.ORDER_STATUS_DELIVERED:
        order_datetimes["sent_datetime"] = get_random_datetime(datetime_2, datetime_3 - datetime.timedelta(1))
        order_datetimes["delivered_datetime"] = get_random_datetime(datetime_3, datetime_4)
    return order_datetimes


def get_random_datetime(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


def get_random_client():
    email_confirmed = random.uniform(0, 1) < 0.7
    address_fields = dict()
    if email_confirmed and random.uniform(0, 1) < 0.6:
        state_id = get_random_valid_state_id()
        address_fields = dict(
            first_name=get_random_phrase((3, 6 + 1), (1, 3 + 1))[0:R.dimen.first_name_max_length],
            last_name=get_random_phrase((3, 6 + 1), (1, 3 + 1))[0:R.dimen.last_name_max_length],
            state_id=state_id,
            city_id=get_random_valid_city_id(state_id),
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


def get_random_cep():
    cep = ""
    for i in range(0, 5):
        cep += get_random_digit()
    cep += "-"
    for i in range(0, 3):
        cep += get_random_digit()
    return cep


def get_random_tel():
    tel = "("
    for i in range(0, 2):
        tel += get_random_digit()
    tel += ") "
    include_nine = random.choice([True, False])
    if include_nine:
        tel += "9"
    for i in range(0, 4):
        tel += get_random_digit()
    tel += "-"
    for i in range(0, 4):
        tel += get_random_digit()
    return tel


def get_random_product_category():
    return ProductCategory(
        name=get_random_string(random.randint(4, 8))[0:R.dimen.product_category_name_max_length],
        active=random.choice([True, False])
    )


def get_random_product_subcategory():
    return ProductSubcategory(
        name=get_random_string(random.randint(4, 8))[0:R.dimen.product_subcategory_name_max_length],
        active=random.choice([True, False]),
        category_id=get_random_valid_product_category_id()
    )


def get_random_product():
    random_value = random.uniform(0, 1)
    category_id = None
    subcategory_id = None
    if random_value < 0.75:
        category_id = get_random_valid_product_category_id(),
        subcategory_id = get_random_valid_product_subcategory_id(category_id=category_id),
    else:
        category_id = get_random_valid_product_category_id(),

    stock = random.randint(0, 500)

    has_discount = random.choice([True, False])
    discount_percentage = 0
    if has_discount:
        discount_percentage = random.choice(range(1,71))

    return Product(
        active=(random.uniform(0, 1) < 0.5),
        title=random.choice(title_key_words) + " " + get_random_phrase((3, 9 + 1), (1, 5 + 1))[0:R.dimen.product_title_max_length],
        category_id=category_id,
        subcategory_id=subcategory_id,
        price=Decimal(get_random_price()),
        has_discount=has_discount,
        discount_percentage=discount_percentage,
        stock=stock,
        min_available=random.randint(2, 20),
        summary_markdown=random.choice(text_key_words) + " " + get_random_phrase((4, 10 + 1), (20, 40 + 1)),
        sales_number=random.randint(0, 500),
        **get_random_images_dic()
    )


def get_valid_client_id(address_defined):
    q = User.query
    if address_defined:
        q = q.filter(User.address != None)
    return random.choice(q.with_entities(User.id).all())


def get_random_valid_product_category_id():
    return random.choice(ProductCategory.query.with_entities(ProductCategory.id).all())


def get_random_valid_state_id():
    return random.choice(State.query.with_entities(State.id).all())


def get_random_valid_product_subcategory_id(category_id):
    try:
        return random.choice(
            ProductSubcategory.query.filter(ProductSubcategory.category_id == category_id).with_entities(
                ProductSubcategory.id).all())
    except Exception:
        return None


def get_random_valid_city_id(state_id):
    try:
        return random.choice(City.query.filter(City.state_id == state_id).with_entities(City.id).all())
    except Exception:
        return None


def get_random_phrase(word_size_interval, words_interval):
    phrase = ""
    words_range = range(0, random.choice(range(*words_interval)))
    if len(words_range) > 0:
        last_idx = words_range[len(words_range) - 1]
        for i in words_range:
            phrase += get_random_string(random.choice(range(*word_size_interval)))
            if i != last_idx:
                phrase += " "
    return phrase.decode('utf-8')


def get_random_string(size):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(size))


def get_random_price():
    s = get_random_digit()
    if random.uniform(0, 1) < 0.5:
        s += get_random_digit()
    s += "."
    s += get_random_digit()
    s += get_random_digit()

    return s


def get_random_digit():
    return random.choice(string.digits)


images_key_list = [
    "image_1",
    "image_2",
    "image_3",
    "image_4",
    "image_5",
    "image_6",
    "image_7",
    "image_8",
    "image_9",
    "image_10",
]


def get_random_images_dic():
    images_key_list_copy = list(images_key_list)
    dic = {images_key_list_copy.pop(0): get_random_image_name()}
    for i in range(0, random.choice(range(0, 10))):
        dic[images_key_list_copy.pop(random.randint(0, len(images_key_list_copy) - 1))] = get_random_image_name()
    return dic


def get_random_image_name():
    return random.choice(os.listdir(current_app.config["UPLOADED_IMAGES_FOLDER_FULL_PATH"]))
