# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 12/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import random
import sys

sys.path.append("/vagrant")
sys.path.append("/vagrant/build")

from app_contexts.app import app

from models.utils import create_random_product_categories, create_random_products, create_specif_cities, create_random_clients, create_random_orders, \
    create_random_product_subcategories, create_random_blog_posts

from proj_extensions import db

from models.about_us import AboutUs
from models.blog_post import BlogPost
from models.contact import Contact
from models.footer import Footer
from models.home_content import HomeContent
from models.product import Product
from models.product_category import ProductCategory
from models.tags_row import TagsRow

def fill_db_with_random_data():
    with app.app_context():
        create_random_product_categories()
        create_random_product_subcategories()
        create_random_products()
        create_specif_cities()
        create_random_clients()
        create_random_orders()
        create_random_blog_posts()

        create_footer_data()
        create_contact_data()
        create_about_us_data()
        create_tags_row_data()
        create_home_content_data()

def create_footer_data():
    footer = Footer.get()
    footer.lower_text_markdown = "Crescer Saudável  \nCNPJ 01.517.384/0001-87  \nITA Júnior © 2016 - 2017"
    db.session.add(footer)
    db.session.commit()

def create_contact_data():
    contact = Contact.get()

    contact.address_markdown = "Centervale Shopping  \nAv. Dep. Benedito Matarazzo, 9403  \nSão José dos Campos - SP"
    contact.tel = "(12) 32131-2321"
    contact.email = "contato@crescersaudavel.com"

    contact.facebook_active = True
    contact.facebook_link = "https://www.facebook.com/crescersaudavelni/"

    contact.youtube_active = True
    contact.youtube_link = "https://www.youtube.com/"

    contact.twitter_active = True
    contact.twitter_link = "https://twitter.com/"

    db.session.add(contact)
    db.session.commit()

def create_about_us_data():
    about_us = AboutUs.get()

    about_us.summary_markdown = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

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

    home_content.carousel_item_1_active = True
    home_content.carousel_item_1_title = "Título 1"
    home_content.carousel_item_1_subtitle = "Subtítulo 1"
    home_content.carousel_item_1_link = "/blog"
    home_content.carousel_item_1_image = "carousel_default.jpg"

    home_content.carousel_item_2_active = True
    home_content.carousel_item_2_title = "Título 2"
    home_content.carousel_item_2_image = "carousel_default.jpg"

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
        for subcategory in category.subcategories:
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
        for subcategory in category.subcategories:
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
        for subcategory in category.subcategories:
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
        for subcategory in category.subcategories:
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
        for subcategory in category.subcategories:
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
        for subcategory in category.subcategories:
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
    fill_db_with_random_data()
