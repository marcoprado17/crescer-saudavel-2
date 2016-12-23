# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from enum import Enum, unique


class Resources(object):

    # noinspection PyPep8Naming
    class string(object):
        temp_error_html = "Ocorreu um erro inesperado em nossos servidores, nossa equipe técnica resolverá o problema assim que possível. Clique <a href=%(home_page_href)s>aqui</a> para voltar à pagina inicial."

        admin = "Admin"

        # Admin navbar
        admin_dashboard = "Painel Administrativo"
        home = "Home"
        products = "Produtos"
        add_new_product = "Adicionar novo produto"
        view_edit_remove_products = "Visualizar / editar / remover produtos"
        add_new_category = "Adicionar nova categoria"
        view_edit_remove_categories = "Visualizar / editar / remover categorias"
        add_new_subcategory = "Adicionar nova subcategoria"
        view_edit_remove_subcategories = "Visualizar / editar / remover subcategorias"
        orders = "Pedidos"
        blog = "Blog"
        add_new_post = "Adicionar novo post"
        view_edit_remove_posts = "Visualizar / editar / remover posts"
        customers = "Clientes"
        images = "Images"
        add_new_image = "Adicionar nova imagem"
        view_remove_images = "Visualizar / remover imagems"
        content = "Conteúdo"
        contact = "Contato"
        about_us = "Sobre nós"
        faq = "FAQ"
        attended_cities = "Cidades atendidas"
        add_new_city = "Adicionar nova cidade"
        view_remove_cities = "Visualizar / remover cidades"

    # noinspection PyPep8Naming
    @unique
    class id(Enum):
        # Admin navbar
        ADMIN_NAVBAR_HOME                       = 1
        ADMIN_NAVBAR_PRODUCTS                   = 2
        ADMIN_NAVBAR_ORDERS                     = 3
        ADMIN_NAVBAR_BLOG                       = 4
        ADMIN_NAVBAR_CUSTOMERS                  = 5
        ADMIN_NAVBAR_IMAGES                     = 6
        ADMIN_NAVBAR_CONTENT                    = 7
        ADMIN_NAVBAR_ATTENDED_CITIES            = 8

    # noinspection PyPep8Naming
    class dimen(object):
        example = 42

R = Resources()
