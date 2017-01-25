# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 25/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================


class ClientFooterDataProvider(object):
    def get_data(self):
        return dict(
            address="Rua ..., n 25, SJC - SP",
            tel="(11) 1234-5678",
            email="email@email.com",
            social_networks=[
                dict(
                    title="Facebook",
                    classes="fb",
                    href="#",
                ),
                dict(
                    title="Twitter",
                    classes="tw",
                    href="#",
                ),
                dict(
                    title="Google Plus",
                    classes="googleplus",
                    href="#",
                ),
                dict(
                    title="Youtube",
                    classes="youtube",
                    href="#",
                ),
            ],
            products=[
                dict(
                    name="Frutas",
                    category_id="1",
                ),
                dict(
                    name="Sopa creme",
                    category_id="2",
                ),
                dict(
                    name="Sopa com pedaços",
                    category_id="3",
                ),
                dict(
                    name="Linha Single",
                    category_id="4",
                ),
                dict(
                    name="Linha Emporinho",
                    category_id="5",
                ),
            ],
            blog_posts=[
                dict(
                    title="Título do post 0",
                    blog_post_id="0",
                ),
                dict(
                    title="Título do post 1",
                    blog_post_id="1",
                ),
                dict(
                    title="Título do post 2",
                    blog_post_id="2",
                ),
                dict(
                    title="Título do post 3",
                    blog_post_id="3",
                ),
                dict(
                    title="Título do post 4",
                    blog_post_id="4",
                ),
            ],
            copyright_text="Copyright © 2016 - Crescer Saudável",
        )


client_footer_data_provider = ClientFooterDataProvider()
