# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from enum import Enum, unique

from flask_bombril.utils import stringfy_list


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
        upload = "Enviar"
        add_image = "Adicionar nova imagem"
        allowed_image_extensions = ["png", "jpg", "jpeg"]
        image_sent_failure = "Ocorreu um erro no envio da imagem %(image_name)s."

        find_image = "Procurar imagem"
        upload_image_auxiliar_text = "Os formatos de imagem aceitos são: " + stringfy_list(allowed_image_extensions)

        images_table_id = "images"
        image_col_id = "image"
        image_name_col_id = "image-name"
        action_col_id = "action"

        remove_class = "remove"
        remove_image_url_meta_data_key = "data-remove-image-url"
        image_name_meta_data_key = "data-image-name"

        # Args name
        page_arg_name = "page"
        category_active_arg_name = "active"
        sort_method_arg_name = "sort_method"
        subcategory_active_arg_name = "active"
        category_id_arg_name = "category_id"

        name = "Nome"
        remove = "Remover"
        removing = "Removendo..."
        image_removed = "Imagem removida"
        remove_image_error = 'Ocorreu uma falha ao remover a imagem "{0}". Tente novamente.'
        no_items_found = "Nenhum item foi encontrado."

        # Admin products
        add_product_category = "Adicionar nova categoria de produto"
        add_product_subcategory = "Adicionar nova subcategoria de produto"
        add_product = "Adicionar novo produto"
        edit_product_category = "Editar categoria de produto"
        edit_product_subcategory = "Editar subcategoria de produto"
        add = "Adicionar"
        active_in_female = "Ativa"
        inactive_in_female = "Inativa"
        product_category_name = "Nome da categoria de produto"
        product_subcategory_name = "Nome da subcategoria de produto"
        product_categories = "Categorias de produto"
        product_categories_table_id = "product-categories"
        product_subcategories_table_id = "product-subcategories"
        product_category_name_col_id = "product-category-name"
        product_category_active_col_id = "product-category-active"
        product_subcategory_name_col_id = "product-subcategory-name"
        product_subcategory_active_col_id = "product-subcategory-active"
        category = "Categoria"
        subcategory = "Subcategoria"
        edit = "Editar"
        edit_class = "edit"
        href_meta_data_key = "data-href"
        category_name_meta_data_key = "data-category-name"
        subcategory_name_meta_data_key = "data-subcategory-name"
        to_activate = "Ativar"
        disable = "Desativar"
        hidden_class = "hidden"
        disable_class = "disable"
        to_activate_class = "to-activate"
        to_activate_btn_id_meta_data_key = "data-to-activate-btn-id"
        disable_btn_id_meta_data_key = "data-disable-btn-id"
        category_status = "Status da categoria"
        subcategory_status = "Status da subcategoria"
        filter = "Filtrar"
        select_field = "SelectField"
        submit_field = "SubmitField"
        disable_product_category_url_meta_data_key = "data-disable-product-category-url"
        disable_product_subcategory_url_meta_data_key = "data-disable-product-subcategory-url"
        to_activate_product_category_url_meta_data_key = "data-to-activate-product-category-url"
        to_activate_product_subcategory_url_meta_data_key = "data-to-activate-product-subcategory-url"
        activating = "Ativando..."
        activate_product_category_error = 'Ocorreu uma falha ao ativar a categoria de produto "{0}". Tente novamente.'
        activate_product_subcategory_error = 'Ocorreu uma falha ao ativar a subcategoria de produto "{0}". Tente novamente.'
        disable_product_category_error = 'Ocorreu uma falha ao desativar a categoria de produto "{0}". Tente novamente.'
        disable_product_subcategory_error = 'Ocorreu uma falha ao desativar a subcategoria de produto "{0}". Tente novamente.'
        disabling = "Desativando..."
        row_meta_data_key = "data-row"
        all = "Todas"
        product_subcategories = "Subcategorias de produto"
        title = "Título"
        dynamic_class = "dynamic"
        none_in_female = "Nenhuma"
        price = "Preço"
        stock_quantity = "Quantia no estoque"
        stop_sell_when_stock_low_than = "Parar de vender quando o estoque estiver abaixo de"
        summary = "Resumo"
        product_title_example = "Ex.: Papinha de maça - 500g"
        product_price_example = "Ex.: 8,80"
        product_stock_quantity_example = "Ex.: 42"
        product_stop_sell_stock_quantity_example = "Ex.: 5"
        product_summary_example = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
        markdown = "Markdown"
        example = "Exemplo"
        preview = "Pré-visualização"
        markdown_href = "https://dwoond.github.io/O-basico-de-Markdown/"
        close = "Fechar"
        loading = "Carregando..."
        markdown_preview_error = "Ocorreu uma falha na tradução do texto Markdown. Tente novamente."
        tab_title_example = "Ex.: Informação nutricional"
        active = "Ativo"

        tab_content_example = \
"""An h1 header
============

Paragraphs are separated by a blank line.

2nd paragraph. *Italic*, **bold**, and `monospace`. Itemized lists
look like:

  * this one
  * that one
  * the other one

Note that --- not considering the asterisk --- the actual text
content starts at 4-columns in.

> Block quotes are
> written like so.
>
> They can span multiple paragraphs,
> if you like.

Use 3 dashes for an em-dash. Use 2 dashes for ranges (ex., "it's all
in chapters 12--14"). Three dots ... will be converted to an ellipsis.
Unicode is supported. ☺



An h2 header
------------

Here's a numbered list:

 1. first item
 2. second item
 3. third item

Note again how the actual text starts at 4 columns in (4 characters
from the left side). Here's a code sample:

    # Let me re-iterate ...
    for i in 1 .. 10 { do-something(i) }

First Header | Second Header
------------ | -------------
Content Cell | Content Cell
Content Cell | Content Cell"""


        @staticmethod
        def image_sent_successfully(image_name):
            return 'A imagem "%s" foi enviada com sucesso.' % image_name

        @staticmethod
        def product_sent_successfully(title):
            return 'O produto "%s" foi adicionado com sucesso.' % title

        @staticmethod
        def product_category_sent_successfully(category_name):
            return 'A categoria de produto "%s" foi adicionada com sucesso.' % category_name

        @staticmethod
        def product_subcategory_sent_successfully(subcategory_name):
            return 'A subcategoria de produto "%s" foi adicionada com sucesso.' % subcategory_name

        @staticmethod
        def invalid_format(allowed_extensions):
            invalid_format_string = "Formato de arquivo inválido. "
            if len(allowed_extensions) == 1:
                invalid_format_string += "O único formato aceito é " + allowed_extensions[0] + "."
            else:
                invalid_format_string += "Os formatos aceitos são: "
                invalid_format_string += stringfy_list(allowed_extensions) + "."
            return invalid_format_string

        @staticmethod
        def n_items_found(n_items):
            if n_items == 1:
                return str(n_items) + " item encontrado."
            else:
                return str(n_items) + " items encontrados."

        @staticmethod
        def disable_category_button_id(category_id):
            return "disable-category-"+str(category_id)+"-btn"

        @staticmethod
        def disable_subcategory_button_id(subcategory_id):
            return "disable-subcategory-" + str(subcategory_id) + "-btn"

        @staticmethod
        def to_activate_category_button_id(category_id):
            return "to-activate-category-"+str(category_id)+"-btn"

        @staticmethod
        def to_activate_subcategory_button_id(subcategory_id):
            return "to-activate-subcategory-" + str(subcategory_id) + "-btn"

        @staticmethod
        def product_category_successful_edited(category_name):
            return 'A categoria de produto "%s" foi editada com sucesso.' % category_name

        @staticmethod
        def product_subcategory_successful_edited(subcategory_name):
            return 'A subcategoria de produto "%s" foi editada com sucesso.' % subcategory_name

        @staticmethod
        def n_image(n):
            return "%sº Imagem" % str(n)

        @staticmethod
        def n_tab_title(n):
            return "Título da %sº aba" % str(n)

        @staticmethod
        def n_tab_content(n):
            return "Conteúdo da %sº aba" % str(n)

    # noinspection PyPep8Naming
    @unique
    class id(Enum):
        # Admin navbar
        ADMIN_NAVBAR_HOME =                     1
        ADMIN_NAVBAR_PRODUCTS =                 2
        ADMIN_NAVBAR_ORDERS =                   3
        ADMIN_NAVBAR_BLOG =                     4
        ADMIN_NAVBAR_CUSTOMERS =                5
        ADMIN_NAVBAR_IMAGES =                   6
        ADMIN_NAVBAR_CONTENT =                  7
        ADMIN_NAVBAR_ATTENDED_CITIES =          8

        # Super table column types
        COL_TYPE_IMAGE =                        9
        COL_TYPE_TEXT =                         10
        COL_TYPE_ACTION =                       11
        COL_TYPE_BOOL =                         12

        # Super table action element types
        ACTION_TYPE_BUTTON =                    13

    # noinspection PyPep8Naming
    class dimen(object):
        example = 42
        min_page = 1
        product_category_max_length = 48
        product_subcategory_max_length = 48
        default_string_field_max_length = 4096
        tab_title_max_length = 48
        product_title_max_length = 96


R = Resources()
