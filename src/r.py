# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from enum import Enum, unique


class Resources(object):

    # noinspection PyPep8Naming
    class string(object):
        and_word = "e"
        comma = ","
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
        images = "Imagens"
        add_new_image = "Adicionar nova imagem"
        view_remove_images = "Visualizar / remover imagens"
        content = "Conteúdo"
        contact = "Contato"
        about_us = "Sobre nós"
        faq = "FAQ"
        attended_cities = "Cidades atendidas"
        add_new_city = "Adicionar nova cidade"
        view_remove_cities = "Visualizar / remover cidades"

        # Admin image
        no_file_selected = "Nenhum arquivo foi selecionado."
        image = "Imagem"
        upload = "Upload"
        add_image = "Adicionar imagem"
        png = "png"
        jpg = "jpg"
        jpeg = "jpeg"

        find_file = "Encontrar arquivo"

        @staticmethod
        def invalid_format(allowed_extensions):
            invalid_format_string = "Formato de arquivo inválido. "
            if len(allowed_extensions) == 1:
                invalid_format_string += "O único formato aceito é " + allowed_extensions[0] + "."
            else:
                invalid_format_string += "Os formatos aceitos são: "
                allowed_extensions_string = ""
                first_idx = 0
                last_idx = len(allowed_extensions)-1
                for idx, extension in enumerate(allowed_extensions):
                    if idx == first_idx:
                        allowed_extensions_string = extension
                    elif idx == last_idx:
                        allowed_extensions_string += " " + R.string.and_word + " " + extension + "."
                    else:
                        allowed_extensions_string += R.string.comma + " " + extension
                invalid_format_string += allowed_extensions_string
            return invalid_format_string


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
