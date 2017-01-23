# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 13/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SelectField, SubmitField, TextAreaField
from wtforms.fields.html5 import TelField

from flask_bombril.form_validators import EmailFormat
from flask_bombril.form_validators import Length
from flask_bombril.form_validators import MarkdownValidator
from flask_bombril.form_validators.phone_fomat.phone_format import PhoneFormat
from models.blog_post import BlogPost
from models.product import Product
from r import R
from proj_utils import get_image_choices, safe_string


class CarouselForm(FlaskForm):
    active = BooleanField(
        label=R.string.active,
        default=False
    )
    title = StringField(
        label=R.string.title,
        validators=[
            Length(max_length=R.dimen.carousel_title_max_length)
        ])
    subtitle = StringField(
        label=R.string.subtitle,
        validators=[
            Length(max_length=R.dimen.carousel_subtitle_max_length)
        ])
    image = SelectField(
        label=R.string.image,
    )

    submit = SubmitField(label=R.string.save)

    def __init__(self, **kwargs):
        super(CarouselForm, self).__init__(**kwargs)
        self.image.choices = get_image_choices(include_none=True)

    def set_values(self, home_content, carousel_number):
        assert carousel_number in range(1, 3+1)
        if carousel_number == 1:
            self.active.data = home_content.carousel_item_1_active
            self.title.data = home_content.carousel_item_1_title
            self.subtitle.data = home_content.carousel_item_1_subtitle
            self.image.data = home_content.carousel_item_1_image
        elif carousel_number == 2:
            self.active.data = home_content.carousel_item_2_active
            self.title.data = home_content.carousel_item_2_title
            self.subtitle.data = home_content.carousel_item_2_subtitle
            self.image.data = home_content.carousel_item_2_image
        else:
            self.active.data = home_content.carousel_item_3_active
            self.title.data = home_content.carousel_item_3_title
            self.subtitle.data = home_content.carousel_item_3_subtitle
            self.image.data = home_content.carousel_item_3_image

class ProductSectionForm(FlaskForm):
    active = BooleanField(
        label=R.string.active_in_female,
        default=False
    )
    name = StringField(
        label=R.string.section_name,
        validators=[
            Length(max_length=R.dimen.product_section_name_max_length)
        ])
    product_1_id = SelectField(label=R.string.get_product_n(1))
    product_2_id = SelectField(label=R.string.get_product_n(2))
    product_3_id = SelectField(label=R.string.get_product_n(3))
    product_4_id = SelectField(label=R.string.get_product_n(4))
    product_5_id = SelectField(label=R.string.get_product_n(5))
    product_6_id = SelectField(label=R.string.get_product_n(6))
    product_7_id = SelectField(label=R.string.get_product_n(7))
    product_8_id = SelectField(label=R.string.get_product_n(8))
    product_9_id = SelectField(label=R.string.get_product_n(9))
    product_10_id = SelectField(label=R.string.get_product_n(10))
    product_11_id = SelectField(label=R.string.get_product_n(11))
    product_12_id = SelectField(label=R.string.get_product_n(12))
    product_13_id = SelectField(label=R.string.get_product_n(13))
    product_14_id = SelectField(label=R.string.get_product_n(14))
    product_15_id = SelectField(label=R.string.get_product_n(15))
    product_16_id = SelectField(label=R.string.get_product_n(16))
    product_17_id = SelectField(label=R.string.get_product_n(17))
    product_18_id = SelectField(label=R.string.get_product_n(18))
    product_19_id = SelectField(label=R.string.get_product_n(19))
    product_20_id = SelectField(label=R.string.get_product_n(20))

    submit = SubmitField(label=R.string.save)

    def __init__(self, **kwargs):
        super(ProductSectionForm, self).__init__(**kwargs)
        product_choices_with_none = Product.get_choices(include_none=True)
        self.product_1_id.choices = product_choices_with_none
        self.product_2_id.choices = product_choices_with_none
        self.product_3_id.choices = product_choices_with_none
        self.product_4_id.choices = product_choices_with_none
        self.product_5_id.choices = product_choices_with_none
        self.product_6_id.choices = product_choices_with_none
        self.product_7_id.choices = product_choices_with_none
        self.product_8_id.choices = product_choices_with_none
        self.product_9_id.choices = product_choices_with_none
        self.product_10_id.choices = product_choices_with_none
        self.product_11_id.choices = product_choices_with_none
        self.product_12_id.choices = product_choices_with_none
        self.product_13_id.choices = product_choices_with_none
        self.product_14_id.choices = product_choices_with_none
        self.product_15_id.choices = product_choices_with_none
        self.product_16_id.choices = product_choices_with_none
        self.product_17_id.choices = product_choices_with_none
        self.product_18_id.choices = product_choices_with_none
        self.product_19_id.choices = product_choices_with_none
        self.product_20_id.choices = product_choices_with_none

    def set_values(self, home_content, product_section_number):
        assert product_section_number in range(1, 5+1)
        if product_section_number == 1:
            self.active.data = home_content.product_section_1_active
            self.name.data = home_content.product_section_1_name
            self.product_1_id.data = str(home_content.product_section_1_product_1_id)
            self.product_2_id.data = str(home_content.product_section_1_product_2_id)
            self.product_3_id.data = str(home_content.product_section_1_product_3_id)
            self.product_4_id.data = str(home_content.product_section_1_product_4_id)
            self.product_5_id.data = str(home_content.product_section_1_product_5_id)
            self.product_6_id.data = str(home_content.product_section_1_product_6_id)
            self.product_7_id.data = str(home_content.product_section_1_product_7_id)
            self.product_8_id.data = str(home_content.product_section_1_product_8_id)
            self.product_9_id.data = str(home_content.product_section_1_product_9_id)
            self.product_10_id.data = str(home_content.product_section_1_product_10_id)
            self.product_11_id.data = str(home_content.product_section_1_product_11_id)
            self.product_12_id.data = str(home_content.product_section_1_product_12_id)
            self.product_13_id.data = str(home_content.product_section_1_product_13_id)
            self.product_14_id.data = str(home_content.product_section_1_product_14_id)
            self.product_15_id.data = str(home_content.product_section_1_product_15_id)
            self.product_16_id.data = str(home_content.product_section_1_product_16_id)
            self.product_17_id.data = str(home_content.product_section_1_product_17_id)
            self.product_18_id.data = str(home_content.product_section_1_product_18_id)
            self.product_19_id.data = str(home_content.product_section_1_product_19_id)
            self.product_20_id.data = str(home_content.product_section_1_product_20_id)
        elif product_section_number == 2:
            self.active.data = home_content.product_section_2_active
            self.name.data = home_content.product_section_2_name
            self.product_1_id.data = str(home_content.product_section_2_product_1_id)
            self.product_2_id.data = str(home_content.product_section_2_product_2_id)
            self.product_3_id.data = str(home_content.product_section_2_product_3_id)
            self.product_4_id.data = str(home_content.product_section_2_product_4_id)
            self.product_5_id.data = str(home_content.product_section_2_product_5_id)
            self.product_6_id.data = str(home_content.product_section_2_product_6_id)
            self.product_7_id.data = str(home_content.product_section_2_product_7_id)
            self.product_8_id.data = str(home_content.product_section_2_product_8_id)
            self.product_9_id.data = str(home_content.product_section_2_product_9_id)
            self.product_10_id.data = str(home_content.product_section_2_product_10_id)
            self.product_11_id.data = str(home_content.product_section_2_product_11_id)
            self.product_12_id.data = str(home_content.product_section_2_product_12_id)
            self.product_13_id.data = str(home_content.product_section_2_product_13_id)
            self.product_14_id.data = str(home_content.product_section_2_product_14_id)
            self.product_15_id.data = str(home_content.product_section_2_product_15_id)
            self.product_16_id.data = str(home_content.product_section_2_product_16_id)
            self.product_17_id.data = str(home_content.product_section_2_product_17_id)
            self.product_18_id.data = str(home_content.product_section_2_product_18_id)
            self.product_19_id.data = str(home_content.product_section_2_product_19_id)
            self.product_20_id.data = str(home_content.product_section_2_product_20_id)
        elif product_section_number == 3:
            self.active.data = home_content.product_section_3_active
            self.name.data = home_content.product_section_3_name
            self.product_1_id.data = str(home_content.product_section_3_product_1_id)
            self.product_2_id.data = str(home_content.product_section_3_product_2_id)
            self.product_3_id.data = str(home_content.product_section_3_product_3_id)
            self.product_4_id.data = str(home_content.product_section_3_product_4_id)
            self.product_5_id.data = str(home_content.product_section_3_product_5_id)
            self.product_6_id.data = str(home_content.product_section_3_product_6_id)
            self.product_7_id.data = str(home_content.product_section_3_product_7_id)
            self.product_8_id.data = str(home_content.product_section_3_product_8_id)
            self.product_9_id.data = str(home_content.product_section_3_product_9_id)
            self.product_10_id.data = str(home_content.product_section_3_product_10_id)
            self.product_11_id.data = str(home_content.product_section_3_product_11_id)
            self.product_12_id.data = str(home_content.product_section_3_product_12_id)
            self.product_13_id.data = str(home_content.product_section_3_product_13_id)
            self.product_14_id.data = str(home_content.product_section_3_product_14_id)
            self.product_15_id.data = str(home_content.product_section_3_product_15_id)
            self.product_16_id.data = str(home_content.product_section_3_product_16_id)
            self.product_17_id.data = str(home_content.product_section_3_product_17_id)
            self.product_18_id.data = str(home_content.product_section_3_product_18_id)
            self.product_19_id.data = str(home_content.product_section_3_product_19_id)
            self.product_20_id.data = str(home_content.product_section_3_product_20_id)
        elif product_section_number == 4:
            self.active.data = home_content.product_section_4_active
            self.name.data = home_content.product_section_4_name
            self.product_1_id.data = str(home_content.product_section_4_product_1_id)
            self.product_2_id.data = str(home_content.product_section_4_product_2_id)
            self.product_3_id.data = str(home_content.product_section_4_product_3_id)
            self.product_4_id.data = str(home_content.product_section_4_product_4_id)
            self.product_5_id.data = str(home_content.product_section_4_product_5_id)
            self.product_6_id.data = str(home_content.product_section_4_product_6_id)
            self.product_7_id.data = str(home_content.product_section_4_product_7_id)
            self.product_8_id.data = str(home_content.product_section_4_product_8_id)
            self.product_9_id.data = str(home_content.product_section_4_product_9_id)
            self.product_10_id.data = str(home_content.product_section_4_product_10_id)
            self.product_11_id.data = str(home_content.product_section_4_product_11_id)
            self.product_12_id.data = str(home_content.product_section_4_product_12_id)
            self.product_13_id.data = str(home_content.product_section_4_product_13_id)
            self.product_14_id.data = str(home_content.product_section_4_product_14_id)
            self.product_15_id.data = str(home_content.product_section_4_product_15_id)
            self.product_16_id.data = str(home_content.product_section_4_product_16_id)
            self.product_17_id.data = str(home_content.product_section_4_product_17_id)
            self.product_18_id.data = str(home_content.product_section_4_product_18_id)
            self.product_19_id.data = str(home_content.product_section_4_product_19_id)
            self.product_20_id.data = str(home_content.product_section_4_product_20_id)
        elif product_section_number == 5:
            self.active.data = home_content.product_section_5_active
            self.name.data = home_content.product_section_5_name
            self.product_1_id.data = str(home_content.product_section_5_product_1_id)
            self.product_2_id.data = str(home_content.product_section_5_product_2_id)
            self.product_3_id.data = str(home_content.product_section_5_product_3_id)
            self.product_4_id.data = str(home_content.product_section_5_product_4_id)
            self.product_5_id.data = str(home_content.product_section_5_product_5_id)
            self.product_6_id.data = str(home_content.product_section_5_product_6_id)
            self.product_7_id.data = str(home_content.product_section_5_product_7_id)
            self.product_8_id.data = str(home_content.product_section_5_product_8_id)
            self.product_9_id.data = str(home_content.product_section_5_product_9_id)
            self.product_10_id.data = str(home_content.product_section_5_product_10_id)
            self.product_11_id.data = str(home_content.product_section_5_product_11_id)
            self.product_12_id.data = str(home_content.product_section_5_product_12_id)
            self.product_13_id.data = str(home_content.product_section_5_product_13_id)
            self.product_14_id.data = str(home_content.product_section_5_product_14_id)
            self.product_15_id.data = str(home_content.product_section_5_product_15_id)
            self.product_16_id.data = str(home_content.product_section_5_product_16_id)
            self.product_17_id.data = str(home_content.product_section_5_product_17_id)
            self.product_18_id.data = str(home_content.product_section_5_product_18_id)
            self.product_19_id.data = str(home_content.product_section_5_product_19_id)
            self.product_20_id.data = str(home_content.product_section_5_product_20_id)

class BlogSectionForm(FlaskForm):
    active = BooleanField(
        label=R.string.active_in_female,
        default=False
    )
    name = StringField(
        label=R.string.section_name,
        validators=[
            Length(max_length=R.dimen.blog_section_name_max_length)
        ])
    post_1_id = SelectField(label=R.string.get_post_n(1))
    post_2_id = SelectField(label=R.string.get_post_n(2))

    submit = SubmitField(label=R.string.save)

    def __init__(self, **kwargs):
        super(BlogSectionForm, self).__init__(**kwargs)
        post_choices_with_none = BlogPost.get_choices(include_none=True)
        self.post_1_id.choices = post_choices_with_none
        self.post_2_id.choices = post_choices_with_none

    def set_values(self, home_content, blog_section_number):
        assert blog_section_number in range(1, 3+1)
        if blog_section_number == 1:
            self.active.data = home_content.blog_section_1_active
            self.name.data = home_content.blog_section_1_name
            self.post_1_id.data = str(home_content.blog_section_1_post_1_id)
            self.post_2_id.data = str(home_content.blog_section_1_post_2_id)
        elif blog_section_number == 2:
            self.active.data = home_content.blog_section_2_active
            self.name.data = home_content.blog_section_2_name
            self.post_1_id.data = str(home_content.blog_section_2_post_1_id)
            self.post_2_id.data = str(home_content.blog_section_2_post_2_id)
        else:
            self.active.data = home_content.blog_section_3_active
            self.name.data = home_content.blog_section_3_name
            self.post_1_id.data = str(home_content.blog_section_3_post_1_id)
            self.post_2_id.data = str(home_content.blog_section_3_post_2_id)


class ContactForm(FlaskForm):
    address = StringField(
        label=R.string.address,
        validators=[
            Length(max_length=R.dimen.contact_address_max_length)
        ])
    tel = TelField(
        label=R.string.telephone,
        validators=[
            PhoneFormat(can_be_empty=True),
            Length(max_length=R.dimen.tel_max_length)
        ]
    )
    email = StringField(
        label=R.string.email,
        validators=[
            EmailFormat(can_be_empty=True),
            Length(max_length=R.dimen.email_max_length)
        ]
    )

    facebook_active = BooleanField(
        label=R.string.active,
        default=False
    )
    facebook_link = StringField(
        label=R.string.link
    )

    googleplus_active = BooleanField(
        label=R.string.active,
        default=False
    )
    googleplus_link = StringField(
        label=R.string.link
    )

    twitter_active = BooleanField(
        label=R.string.active,
        default=False
    )
    twitter_link = StringField(
        label=R.string.link
    )

    youtube_active = BooleanField(
        label=R.string.active,
        default=False
    )
    youtube_link = StringField(
        label=R.string.link
    )

    pintrest_active = BooleanField(
        label=R.string.active,
        default=False
    )
    pintrest_link = StringField(
        label=R.string.link
    )

    submit = SubmitField(label=R.string.save)

    def set_values(self, contact):
        self.address.data = contact.address
        self.tel.data = contact.tel
        self.email.data = contact.email

        self.facebook_active.data = contact.facebook_active
        self.facebook_link.data = safe_string(contact.facebook_link)

        self.googleplus_active.data = contact.googleplus_active
        self.googleplus_link.data = safe_string(contact.googleplus_link)

        self.twitter_active.data = contact.twitter_active
        self.twitter_link.data = safe_string(contact.twitter_link)

        self.youtube_active.data = contact.youtube_active
        self.youtube_link.data = safe_string(contact.youtube_link)

        self.pintrest_active.data = contact.pintrest_active
        self.pintrest_link.data = safe_string(contact.pintrest_link)


class AboutUsForm(FlaskForm):
    content = TextAreaField(
        label=R.string.content,
        validators=[
            MarkdownValidator()
        ]
    )
    submit = SubmitField(label=R.string.save)

    def set_values(self, about_us):
        self.content.data = about_us.content


class FaqForm(FlaskForm):
    content = TextAreaField(
        label=R.string.content,
        validators=[
            MarkdownValidator()
        ]
    )
    submit = SubmitField(label=R.string.save)

    def set_values(self, faq):
        self.content.data = faq.content


class FooterForm(FlaskForm):
    lower_text = StringField(
        label=R.string.lower_text,
        validators=[
            Length(max_length=R.dimen.footer_lower_text_max_length)
        ]
    )
    submit = SubmitField(label=R.string.save)

    def set_values(self, footer):
        self.lower_text.data = footer.lower_text
