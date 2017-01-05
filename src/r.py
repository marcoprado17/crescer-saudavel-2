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
        sort_method_arg_name = "sort-method"

        name = "Nome"
        remove = "Remover"
        removing = "Removendo..."
        image_removed = "Imagem removida"
        remove_image_error = 'Ocorreu uma falha ao remover a imagem "{0}". Tente novamente.'
        no_items_found = "Nenhum item foi encontrado."

        # Admin products
        add_product_category = "Adicionar nova categoria de produto"
        add_product_subcategory = "Adicionar nova subcategoria de produto"
        edit_product_category = "Editar categoria de produto"
        add = "Adicionar"
        active_in_female = "Ativa"
        inactive_in_female = "Inativa"
        product_category_name = "Nome da categoria de produto"
        product_subcategory_name = "Nome da subcategoria de produto"
        product_categories = "Categorias de produto"
        product_categories_table_id = "product-categories"
        product_category_name_col_id = "product-category-name"
        product_category_active_col_id = "product-category-active"
        category = "Categoria"
        edit = "Editar"
        edit_class = "edit"
        href_meta_data_key = "data-href"
        category_name_meta_data_key = "data-category-name"
        to_activate = "Ativar"
        disable = "Desativar"
        hidden_class = "hidden"
        disable_class = "disable"
        to_activate_class = "to-activate"
        to_activate_btn_id_meta_data_key = "data-to-activate-btn-id"
        disable_btn_id_meta_data_key = "data-disable-btn-id"
        category_status = "Status da categoria"
        filter = "Filtrar"
        select_field = "SelectField"
        submit_field = "SubmitField"
        disable_product_category_url_meta_data_key = "data-disable-product-category-url"
        to_activate_product_category_url_meta_data_key = "data-to-activate-product-category-url"
        activating = "Ativando..."
        activate_product_category_error = 'Ocorreu uma falha ao ativar a categoria de produto "{0}". Tente novamente.'
        disable_product_category_error = 'Ocorreu uma falha ao desativar a categoria de produto "{0}". Tente novamente.'
        disabling = "Desativando..."
        row_meta_data_key = "data-row"
        all = "Todas"

        @staticmethod
        def image_sent_successfully(image_name):
            return 'A imagem "%s" foi enviada com sucesso.' % image_name

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
        def to_activate_category_button_id(category_id):
            return "to-activate-category-"+str(category_id)+"-btn"

        @staticmethod
        def product_category_successful_edited(category_name):
            return 'A categoria de produto "%s" foi editada com sucesso.' % category_name

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


R = Resources()
