# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 12/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import os
import random
import datetime
import string
import sys

sys.path.append("/vagrant")
sys.path.append("/vagrant/build")

from app_contexts.app import app
from decimal import Decimal
from flask import current_app
from models.city import City
from models.client import Client
from models.order import Order
from models.product import Product
from models.product_category import ProductCategory
from models.product_subcategory import ProductSubcategory
from models.state import State
from r import R
from extensions import db


def fill_db():
    with app.app_context():
        create_product_categories()
        create_product_subcategories()
        create_products()
        create_states()
        create_cities()
        create_clients()
        create_orders()


def create_product_categories():
    for i in range(0, 25):
        db.session.add(get_random_product_category())
        print "Product category " + str(i) + " created."
    db.session.commit()


def create_product_subcategories():
    for i in range(0, 150):
        db.session.add(get_random_product_subcategory())
        print "Product subcategory " + str(i) + " created."
    db.session.commit()


def create_products():
    for i in range(0, 300):
        db.session.add(get_random_product())
        print "Product " + str(i) + " created."
    db.session.add(Product(
        title = "0000000000 São José dos Campos",
        active = True,
        category_id = 1,
        subcategory_id = 1,
        price = Decimal("1.00"),
        stock = 1,
        min_stock = 1,
        summary = 1,
        sales_number = 1,
        image_1 = get_random_image_name()
    ))
    db.session.commit()


def create_states():
    db.session.add(State(name="SP", active=True))
    db.session.add(State(name="RJ", active=True))
    db.session.add(State(name="MG", active=True))
    db.session.add(State(name="GO", active=True))

    db.session.add(State(name="AC", active=True))
    db.session.add(State(name="AL", active=True))
    db.session.add(State(name="AP", active=True))
    db.session.add(State(name="AM", active=True))
    db.session.add(State(name="BA", active=True))
    db.session.add(State(name="CE", active=True))
    db.session.add(State(name="DF", active=True))
    db.session.add(State(name="ES", active=True))
    db.session.add(State(name="MA", active=True))
    db.session.add(State(name="MT", active=True))
    db.session.add(State(name="MS", active=True))
    db.session.add(State(name="PA", active=True))
    db.session.add(State(name="PB", active=True))
    db.session.add(State(name="PR", active=True))
    db.session.add(State(name="PE", active=True))
    db.session.add(State(name="PI", active=True))
    db.session.add(State(name="RN", active=True))
    db.session.add(State(name="RS", active=True))
    db.session.add(State(name="RO", active=True))
    db.session.add(State(name="RR", active=True))
    db.session.add(State(name="SC", active=True))
    db.session.add(State(name="SE", active=True))
    db.session.add(State(name="TO", active=True))

    db.session.commit()

    print "States created."


def create_cities():
    db.session.add(City(state_id=1, name="São José dos Campos", active=True))
    db.session.add(City(state_id=1, name="Jacareí", active=True))
    db.session.add(City(state_id=1, name="Santo André", active=True))
    db.session.add(City(state_id=1, name="São Paulo", active=False))
    db.session.add(City(state_id=1, name="São Bernardo do Campo", active=False))

    db.session.add(City(state_id=2, name="Rio de Janeiro", active=True))

    db.session.add(City(state_id=3, name="Belo Horizonte", active=True))
    db.session.add(City(state_id=3, name="Juiz de Fora", active=True))
    db.session.add(City(state_id=3, name="Contagem", active=False))

    db.session.add(City(state_id=5, name="Goiânia", active=True))
    db.session.add(City(state_id=5, name="Anápolis", active=True))
    db.session.add(City(state_id=5, name="Trindade", active=False))

    db.session.commit()

    print "Cities created."


def create_clients():
    for i in range(0, 300):
        db.session.add(get_random_client())
        print "Client " + str(i) + " created."
    db.session.commit()


def create_orders():
    for i in range(0, 300):
        db.session.add(get_random_order())
        print "Order " + str(i) + " created."
    db.session.commit()


def get_random_order():
    status = random.choice(filter(lambda order_status_id: order_status_id != R.id.ORDER_STATUS_ANY, Order.order_status_ids))
    return Order(
        client_email=get_valid_client_email(address_defined=True),
        status=status,
        quantity_by_product_id=get_quantity_by_product_id(),
        **get_order_datetimes(status)
    )

def get_quantity_by_product_id():
    quantity_by_product_id = {}
    n_products = random.randint(1, 10)
    products = Product.query.all()
    random.shuffle(products)
    chosen_products = products[0:n_products]
    for product in chosen_products:
        quantity = random.randint(1, 20)
        quantity_by_product_id[product.id] = quantity
    return quantity_by_product_id

datetime_1 = datetime.datetime.now()-datetime.timedelta(days=90)
datetime_2 = datetime.datetime.now()-datetime.timedelta(days=60)
datetime_3 = datetime.datetime.now()-datetime.timedelta(days=30)
datetime_4 = datetime.datetime.now()

def get_order_datetimes(status):
    order_datetimes = dict(
        paid_datetime=get_random_datetime(datetime_1, datetime_2-datetime.timedelta(1))
    )
    if status == R.id.ORDER_STATUS_SENT:
        order_datetimes["sent_datetime"]=get_random_datetime(datetime_2, datetime_3-datetime.timedelta(1))
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

    return Client(
        email=(get_random_string(random.randint(4, 8)) + "@" + get_random_string(random.randint(4, 8)) + ".com")[0:R.dimen.email_max_length],
        password=get_random_string(random.randint(6, 32))[0:R.dimen.password_max_length],
        email_confirmed=email_confirmed,
        register_datetime = get_random_datetime(datetime_1, datetime_4),
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

    return Product(
        active=(random.uniform(0, 1) < 0.5),
        title=get_random_phrase((3, 10 + 1), (1, 5 + 1))[0:R.dimen.product_title_max_length],
        category_id=category_id,
        subcategory_id=subcategory_id,
        price=Decimal(get_random_price()),
        stock=random.randint(0, 500),
        min_stock=random.randint(2, 20),
        summary=get_random_phrase((4, 10 + 1), (20, 40 + 1)),
        sales_number=random.randint(0, 500),
        **get_random_images_dic()
    )


def get_valid_client_email(address_defined):
    q = Client.query
    if address_defined:
        q = q.filter(Client.address != None)
    return random.choice(q.with_entities(Client.email).all())


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
    return phrase


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

if __name__ == "__main__":
    fill_db()
