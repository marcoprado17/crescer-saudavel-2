# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 25/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import url_for
from sqlalchemy import desc

from components.forms import NewsletterEmailForm
from models.about_us import AboutUs
from models.blog.blog_post import BlogPost
from models.contact import Contact
from models.footer import Footer
from r import R


class ClientFooterDataProvider(object):
    def get_data(self):
        chosen_categories = []

        chosen_blog_posts = []
        q = BlogPost.query
        q = q.filter(BlogPost.active == True)
        q = q.order_by(desc(BlogPost.date), desc("id"))

        for blog_post in q.slice(0, 4):
            chosen_blog_posts.append(
                dict(
                    title=blog_post.title,
                    href=url_for("client_blog.blog_post", **{R.string.blog_post_id_arg_name: blog_post.id}),
                )
            )

        contact = Contact.get()
        return dict(
            about_us_summary_html = AboutUs.get().summary_html,
            address_html=contact.address_html,
            tel=contact.tel,
            email=contact.email,
            social_networks=[
                dict(
                    is_facebook=True,
                    active=contact.facebook_active,
                    title=R.string.facebook,
                    classes="fb",
                    href=contact.facebook_link,
                ),
                dict(
                    active=contact.youtube_active,
                    title=R.string.youtube,
                    classes="youtube",
                    href=contact.youtube_link,
                ),
                dict(
                    active=contact.twitter_active,
                    title=R.string.twitter,
                    classes="tw",
                    href=contact.twitter_link,
                ),
                dict(
                    active=contact.googleplus_active,
                    title=R.string.google_plus,
                    classes="googleplus",
                    href=contact.googleplus_link,
                ),
                dict(
                    active=contact.pintrest_active,
                    title=R.string.pintrest,
                    classes="pintrest",
                    href=contact.pintrest_link,
                ),
            ],
            chosen_blog_posts=chosen_blog_posts,
            lower_text_html=Footer.get().lower_text_html,
            newsletter_email_form=NewsletterEmailForm()
        )


client_footer_data_provider = ClientFooterDataProvider()
