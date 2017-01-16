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

from extensions import db
from models.about_us import AboutUs
from models.blog_post import BlogPost
from models.city import City
from models.client import Client
from models.contact import Contact
from models.faq import Faq
from models.home_content import HomeContent
from models.order import Order
from models.product import Product
from models.product_category import ProductCategory
from models.product_subcategory import ProductSubcategory
from models.state import State
from r import R
from wrappers.base.utils import parse_markdown


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


def create_home_content(product_example_id, blog_post_example_id):
    home_content = HomeContent(
        carousel_item_1_active=True,
        carousel_item_1_title="Título do carrossel 1",
        carousel_item_1_subtitle="Subtítulo do carrossel 1",
        carousel_item_1_image="carousel_default.jpg",

        carousel_item_2_active=True,
        carousel_item_2_title="Título do carrossel 2",
        carousel_item_2_subtitle="Subtítulo do carrossel 2",
        carousel_item_2_image="carousel_default.jpg",

        carousel_item_3_active=True,
        carousel_item_3_title="Título do carrossel 3",
        carousel_item_3_subtitle="Subtítulo do carrossel 3",
        carousel_item_3_image="carousel_default.jpg",

        product_section_1_active=True,
        product_section_1_name="Seção de produtos 1",
        product_section_1_product_1_id=product_example_id,

        product_section_2_active=True,
        product_section_2_name="Seção de produtos 2",
        product_section_2_product_1_id=product_example_id,

        product_section_3_active=True,
        product_section_3_name="Seção de produtos 3",
        product_section_3_product_1_id=product_example_id,

        product_section_4_active=False,
        product_section_4_name="Seção de produtos 4",
        product_section_4_product_1_id=product_example_id,

        product_section_5_active=False,
        product_section_5_name="Seção de produtos 5",
        product_section_5_product_1_id=product_example_id,

        blog_section_1_active=True,
        blog_section_1_name="Seção do blog 1",
        blog_section_1_post_1_id=blog_post_example_id,

        blog_section_2_active=False,
        blog_section_2_name="Seção do blog 2",
        blog_section_2_post_1_id=blog_post_example_id,

        blog_section_3_active=False,
        blog_section_3_name="Seção do blog 3",
        blog_section_3_post_1_id=blog_post_example_id,
    )
    db.session.add(home_content)
    db.session.commit()
    print "Home content created."
    return home_content


def create_contact():
    contact = Contact(
        address="R. Vinte e Sete de Julho, 231 - São José dos Campos - SP",
        tel="(12) 2341-8725",
        email="contato@crescersaudavel.com",
        facebook_active=True,
        facebook_link="#",
        youtube_active=True,
        youtube_link="#",
        twitter_active=True,
        twitter_link="#"
    )
    db.session.add(contact)
    db.session.commit()
    print "Contact created."
    return contact


def create_about_us():
    about_us = AboutUs(
        content = R.string.about_us_content_example
    )
    db.session.add(about_us)
    db.session.commit()
    print "AboutUs created."
    return about_us


def create_faq():
    faq = Faq(
        content = R.string.faq_content_example
    )
    db.session.add(faq)
    db.session.commit()
    print "Faq created."
    return faq


def create_product_category_example():
    product_category = ProductCategory(
        name="Exemplo - Frutas",
        active=False,
    )
    db.session.add(product_category)
    db.session.commit()
    print "Product category example created."
    return product_category


def create_product_example(category_id):
    product = Product(
        title="Exemplo - Banana orgânica 100g",
        active=False,
        category_id=category_id,
        price=Decimal("9.90"),
        stock=100,
        min_stock=10,
        summary=parse_markdown(
            """
            Exemplo - A papinha de banana orgânica é saborosa, com uma textura muito agradável para os babys.
            Além disso, possui o beneficio de acalmar o estômago e ajudar na digestão.
            """),
        sales_number=32,

        image_1="banana_example_1.jpg",
        image_2="banana_example_2.jpg",
        image_3="banana_example_3.jpg",

        tab_1_title="Preparação",
        tab_1_content=parse_markdown(
            """
            #### Produto Congelado:
            1. Retirar o rótulo e a tampa
            2. Aquecer em microondas por 01 minuto ou em banho maria por 15 minutos, mexendo de vez em quando.
            3. Verifique a temperatura. Antes de consumir, misturar uniformemente o conteúdo.

            #### Produto descongelado (em refrigeração por 12 horas):
            1. Retirar o rótulo e a tampa
            2. Aquecer em microondas por 01 minuto ou em banho maria por 10 minutos mexendo de vez em quando.
            3. Verifique a temperatura. Antes de consumir, misturar uniformemente o conteúdo.
            """),

        tab_2_title="Ingredientes",
        tab_2_content=parse_markdown(
            """
            \* Para uma porção de **100g**

            Ingrediente     | Quantidade
            --------------- | ----------
            Banana orgânica | 75g
            Água            | 20ml
            Açúcar mascavo  | 5g
            """),
        tab_3_title="Informações nutricionais",
        tab_3_content=parse_markdown(
            """
            \* Para uma porção de **100g**

            Tipo de nutriente  | Quantidade
            ------------------ | ----------
            Carboidrato        | 22g
            Proteínas          | 1,2g
            Gorduras totais    | 0g
            Gorduras saturadas | 0g
            Gorduras trans     | 0g
            Fibra alimentar    | 1,9g

                Valor energético: 94 kcal
            """),
        tab_4_title="Benefícios",
        tab_4_content=parse_markdown(
            """
            * Rica em potássio, perfeita para baixar a pressão arterial.
            * Ricas em fibras, a inclusão de bananas nas dietas ajuda a normalizar o trânsito intestinal, permitindo melhorar os
            problemas de constipação sem o uso de laxantes.
            * A banana acalma o estômago e ajuda na digestão.
            """),
        tab_5_title="Conservação",
        tab_5_content=parse_markdown(
            """
            Conservar este produto congelado até o seu uso. Após Aberto e descongelado, consumir em até 12 horas.
            Nenhum produto após o descongelamento poderá ser recongelado.
            """)
    )
    db.session.add(product)
    db.session.commit()
    print "Product example created."
    return product


def create_blog_post_example():
    blog_post = BlogPost(
        title="Exemplo - Papinha é coisa séria"
    )
    db.session.add(blog_post)
    db.session.commit()
    print "Blog post example created."
    return blog_post


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
    for i in range(0, 300):
        db.session.add(get_random_order())
        print "Order " + str(i) + " created."
    db.session.commit()


def get_random_order():
    status = random.choice(
        filter(lambda order_status_id: order_status_id != R.id.ORDER_STATUS_ANY, Order.order_status_ids))
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

    return Client(
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
