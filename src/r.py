# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from decimal import Decimal
from time import strftime

from enum import Enum, unique
from flask import url_for

from flask_bombril.utils import stringfy_list


class Resources(object):
    # noinspection PyPep8Naming
    class dict(object):
        column_labels = dict(
            name="Nome",
            active="Ativo",
            state="Estado",
            cities="Cidades",
            subcategories="Subcategorias",
            products="Produtos",
            priority="Prioridade",
            category="Categoria",
            product_category="Categoria de produto",
            product_subcategory="Subcategoria de produto",
            title="Título",
            price="Preço",
            has_discount="Possui desconto",
            discount_percentage="Percentual de desconto",
            stock="Estoque",
            subcategory="Subcategoria",
            summary_markdown="Resumo",
            min_available="Mín. disponíveis",
            image_type="Tipo",
            filename="Nome do arquivo",
            image="Imagem",
            link="Link",
            image_1="Imagem 1",
            image_2="Imagem 2",
            image_3="Imagem 3",
            image_4="Imagem 4",
            tab_1_active="Tab 1 ativa",
            tab_2_active="Tab 2 ativa",
            tab_3_active="Tab 3 ativa",
            tab_4_active="Tab 4 ativa",
            tab_5_active="Tab 5 ativa",
            tab_1_title="Título da tab 1",
            tab_2_title="Título da tab 2",
            tab_3_title="Título da tab 3",
            tab_4_title="Título da tab 4",
            tab_5_title="Título da tab 5",
            tab_1_content_markdown="Conteúdo da tab 1",
            tab_2_content_markdown="Conteúdo da tab 2",
            tab_3_content_markdown="Conteúdo da tab 3",
            tab_4_content_markdown="Conteúdo da tab 4",
            tab_5_content_markdown="Conteúdo da tab 5",
            price_with_discount="Preço com desconto",
            reserved="Reservadas",
            n_units_available="Num. de unidades disponíveis",
            date="Data",
            content_markdown="Conteúdo",
            summary_html="Resumo",
            content_html="Conteúdo",
            lower_text_html="Texto inferior",
            lower_text_markdown="Texto inferior",
            n_visible_categories="Número de categorias visíveis",
            address_html="Endereço",
            facebook_active="Facebook",
            youtube_active="Youtube",
            twitter_active="Twitter",
            googleplus_active="Google+",
            pintrest_active="Pintrest",
            address_markdown="Endereço",
            facebook_link="Facebook link",
            youtube_link="Youtube link",
            twitter_link="Twitter link",
            googleplus_link="Google+ link",
            pintrest_link="Pintrest link",
            carousel_1_image_filename="Imagem do carrossel 1",
            carousel_1_active="Carrossel 1 ativo",
            carousel_1_title="Título do carrossel 1",
            carousel_1_subtitle="Subtítulo do carrossel 1",
            carousel_1_link="Link do carrossel 1",
            carousel_2_image_filename="Imagem do carrossel 2",
            carousel_2_active="Carrossel 2 ativo",
            carousel_2_title="Título do carrossel 2",
            carousel_2_subtitle="Subtítulo do carrossel 2",
            carousel_2_link="Link do carrossel 2",
            carousel_3_image_filename="Imagem do carrossel 3",
            carousel_3_active="Carrossel 3 ativo",
            carousel_3_title="Título do carrossel 3",
            carousel_3_subtitle="Subtítulo do carrossel 3",
            carousel_3_link="Link do carrossel 3",
            product_section_1_active="Seção de produto 1 ativa",
            product_section_1_name="Nome da seção de produto 1",
            product_section_1_link="Link da seção de produto 1",
            products_of_section_1="Produtos da seção 1",
            product_section_2_active="Seção de produto 2 ativa",
            product_section_2_name="Nome da seção de produto 2",
            product_section_2_link="Link da seção de produto 2",
            products_of_section_2="Produtos da seção 2",
            product_section_3_active="Seção de produto 3 ativa",
            product_section_3_name="Nome da seção de produto 3",
            product_section_3_link="Link da seção de produto 3",
            products_of_section_3="Produtos da seção 3",
            product_section_4_active="Seção de produto 4 ativa",
            product_section_4_name="Nome da seção de produto 4",
            product_section_4_link="Link da seção de produto 4",
            products_of_section_4="Produtos da seção 4",
            product_section_5_active="Seção de produto 5 ativa",
            product_section_5_name="Nome da seção de produto 5",
            product_section_5_link="Link da seção de produto 5",
            products_of_section_5="Produtos da seção 5",
            more_categories_section_category_1="Categoria 1 da seção 'Mais para você'",
            more_categories_section_category_1_image_filename="Imagem da categoria 1 da seção 'Mais para você'",
            more_categories_section_category_1_subcategories="Subcategorias da categoria 1 da seção 'Mais para você'",
            more_categories_section_category_2="Categoria 2 da seção 'Mais para você'",
            more_categories_section_category_2_image_filename="Imagem da categoria 2 da seção 'Mais para você'",
            more_categories_section_category_2_subcategories="Subcategorias da categoria 2 da seção 'Mais para você'",
            more_categories_section_category_3="Categoria 3 da seção 'Mais para você'",
            more_categories_section_category_3_image_filename="Imagem da categoria 3 da seção 'Mais para você'",
            more_categories_section_category_3_subcategories="Subcategorias da categoria 3 da seção 'Mais para você'",
            more_categories_section_category_4="Categoria 4 da seção 'Mais para você'",
            more_categories_section_category_4_image_filename="Imagem da categoria 4 da seção 'Mais para você'",
            more_categories_section_category_4_subcategories="Subcategorias da categoria 4 da seção 'Mais para você'",
            more_categories_section_category_5="Categoria 5 da seção 'Mais para você'",
            more_categories_section_category_5_image_filename="Imagem da categoria 5 da seção 'Mais para você'",
            more_categories_section_category_5_subcategories="Subcategorias da categoria 5 da seção 'Mais para você'",
            more_categories_section_category_6="Categoria 6 da seção 'Mais para você'",
            more_categories_section_category_6_image_filename="Imagem da categoria 6 da seção 'Mais para você'",
            more_categories_section_category_6_subcategories="Subcategorias da categoria 6 da seção 'Mais para você'",
            blog_section_1_active="Seção 1 do blog ativa",
            blog_section_1_name="Nome da seção 1 de blog",
            blog_section_1_link="Link da seção 1 de blog",
            blog_section_1_post_1="Post 1 da seção 1 de blog",
            blog_section_1_post_2="Post 2 da seção 1 de blog",
            blog_section_2_active="Seção 2 do blog ativa",
            blog_section_2_name="Nome da seção 2 de blog",
            blog_section_2_link="Link da seção 2 de blog",
            blog_section_2_post_1="Post 1 da seção 2 de blog",
            blog_section_2_post_2="Post 2 da seção 2 de blog",
            blog_section_3_active="Seção 3 do blog ativa",
            blog_section_3_name="Nome da seção 3 de blog",
            blog_section_3_link="Link da seção 3 de blog",
            blog_section_3_post_1="Post 1 da seção 3 de blog",
            blog_section_3_post_2="Post 2 da seção 3 de blog",
            thumbnail_image="Imagem da thumbnail",
            image_1_filename="Imagem 1",
            image_2_filename="Imagem 2",
            image_3_filename="Imagem 3",
            image_4_filename="Imagem 4",
            sales_number="Número de vendas",
            tab_1_content_html="Conteúdo da tab 1",
            tab_2_content_html="Conteúdo da tab 2",
            tab_3_content_html="Conteúdo da tab 3",
            tab_4_content_html="Conteúdo da tab 4",
            tab_5_content_html="Conteúdo da tab 5",
            tag_1_active="Tag 1 ativa",
            tag_1_image_filename="Imagem da tag 1",
            tag_1_title="Título da tag 1",
            tag_1_subtitle="Subtítulo da tag 1",
            tag_2_active="Tag 2 ativa",
            tag_2_image_filename="Imagem da tag 2",
            tag_2_title="Título da tag 2",
            tag_2_subtitle="Subtítulo da tag 2",
            tag_3_active="Tag 3 ativa",
            tag_3_image_filename="Imagem da tag 3",
            tag_3_title="Título da tag 3",
            tag_3_subtitle="Subtítulo da tag 3",
            tag_4_active="Tag 4 ativa",
            tag_4_image_filename="Imagem da tag 4",
            tag_4_title="Título da tag 4",
            tag_4_subtitle="Subtítulo da tag 4",
            city="Cidade",
            email_confirmed="Email confirmado",
            register_datetime="Hora e dia do registro",
            first_name="Nome",
            last_name="Sobrenome",
            address="Endereço",
            address_number="Número",
            address_complement="Complemento",
            client_email="Email do cliente",
            paid_datetime="Data e hora do pagamento",
            sent_datetime="Data e hora do envio",
            delivered_datetime="Data e hora da entrega",
            total_price="Valor total do pedido",
            products_total_price="Preço total dos produtos",
            freight="Frete",
            orders="Pedidos"
        )

    # noinspection PyPep8Naming
    class string(object):
        change_status = "mudar-status"
        my_information = "Minhas informações"
        resend_confirmation_email_query = "Deseja reenviar o email de confirmação?"
        resend_confirmation_email_auxiliar_text = "Entre com o email cadastrado, reenviaremos o link para confirmação do email."
        resend_confirmation_email = "Reenviar email de confirmação"
        password_successful_redefined = "Sua senha foi redefinida com sucesso."
        invalid_redefine_password_requisition = "A requisição de redefinição de senha em questão expirou. Por favor, faça outra requisição de redefinição de senha."
        forgot_password_or_want_redefine_it = "Esqueceu sua senha ou quer redefini-la?"
        want_redefine_your_password = "Quer redefinir sua senha?"
        redefine_password = "Redefinir senha"
        send_redefine_password_email_error_message = "Ocorreu uma falha no envio do email de redefinição de senha. Por favor, tente novamente."
        recovery_password_message = "Entre com o email cadastrado, enviaremos um link para a redefinição da senha."
        recovery_password = "Recuperar senha"
        forgot_password = "Esqueceu sua senha?"
        admin_login_required = "É preciso entrar como admin para acessar tal página."
        login_message = "Para acessar a página é preciso entrar na sua conta."
        login_error = "Ocorreu uma falha ao entrar na sua conta. Por favor, tente novamente."
        to_enter = "Entrar"
        not_has_account = "Não possui conta?"
        new_account = "Nova conta"
        login = "Entrar"
        send_confirmation_email_error_message = "Ocorreu uma falha no envio do email de confirmação. Por favor, tente novamente."
        data_base_access_error_message = "Ocorreu uma falha ao acessar o banco de dados. Por favor, tente novamente."
        email_already_in_use = "Este email já está em uso."
        already_has_account = "Já possui conta?"
        to_register = "Cadastrar"
        new_client = "Novo cliente"
        password_mismatch_message = "As senhas digitadas não são iguais."
        password = "Senha"
        password_confirmation = "Confirmação de senha"
        email_example_placeholder = "Ex.: exemplo@gmail.com"
        without_stock = "Sem estoque"
        product_images_text = "Tamanho ideal das imagens de produto: 600 x 600.<br><br>"
        blog_thumbnail_text = "Tamanho ideal das thumbnails do blog: 900 x 500.<br><br>"
        carousel_image_text = "Tamanho ideal das imagens do carrossel: 2560 x 500."
        more_categories_image_text = "Tamanho ideal da imagem: 512 x 512."
        post_thumbnail = "Thumbnail do post"
        order_by = "Ordenar por: "
        inner_link_example = "Ex.: /produtos/?category_id=1"
        blog_thumbnail_default_filename = "blog_thumbnail_default.jpg"
        blog_thumbnail_wide_default_filename = "blog_thumbnail_wide_default.jpg"
        carousel_default_filename = "carousel_default.jpg"
        more_categories_default_filename = "more_categories_default.jpg"
        unavailable_product_at_moment = "Produto indisponível no momento."
        product_image = "Imagem do produto"
        product_images = "Imagens dos produtos"
        product_images_endpoint = "imagens-de-produto"
        products_endpoint="produtos"
        images_endpoint = "imagens"
        add_to_cart = "Adicionar ao carrinho"
        default_product_image_name = "product_default.jpg"
        back_to_blog = "Voltar ao blog"
        post = "Post"
        previous_page = "Página anterior"
        next_page = "Próxima página"
        read_more = "Ler mais"
        back_to_home = "Voltar para Home"
        or_word = "ou"
        finalize_purchase = "Finalizar compra"
        purchase_finalization = "Finalização de compra"
        view_cart = "Ver Carrinho"
        to_search = "Buscar"
        search = "Busca"
        enter = "Entre"
        my_account = "Minha conta"
        enter_with_your_email = "Digite seu e-mail"
        register = "Cadastre-se"
        signup_newsletter = "Assine nossa newsletter"
        fixed = "Fixa"
        signup = "Assinar"
        signing = "Assinando..."
        newsletter_sign_error_msg = "Ocorreu uma falha ao cadastrar seu email em nosso newsletter. Por favor, cheque seu email e tente novamente."
        newsletter_sign_success_msg = "O email <b>{0}</b> foi registrado com sucesso em nossa newsletter!"
        sign = "Assinar"
        contact = "Contato"
        contact_endpoint = "contato"
        company = "Empresa"
        can_not_be_removed = "Não pode ser removida"
        test_price = "1,11"
        test1 = "test1"
        footer_lower_text_example = "Crescer saudável\n\nCNPJ 01.517.384/0001-87\n\n© 2016 - 2017 "
        lower_text = "Texto inferior"
        edit_footer = "Editar rodapé"
        edit_header = "Editar cabeçalho"
        thumbnail = "Thumbnail"
        thumbnail_tooltip = "Imagem principal do post em questão"
        tabs = "Abas"
        admin_welcome_message = "Seja bem vindo admin!"
        fixed_images_tooltip = "Imagens fixas não podem ser removidas e nem atualizadas."
        irremovable = "Irremovível"
        irremovable_images_tooltip = "Imagens irremovíveis não podem ser removidas, mas podem ser atualizadas ao se adicionar uma nova imagem com o mesmo nome."
        previous_posts = "Posts anteriores"

        lowest_reserved = "Menor nº de unid. reservadas"
        higher_reserved = "Maior nº de unid. reservadas"

        lowest_available = "Menor nº de unid. disponíveis"
        higher_available = "Maior nº de unid. disponíveis"

        none_in_masculine = "Nenhum"

        and_word = "e"
        comma = ","
        temp_error_html = "Ocorreu um erro inesperado em nossos servidores, nossa equipe técnica resolverá o problema assim que possível. Clique <a href=%(home_page_href)s>aqui</a> para voltar para a página inicial."

        admin = "Admin"

        # Admin navbar
        admin_dashboard = "Painel Administrativo"
        home = "Home"
        products = "Produtos"
        add_new_product = "Adicionar novo produto"
        products_table = "Tabela produtos"
        add_new_category = "Adicionar nova categoria"
        categories_table = "Tabela de categorias"
        add_new_subcategory = "Adicionar nova subcategoria"
        subcategories_table = "Tabela de subcategorias"
        orders = "Pedidos"
        orders_endpoint = "pedidos"
        blog = "Blog"
        add_new_post = "Adicionar novo post"
        posts_table = "Tabela de posts"
        customers = "Clientes"
        images = "Imagens"
        add_new_image = "Adicionar nova imagem"
        images_table = "Tabela de imagens"
        content = "Conteúdo"
        about_us = "Sobre nós"
        faq = "FAQ"
        faq_endpoint = "faq"
        attended_cities = "Cidades atendidas"
        add_new_city = "Adicionar nova cidade"
        cities_table = "Tabela de cidades"
        order_space_at_end = "Pedido "

        # Admin image
        no_file_selected = "Nenhum arquivo foi selecionado."
        image = "Imagem"
        upload = "Enviar"
        add_image = "Adicionar nova imagem"
        allowed_image_extensions = ["png", "jpg", "jpeg"]
        image_sent_failure = "Ocorreu um erro no envio da imagem %(image_name)s."

        find_image = "Procurar imagem"
        upload_image_auxiliar_text = "Os formatos de imagem aceitos são: " + stringfy_list(allowed_image_extensions) + "."

        images_table_id = "images-table"
        products_table_id = "products-table"
        image_col_id = "image"
        image_name_col_id = "image-name"
        action_col_id = "action"


        remove_class = "remove"
        remove_image_url_meta_data_key = "data-remove-image-url"
        image_name_meta_data_key = "data-image-name"

        # Args name
        page_arg_name = "pagina"
        category_active_arg_name = "active"
        sort_method_arg_name = "sort_method"
        subcategory_active_arg_name = "active"
        category_id_arg_name = "category_id"
        subcategory_id_arg_name = "subcategory_id"
        order_status_id_arg_name = "status"
        state_id_arg_name = "state_id"
        city_id_arg_name = "city_id"
        active_arg_name = "active"
        blog_post_id_arg_name = "blog_post_id"
        search_string_arg_name = "q"
        product_id_arg_name = "product_id"
        email_arg_name = "email"
        edit_arg_name = "editar"
        amount_arg_name = "quantia"
        redirect_to_cart_arg_name = "redirecionar_ao_carrinho"
        step_arg_name = "passo"
        search_query_arg_name = "q"

        name = "Nome"
        section_name = "Nome de seção"
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
        edit_product = "Editar produto"
        add = "Adicionar"
        active_in_female = "Ativa"
        inactive_in_female = "Inativa"
        inactive = "Inativo"
        product_category_name = "Nome da categoria de produto"
        product_subcategory_name = "Nome da subcategoria de produto"
        product_categories = "Categorias de produto"
        product_categories_table_id = "product-categories-table"
        product_subcategories_table_id = "product-subcategories-table"
        product_category_name_col_id = "product-category-name"
        product_category_active_col_id = "product-category-active"
        product_active_col_id = "product-active-col"
        product_title_col_id = "product-title-col"
        product_subcategory_name_col_id = "product-subcategory-name"
        product_subcategory_active_col_id = "product-subcategory-active"
        category = "Categoria"
        subcategory = "Subcategoria"
        edit = "Editar"
        add_to_stock = "Adicionar ao estoque"
        remove_from_stock = "Remover do estoque"
        update_stock = "Atualizar estoque"
        edit_class = "edit"
        href_meta_data_key = "data-href"
        category_name_meta_data_key = "data-category-name"
        subcategory_name_meta_data_key = "data-subcategory-name"
        product_title_meta_data_key = "data-product-title"
        to_activate = "Ativar"
        disable = "Desativar"
        hidden_class = "hidden"
        disable_class = "disable"
        add_to_stock_class = "add-to-stock"
        remove_from_stock_class = "remove-from-stock"
        update_stock_class = "update-stock"
        to_activate_class = "to-activate"
        to_activate_btn_id_meta_data_key = "data-to-activate-btn-id"
        disable_btn_id_meta_data_key = "data-disable-btn-id"
        category_status = "Status da categoria"
        blog_posts_status = "Status do post"
        subcategory_status = "Status da subcategoria"
        order_status = "Status do pedido"
        filter = "Filtrar"
        select_field = "SelectField"
        select_field_with_classes = "SelectFieldWithClasses"
        submit_field = "SubmitField"
        disable_product_category_url_meta_data_key = "data-disable-product-category-url"
        disable_product_subcategory_url_meta_data_key = "data-disable-product-subcategory-url"
        disable_product_url_meta_data_key = "data-disable-product-url"
        to_activate_product_category_url_meta_data_key = "data-to-activate-product-category-url"
        to_activate_product_subcategory_url_meta_data_key = "data-to-activate-product-subcategory-url"
        to_activate_product_url_meta_data_key = "data-to-activate-product-url"
        activating = "Ativando..."
        activate_product_category_error = 'Ocorreu uma falha ao ativar a categoria de produto "{0}". Tente novamente.'
        activate_product_subcategory_error = 'Ocorreu uma falha ao ativar a subcategoria de produto "{0}". Tente novamente.'
        disable_product_category_error = 'Ocorreu uma falha ao desativar a categoria de produto "{0}". Tente novamente.'
        disable_product_subcategory_error = 'Ocorreu uma falha ao desativar a subcategoria de produto "{0}". Tente novamente.'
        disabling = "Desativando..."
        row_meta_data_key = "data-row"
        all = "Todas"
        all_in_masculine = "Todos"
        any = "Qualquer"
        product_subcategories = "Subcategorias de produto"
        title = "Título"
        subtitle = "Subtítulo"
        dynamic_class = "dynamic"
        none_in_female = "Nenhuma"
        price = "Preço"
        stock_quantity = "Quantia no estoque"
        stop_sell_when_stock_low_than = "Parar de vender quando o estoque estiver abaixo de"
        summary = "Resumo"
        product_title_placeholder = "Ex.: Papinha de maça - 500g"
        product_price_placeholder = "Ex.: 8.80"
        product_stock_quantity_placeholder = "Ex.: 42"
        product_stop_sell_stock_quantity_placeholder = "Ex.: 5"
        markdown = "Markdown"
        example = "Exemplo"
        preview = "Pré-visualização"
        markdown_href = "https://dwoond.github.io/O-basico-de-Markdown/"
        close = "Fechar"
        loading = "Carregando..."
        markdown_preview_error = "Ocorreu uma falha na tradução do texto Markdown. Tente novamente."
        tab_title_placeholder = "Ex.: Informação nutricional"
        active = "Ativo"
        product_category_col_id = "product-category-col"
        product_price_col_id = "product-price-col"
        price_in_real = "Preço em R$"
        product_stock_col_id = "product-stock-col"
        in_stock = "Em estoque"
        product_min_stock_col_id = "product-min-stock-col"
        min_available = "Mín. Disponíveis"
        min_available_description = "Quando o número de unidades disponíveis do produto atingir o valor estabelecido em mín. disponíveis, o produto não será mais disponibilizado para venda na loja virtual."
        product_sales_number_col_id = "product-sales-number-col"
        sales = "Vendas"
        sort_method_label = "Ordenar por:"
        empty_symbol = "-"
        id_prefix = "#"
        product_default_filename = "product_default.jpg"
        tag_default_filename = "tag_default.jpg"
        categories = "Categorias"
        none = "Nenhuma"

        lowest_price = "Menor preço"
        higher_price = "Maior preço"
        lowest_stock = "Menor estoque"
        higher_stock = "Maior estoque"
        best_seller = "Mais vendido"
        less_sold = "Menos vendido"

        product_status = "Status do produto"
        example_42 = "Ex.: 42"
        updating = "Atualizando..."
        adding = "Adicionando..."

        client_email = "Email do cliente"
        client_name = "Nome do cliente"
        newest = "Mais recente"
        older = "Mais antigo"
        newest_register = "Cadastro mais recente"
        older_register = "Cadastro mais antigo"

        paid = "Pago"
        sent = "Enviado"
        delivered = "Entregue"

        client = "Cliente"
        order_products_price_tooltip = "Preço total dos produtos em R$"
        status = "Status"
        paid_date = "Data do pagamento"
        paid_date_tooltip = "Data em que o pedido foi pago pelo cliente."
        sent_date = "Data do envio"
        sent_date_tooltip = "Data em que o pedido foi marcado como enviado."
        delivered_date = "Data da entrega"
        delivered_date_tooltip = "Data em que o pedido foi marcado como entregue."
        id = "Id"
        details = "Detalhes"
        subtotal = "Subtotal"
        freight = "Frete"
        total = "Total"
        mark_as_sent = "Marcar como enviado"
        unmark_as_sent = "Desmarcar como enviado"
        mark_as_delivered = "Marcar como entregue"
        unmark_as_delivered = "Desmarcar como entregue"
        checking = "Marcando..."
        unchecking = "Desmarcando..."
        order_status_change_error = "Não foi possivel alterar o status do pedido #{0}. Tente novamente."
        mark_as_sent_confirmation = 'Você tem certeza que deseja marcar o pedido como enviado? Um email será automaticamente enviado para: {0}.'
        mark_as_canceled_confirmation = 'Você tem certeza que deseja cancelar o pedido? Um email será automaticamente enviado para: {0}.'
        canceling = "Cancelando..."
        canceled = "Cancelado"
        email = "Email"
        email_confirmed = "Email confirmado"
        first_name = "Nome"
        last_name = "Sobrenome"
        state = "Estado"
        city = "Cidade"
        address = "Endereço"
        number = "Número"
        complement = "Complemento"
        cep = "CEP"
        telephone = "Telefone"
        undefined_masculine = "Indefinido"
        undefined_feminine = "Indefinida"
        products_of_order = "Produtos do pedido"
        amount = "Quantia"
        product_title = "Título do produto"
        subtotal_tooltip = "Valor do produto multiplicado por sua quantia (em R$)"
        product_price_description = "Valor do produto em R$.\nPreço original, sem desconto.\nUsar '.' para separar os centavos da unidade."
        order_total_value = "Valor total do pedido"
        register_date = "Data de cadastro"
        clients = "Clientes"
        clients_endpoint = "clientes"
        orders_of_client = "Pedidos do cliente"
        no_orders_registered = "Nenhum pedido cadastrado."
        product = "Produto"
        client_data = "Dados do cliente"
        city_name = "Nome da cidade"
        edit_city = "Editar cidade"
        save = "Salvar"
        saving = "Salvando..."
        edit_home_content = 'Editar conteúdo da página "Home"'
        carousel = "Carrossel"
        product_sections = "Seções de produto"
        blog_sections = "Seções do blog"
        edit_contact_information = "Editar informações de contato"
        main_info = "Principais informações"
        social_networks = "Redes sociais"
        link = "Link"
        just_enter_numbers = "Digite apenas os números."
        facebook = "Facebook"
        twitter = "Twitter"
        google_plus = "Google+"
        pintrest = "Pintrest"
        youtube = "Youtube"
        save_contact_error_msg = "Não foi possível salvar os novos dados de contato. Verifique os valores e tente novamente."
        save_contact_success_msg = "Os dados de contato foram atualizados com sucesso."
        save_tags_error_msg = "Não foi possível salvar os novos dados das tags. Verifique os valores e tente novamente."
        save_tags_success_msg = "Os dados das tags foram atualizados com sucesso."
        save_about_us_error_msg = 'Não foi possível salvar os novos dados da página "Sobre nós". Verifique os valores e tente novamente.'
        save_about_us_success_msg = 'Os dados da página "Sobre nós" foram atualizados com sucesso.'
        save_faq_error_msg = 'Não foi possível salvar os novos dados da página "FAQ". Verifique os valores e tente novamente.'
        save_payment_error_msg = 'Não foi possível salvar os novos dados da página "Pagamento". Verifique os valores e tente novamente.'
        save_dispatch_error_msg = 'Não foi possível salvar os novos dados da página "Envio". Verifique os valores e tente novamente.'
        save_exchanges_and_returns_error_msg = 'Não foi possível salvar os novos dados da página "Trocas & Devoluções". Verifique os valores e tente novamente.'
        save_faq_success_msg = 'Os dados da página "FAQ" foram atualizados com sucesso.'
        save_payment_success_msg = 'Os dados da página "Pagamento" foram atualizados com sucesso.'
        save_dispatch_success_msg = 'Os dados da página "Envio" foram atualizados com sucesso.'
        save_exchanges_and_returns_success_msg = 'Os dados da página "Trocas & Devoluções" foram atualizados com sucesso.'
        save_footer_error_msg = 'Não foi possível salvar os novos dados do rodapé. Verifique os valores e tente novamente.'
        save_header_error_msg = 'Não foi possível salvar os novos dados do cabeçalho. Verifique os valores e tente novamente.'
        save_footer_success_msg = 'Os dados do rodapé foram atualizados com sucesso.'
        save_header_success_msg = 'Os dados do cabeçalho foram atualizados com sucesso.'
        edit_about_us_page_content = 'Editar conteúdo da página "Sobre nós"'
        edit_faq_page_content = 'Editar conteúdo da página "FAQ"'
        edit_payment_page_content = 'Editar conteúdo da página "Pagamento"'
        edit_dispatch_page_content = 'Editar conteúdo da página "Envio"'
        edit_exchanges_and_returns_page_content = 'Editar conteúdo da página "Trocas & Devoluções"'
        footer = "Rodapé"
        footer_endpoint = "rodape"
        date = "Data"
        default_date_format = "%d/%m/%Y"
        default_datetime_format = "%d/%m/%Y\n%H:%M"
        default_datetime_format_with_hifen = "%d/%m/%Y - %H:%M"
        day_format = "%d"
        month_format = "%b"
        posts = "Posts"
        edit_post = "Editar post"
        product_category_example = "Ex.: Frutas"
        product_subcategory_example = "Ex.: Frutas vermelhas"
        product_category = "Categoria de produto"
        tel_example = "(12) 2352-2458"
        email_example = "contato@crescersaudavel.com"
        blog_post_title_placeholder = "Ex.: Nutricionista fala sobre introdução dos alimentos nas papinhas dos bebês"
        thumbnail_alt = "Imagem principal do post"

        blog_example_title = "Nutricionista fala sobre introdução dos alimentos nas papinhas dos bebês"
        blog_example_thumbnail = "post_exemplo_bebe_comendo.jpg"
        product_category_example_name = "Frutas"
        carousel_title_placeholder = "Ex.: Conheça nossa loja física"
        carousel_subtitle_placeholder = "Ex.: Localização: Shopping Centervale - São José dos Campos"
        carousel_link_placeholder = "Ex.: /blog"
        product_section_name_placeholder = "Ex.: Novidades"
        product_section_link_placeholder = "Ex.: /blog"
        blog_section_name_example = "Ex.: Posts mais recentes"
        tel_placeholder = "Ex.: (12) 2352-2458"
        email_placeholder = "Ex.: contato@crescersaudavel.com"
        link_placeholder = "Ex.: https://www.google.com.br"
        city_placeholder = "Ex.: São José dos Campos"
        category_name = "Nome da categoria"
        subcategory_name = "Nome da subcategoria"
        cancel_order = "Cancelar pedido"
        mark_as_paid = "Marcar como pago"
        available = "Disponíveis"
        available_tooltip = "Número de unidades disponíveis do produto, equivale ao número de unidades no estoque menos o número de unidades reservadas."
        reserved = "Reservadas"
        reserved_description = "Número de unidades reservadas do produto, já foram vendidas, mas ainda não foram enviadas."
        cancel = "Cancelar"
        facebook_link_placeholder = "Ex.: https://www.facebook.com"
        youtube_link_placeholder = "Ex.: https://www.youtube.com"
        twitter_link_placeholder = "Ex.: https://twitter.com"
        googleplus_link_placeholder = "Ex.: https://plus.google.com/?hl=pt_BR"
        pintrest_link_placeholder = "Ex.: https://br.pinterest.com/"

        first_name_placeholder="Ex.: João"
        last_name_placeholder="Ex.: Silva Mendes"
        cep_placeholder = "Ex.: 12210-250"
        number_placeholder = "Ex.: 460"
        address_complement_placeholder = "Ex.: Blc. A, Apt. 72"
        user_info_address_placeholder = "Ex.: R. Siqueira Campos - Centro"
        my_orders = "Meus pedidos"
        none_order_registered = "Nenhum pedido registrado."
        details_of_order_space_at_end = "Detalhes do pedido "
        status_label = "Status: "
        paid_date_label = "Data do pagamento: "
        sent_date_label = "Data do envio: "
        delivered_date_label = "Data da entrega: "
        basic_info = "Informações básicas"
        order_total_tooltip = "Valor total do pedido, produtos + frete, em R$"
        lowest_total_price = "Menor preço total"
        higher_total_price = "Maior preço total"
        my_cart = "Meu carrinho"
        keep_buying = "Continuar comprando"
        clean_cart = "Limpar carrinho"
        purchase_total = "Total da compra"
        cart_empty = "Carrinho vazio!"
        add_to_cart_error_msg_invalid_product_id = "Não foi possível adicionar o produto ao seu carrinho. O id do produto é inválido."
        anonymous_user_id = "anonymous_user_id"
        unit_price = "Preço da unid."
        quantity = "Quantidade"
        cart_cleared = "Todos os produtos do carrinho foram removidos com sucesso."
        add_cart_fail_invalid_product = "Não foi possível adicionar o produto ao carrinho, o produto em questão é inválido."
        product_stock_limit_reached = "O limite do estoque deste produto foi atingido."
        store_logo = "Logo da loja"
        logout = "Sair"
        step_1_title = "1"
        step_2_title = "2"
        step_3_title = "3"
        delivery_address = "Endereço de entrega"
        cart = "Carrinho"
        continue_text = "Continuar"
        confirm_purchase = "Confirmar compra"
        edit_items = "Editar items"
        payment = "Pagamento"
        payment_endpoint = "pagamento"
        fix_form_errors_before_proceed = "Conserte os erros no formulário antes de prosseguir."
        product_not_found = "Nenhum produto foi encontrado."
        blog_posts = "Posts do Blog"
        no_results_were_found = "Nenhum resultado foi encontrado."
        register_with_facebook = "Cadastrar pelo Facebook"
        or_text = "ou"
        registering = "Cadastrando..."
        facebook_register_error_msg = "Ocorreu uma falha ao tentar cadastrá-lo pelo Facebook. Por favor, tente novamente."
        users_registered_with_facebook_cant_redefine_password = "Usuários cadastrados utilizando o Facebook não podem redefinir sua senha."
        users_registered_with_facebook_no_need_confirm_email = "Usuários cadastrados utilizando o Facebook não precisam confirmar o email."
        enter_with_facebook = "Entrar pelo Facebook"
        entering = "Entrando..."
        facebook_login_error_msg = "Ocorreu uma falha ao tentar entrar pelo Facebook. Por favor, tente novamente."
        successful_facebook_login = "Você entrou com sucesso pelo Facebook."
        successful_login = "Você entrou na sua conta com sucesso."
        csrf_token = "csrf_token"
        comments = "Comentários"
        how_can_we_help_you = "Como podemos te ajudar?"
        hello = "Olá"
        others = "Outros"
        n_visible_categories = "Número de categorias visíveis"
        n_visible_categories_placeholder = "Ex.: 5"
        header = "Cabeçalho"
        header_endpoint = "cabecalho"
        priority = "Prioridade"
        product_category_priority_tooltip = "Prioridade na exibição dessa categoria de produto no menu de navegação, a categoria com maior prioridade será exibida primeiro e a categoria com menor prioridade será exibida por último."
        product_category_priority_placeholder = "Ex.: 10"
        buy = "Comprar"
        product_active = "Produto ativo"
        discount_active = "Desconto ativo"
        discount = "Percentual de desconto"
        price_with_discount = "Preço com desconto"
        complete_content = "Conteúdo completo"
        dispatch = "Envio"
        dispatch_endpoint = "envio"
        exchanges_and_returns = "Trocas & Devoluções"
        exchanges_and_returns_endpoint = "trocas-e-devolucoes"
        read_more_plus = "Leia mais +"
        utilities = "Utilidades"
        payment_methods = "Formas de pagamento"
        what_do_we_have_more_for_you_section = "Seção o que temos mais para você"
        what_do_we_have_more_for_you_title = "Olha só o que mais temos para você!"
        stay_in = "Fique por dentro!"
        stay_in_auxiliar_message = "Assine nosso newsletter e receba nossas promoções e novidades."
        tags_content = "Conteúdo das tags"
        tags = "Tags"
        tags_endpoint = "tags"
        unavailable = "Indisponível"
        your_email = "Seu email"
        discount_from = "De: "
        discount_to = "Por: "
        buy_100_percent_safe = "Compra 100% segura"
        description = "Descrição"
        additional_information = "Informações Adicionais"
        add_edit_form_error = "Erro! Por favor, cheque os campos e tente novamente."
        add_image_error = "Erro ao se adicionar a imagem! Por favor, cheque o arquivo selecionado e tente novamente."
        new_password = "Nova senha"
        new_password_confirmation = "Confirmação da nova senha"
        states = "Estados"
        cities = "Cidades"
        blog_thumbnail = "Thumbnail do blog"
        other = "Outro"
        filename_already_exist = "Um arquivo com o mesmo nome já existe."
        blog_thumbnail_images = "Imagens das thumbnails do blog"
        blog_thumbnail_image = "Imagem da thumbnail"
        blog_thumbnail_images_endpoint = "imagens-das-thumbnails-do-blog"
        product_subcategories_endpoint = "subcategorias-de-produto"
        product_categories_endpoint = "categorias-de-produto"
        cities_endpoint = "cidades"
        carousel_images = "Imagens do carousel"
        carousel_images_endpoint = "imagens-do-carrossel"
        other_images = "Outras imagens"
        other_images_endpoint = "outras-imagens"
        blog_posts_endpoint = "posts-do-blog"
        image_1 = "Imagem 1"
        image_2 = "Imagem 2"
        image_3 = "Imagem 3"
        image_4 = "Imagem 4"
        blog_tags = "Tags do blog"
        blog_tags_endpoint = "tags-do-blog"
        blog_tag_name_placeholder = "Ex.: Comidas saudáveis"
        about_us_endpoint = "sobre-nos"
        home_content = "Conteúdo da home"
        home_content_endpoint = "conteudo-da-home"
        tag_title_placeholder = "Ex.: Frete grátis"
        tag_subtitle_placeholder = "Ex.: Para São José dos Campos para compras acima de R$ 50,00"
        send_email_when_update_order_status = "Enviar email para o cliente ao alterar o status"
        change_status = "Alterar status"
        new_status = "Novo status:"
        change_order_status_confirmation_message = "Você tem certeza que deseja alterar o status do pedido '#{0}' para '{1}'?"
        shop_diminutive = "Lojinha"
        who_we_are = "Quem somos"
        more_recent_posts = "Posts mais recentes"
        order_id = "Id do pedido"
        product_total_price = "Preço total dos produtos"
        no_posts_found = "Nenhum post encontrado."

        facebook_link_example = "https://www.facebook.com/crescersaudavelni/"
        youtube_link_example = "https://www.youtube.com/"
        twitter_link_example = "https://twitter.com/"

        product_example_title = "Banana orgânica 100g"
        product_example_image_1 = "banana_exemplo_1.jpg"
        product_example_image_2 = "banana_exemplo_2.jpg"
        product_example_image_3 = "banana_exemplo_3.jpg"
        product_example_summary = \
"""A papinha de banana orgânica é saborosa, com uma textura muito agradável para os babys.
Além disso, possui o beneficio de acalmar o estômago e ajudar na digestão.
"""
        product_example_tab_1_title = "Preparação"
        product_example_tab_1_content = \
"""#### Produto Congelado:
1. Retirar o rótulo e a tampa.
2. Aquecer em microondas por 01 minuto ou em banho maria por 15 minutos, mexendo de vez em quando.
3. Verifique a temperatura. Antes de consumir, misturar uniformemente o conteúdo.

#### Produto descongelado (em refrigeração por 12 horas):
1. Retirar o rótulo e a tampa.
2. Aquecer em microondas por 01 minuto ou em banho maria por 10 minutos mexendo de vez em quando.
3. Verifique a temperatura. Antes de consumir, misturar uniformemente o conteúdo."""
        product_example_tab_2_title = "Ingredientes"
        product_example_tab_2_content = \
"""\* Para uma porção de **100g**

Ingrediente     | Quantidade
--------------- | ----------
Banana orgânica | 75g
Água            | 20ml
Açúcar mascavo  | 5g"""
        product_example_tab_3_title = "Informação nutricional"
        product_example_tab_3_content = \
"""\* Para uma porção de **100g**

Tipo de nutriente  | Quantidade
------------------ | ----------
Carboidratos       | 87g
Proteínas          | 9,2g
Gorduras totais    | 0g
Gorduras saturadas | 0g
Gorduras trans     | 0g
Fibra alimentar    | 3,8g

Valor energético: 94 kcal"""
        product_example_tab_4_title = "Benefícios"
        product_example_tab_4_content = \
"""* Rica em potássio, perfeita para baixar a pressão arterial.
* Ricas em fibras, a inclusão de bananas nas dietas ajuda a normalizar o trânsito intestinal, permitindo melhorar os
problemas de constipação sem o uso de laxantes.
* A banana acalma o estômago e ajuda na digestão."""
        product_example_tab_5_title = "Conservação"
        product_example_tab_5_content = \
"""Conservar este produto congelado até o seu uso. Após Aberto e descongelado, consumir em até 12 horas.
Nenhum produto após o descongelamento poderá ser recongelado."""

        address_example = \
"Centervale Shopping  \nAv. Dep. Benedito Matarazzo, 9403  \nSão José dos Campos - SP"

        lower_text_example = "Crescer Saudável  \nCNPJ 01.517.384/0001-87  \nITA Júnior © 2016 - 2017"

        tab_content_example = \
"""##Preparação
#### Produto Congelado:
1. Retirar o rótulo e a tampa.
2. Aquecer em microondas por 01 minuto ou em banho maria por 15 minutos, mexendo de vez em quando.
3. Verifique a temperatura. Antes de consumir, misturar uniformemente o conteúdo.

#### Produto descongelado (em refrigeração por 12 horas):
1. Retirar o rótulo e a tampa.
2. Aquecer em microondas por 01 minuto ou em banho maria por 10 minutos mexendo de vez em quando.
3. Verifique a temperatura. Antes de consumir, misturar uniformemente o conteúdo.
___
##Ingredientes
\* Para uma porção de **100g**

Ingrediente     | Quantidade
--------------- | ----------
Banana orgânica | 75g
Água            | 20ml
Açúcar mascavo  | 5g

___
##Informação Nutricional
\* Para uma porção de **100g**

Tipo de nutriente  | Quantidade
------------------ | ----------
Carboidratos       | 87g
Proteínas          | 9,2g
Gorduras totais    | 0g
Gorduras saturadas | 0g
Gorduras trans     | 0g
Fibra alimentar    | 3,8g

Valor energético: 94 kcal
___
##Benefícios
* Rica em potássio, perfeita para baixar a pressão arterial.
* Ricas em fibras, a inclusão de bananas nas dietas ajuda a normalizar o trânsito intestinal, permitindo melhorar os
problemas de constipação sem o uso de laxantes.
* A banana acalma o estômago e ajuda na digestão.
___
##Conservação
Conservar este produto congelado até o seu uso. Após Aberto e descongelado, consumir em até 12 horas.
Nenhum produto após o descongelamento poderá ser recongelado.
"""

        paragraph_example = \
"""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

        about_us_summary_example = \
"""Lorem ipsum dolor sit amet, vitae in etiam. Dignissim rutrum, phasellus arcu nibh hendrerit vel ridiculus eget, eget sit. Feugiat scelerisque risus. Fusce sit quis massa, wisi eu mauris curabitur. Et turpis in lectus neque, wisi eget, turpis in sed elementum, donec sed, nisl non odio eget. Magna maecenas aliquam, posuere viverra ante, turpis ipsum sociis vel porta. Mauris varius velit morbi non blandit sem, in tincidunt, ligula luctus orci condimentum risus ipsum, lacus lacus luctus. Lacinia parturient pellentesque duis. Dolor scelerisque odio eu pede at, integer vitae nunc tenetur wisi, dui cubilia tempor ullamcorper.
"""

        about_us_content_example = \
"""Lorem ipsum dolor sit amet, vitae in etiam. Dignissim rutrum, phasellus arcu nibh hendrerit vel ridiculus eget, eget sit. Feugiat scelerisque risus. Fusce sit quis massa, wisi eu mauris curabitur. Et turpis in lectus neque, wisi eget, turpis in sed elementum, donec sed, nisl non odio eget. Magna maecenas aliquam, posuere viverra ante, turpis ipsum sociis vel porta. Mauris varius velit morbi non blandit sem, in tincidunt, ligula luctus orci condimentum risus ipsum, lacus lacus luctus. Lacinia parturient pellentesque duis. Dolor scelerisque odio eu pede at, integer vitae nunc tenetur wisi, dui cubilia tempor ullamcorper.

Tempor eu fusce, sodales proin gravida cras felis libero, tempor eu mauris vestibulum. Penatibus dapibus egestas risus wisi quis, in eleifend, ornare nec, elit quis, nibh integer curabitur metus. Id dictum vivamus, ac urna temporibus nibh nullam. Nunc faucibus. Vitae id, posuere consectetuer ut lobortis vehicula vulputate purus, morbi curabitur, ultricies odio cum et quisque velit ut, tincidunt nulla auctor faucibus in tristique. Est etiam, donec sit aliquam duis, sed tortor suspendisse et habitasse odio vivamus. Libero ligula pede amet vestibulum, nunc leo, pede id duis rutrum. Quam lacinia justo ac, consequat nisl et et donec pharetra ornare, leo dapibus, eu nulla, amet mauris donec lectus voluptas elementum turpis. Quisque justo pretium neque eros pede, quisque pede, elit hendrerit quam fusce pharetra diam, pellentesque phasellus reiciendis congue euismod, irure in id pretium porttitor sagittis nihil. Felis lorem velit nisl velit sed ipsum, imperdiet morbi, volutpat leo litora curabitur tellus pharetra at, adipiscing congue duis id aliquam mauris varius, nulla fusce faucibus ac.
"""

        faq_content_example = \
"""1. **Pergunta 1?**

    Lorem ipsum dolor sit amet, non hac elit quam, et turpis scelerisque vivamus.

2. **Pergunta 2?**

    Lorem ipsum dolor sit amet, non hac elit quam, et turpis scelerisque vivamus. Ut neque lectus diam et,
curabitur est platea nisl nec nulla.

    Sagittis non arcu dis, neque non [link](https://www.google.com) aliquet autem cupidatat, at nulla neque nulla aliquet, mi turpis ipsum faucibus,
habitasse sodales urna. Congue convallis a pellentesque pretium non, rutrum sollicitudin vestibulum quam iaculis,
eget sem euismod, lobortis lectus vel.

3. **Pergunta 3?**

    Eros vehicula justo platea adipiscing pulvinar, donec accumsan, metus metus
metus, integer sed est. Non dignissim felis cras tortor.
"""

        blog_post_summary_example = \
"""A nutricionista *Karin Honorato*, dá dicas sobre a introdução dos alimentos nas papinhas dos bebês. Ela destaca os cuidados para que esta introdução seja feita de forma a beneficiar toda a vida da criança.
"""

        blog_post_content_example = \
"""A melhor idade para o bebê começar a comer as papinhas salgadas é a partir do sexto mês, conforme a nutricionista Karin afirma que o ponto mais importante neste momento, é a introdução de um alimento de cada vez. Desta forma, é possível observar se o bebê tem alguma reação ou mudança no intestino. Ela indica que cada alimento deve ser dado por dois ou três dias seguidos.

###Ordem dos alimentos
***
O primeiro tipo de alimento para uma papinha é o tubérculo ou raiz, como batata, batata doce, inhame e cará. A mandioca só pode ser introduzida a partir do nono mês, destaca. Ela recomenda fazer um purê, com o leite que o bebê já consome.

![Batata doce](https://abrilboaforma.files.wordpress.com/2016/10/batata-doce-emagrece.jpg?quality=85&strip=all&w=680&h=453&crop=1 "Batata doce")

Depois de introduzido o tubérculo, é hora de acrescentar um legume. Pode ser: chuchu, abóbora, abobrinha, cenoura, tomate, vagem e até jiló. Quanto ao jiló, que tem um sabor mais amargo, Karin afirma que é importante as crianças conhecerem todos os alimentos e sabores.

![Abóbora](/static/imgs/other/post_link_example.jpg "Abóbora")

Os próximos alimentos a serem introduzidos, conforme a nutricionista, são as verduras: brócolis, couve, almeirão. Neste caso, as folhas devem ser acrescentadas no fim do preparo, ficando no fogo por no máximo oito minutos. A verdura deve ser batida no liquidificador com parte do caldo da sopa.

####Lista (ordenada) dos alimentos:
1. Tubérculo ou raiz, como batata, batata doce, inhame e cará.
2. Legume, como chuchu, abóbora, abobrinha, cenoura, tomate, vagem e até jiló.
3. Verduras, com brócolis e couve, almeirão.
4. Carnes, como frango sem pele, patinho acém ou músculos (moídos ou cozidos).

####Lista (não ordenada) dos alimentos:
* Tubérculo ou raiz, como batata, batata doce, inhame e cará.
* Legume, como chuchu, abóbora, abobrinha, cenoura, tomate, vagem e até jiló.
* Verduras, com brócolis e couve, almeirão.
* Carnes, como frango sem pele, patinho acém ou músculos (moídos ou cozidos).

####Tabela dos alimentos:
Ordem | Alimento
- | -
1° | Tubérculos
2° | Legumes
3° | Verduras
4° | Carnes

###Cuidados
***
Karin alerta que **apenas as verduras e as carnes podem ser processadas no liquidificador. Os demais alimentos devem ser amassados.** No inicio, os alimentos devem ser mais "amassadinhos" e, com o tempo, é indicado deixar uns pedacinhos maiores. Desta forma, o bebê exercita a musculatura tanto para mastigação quanto para a fala, diz.

Na hora da introdução das carnes, Karin indica o frango sem pele e a carne de boi (patinho, acém ou músculo, moídos ou cozidos). A carne, como dito anteriormente deve ser processada no liquidificador. A partir do sétimo mês, alguns pedaços desfiados podem ser introduzidos.

As leguminosas como feijão, arroz, ervilha e lentilha são os próximos alimentos a serem incorporados à alimentação do bebê. Primeiro deve ser dado só o caldo. Depois, o alimento processado, e após o oitavo mês, ele pode já conseguir mastigar uns "grãozinhos", explica.

Depois de introduzir todos estes tipos de alimentos, o bebê já vai ter um cardápio variado. Karin destaca ainda os temperos, que aguçam o paladar da criança. Ela recomenda uma pitadinha de sal, um fio de azeite, cebola e algumas ervinhas.

A nutricionista faz ressalvas quanto a alguns alimentos. Beterraba, espinafre, aipo e ovo, assim como a mandioca, Karin recomenda a introdução a partir do nono mês. Os peixes, ela recomenda entre 1 ano e meio e dois anos e os frutos do mar só a partir dos dois anos.

>"É importante fazer a introdução correta de cada alimento para evitar processos alérgicos, de intolerância e até mesmo reações adversas no corpo do bebê. No final, até os três anos, a criança já deve ter conhecido de todos os alimentos." *Karin Honorato*

[fonte](http://g1.globo.com/minas-gerais/noticia/2015/02/nutricionista-fala-sobre-introducao-dos-alimentos-nas-papinhas-dos-bebes.html)
"""

        markdown_example = \
"""# An exhibit of Markdown

This note demonstrates some of what [Markdown][1] is capable of doing.

*Note: Feel free to play with this page. Unlike regular notes, this doesn't automatically save itself.*

## Basic formatting

Paragraphs can be written like so. A paragraph is the basic block of Markdown. A paragraph is what text will turn into when there is no reason it should become anything else.

Paragraphs must be separated by a blank line. Basic formatting of *italics* and **bold** is supported. This *can be **nested** like* so.

## Lists

### Ordered list

1. Item 1
2. A second item
3. Number 3
4. Ⅳ

*Note: the fourth item uses the Unicode character for [Roman numeral four][2].*

### Unordered list

* An item
* Another item
* Yet another item
* And there's more...

## Paragraph modifiers

### Code block

    Code blocks are very useful for developers and other people who look at code or other things that are written in plain text. As you can see, it uses a fixed-width font.

You can also make `inline code` to add code into other things.

### Quote

> Here is a quote. What this is should be self explanatory. Quotes are automatically indented when they are used.

## Headings

There are six levels of headings. They correspond with the six levels of HTML headings. You've probably noticed them already in the page. Each level down uses one more hash character.

### Headings *can* also contain **formatting**

### They can even contain `inline code`

Of course, demonstrating what headings look like messes up the structure of the page.

I don't recommend using more than three or four levels of headings here, because, when you're smallest heading isn't too small, and you're largest heading isn't too big, and you want each size up to look noticeably larger and more important, there there are only so many sizes that you can use.

## URLs

URLs can be made in a handful of ways:

* A named link to [MarkItDown][3]. The easiest way to do these is to select what you want to make a link and hit `Ctrl+L`.
* Another named link to [MarkItDown](http://www.markitdown.net/)
* Sometimes you just want a URL like <http://www.markitdown.net/>.

## Horizontal rule

A horizontal rule is a line that goes across the middle of the page.

---

It's sometimes handy for breaking things up.

## Images

![Batata doce](https://abrilboaforma.files.wordpress.com/2016/10/batata-doce-emagrece.jpg?quality=85&strip=all&w=680&h=453&crop=1 "Batata doce")

___

![Bebê](/static/imgs/other/bebe_fofo.jpg "Babê")

## Finally

There's actually a lot more to Markdown than this. See the official [introduction][4] and [syntax][5] for more information. However, be aware that this is not using the official implementation, and this might work subtly differently in some of the little things.


  [1]: http://daringfireball.net/projects/markdown/
  [2]: http://www.fileformat.info/info/unicode/char/2163/index.htm
  [3]: http://www.markitdown.net/
  [4]: http://daringfireball.net/projects/markdown/basics
  [5]: http://daringfireball.net/projects/markdown/syntax
"""

        @staticmethod
        def to_activate_product_error(product):
            return 'Ocorreu uma falha ao ativar o produto #%s - "%s". Tente novamente.' % (product.id, product.title)

        @staticmethod
        def disable_product_error(product):
            return 'Ocorreu uma falha ao desativar o produto #%s - "%s". Tente novamente.' % (product.id, product.title)

        @staticmethod
        def to_activate_post_error(blog_post):
            return 'Ocorreu uma falha ao ativar o post #%s - "%s". Tente novamente.' % (blog_post.id, blog_post.title)

        @staticmethod
        def disable_post_error(blog_post):
            return 'Ocorreu uma falha ao desativar o post #%s - "%s". Tente novamente.' % (blog_post.id, blog_post.title)

        @staticmethod
        def to_activate_product_category_error(product_category):
            return 'Ocorreu uma falha ao ativar a categoria de produto #%s - "%s". Tente novamente.' % (product_category.id, product_category.name)

        @staticmethod
        def disable_product_category_error(product_category):
            return 'Ocorreu uma falha ao desativar a categoria de produto #%s - "%s". Tente novamente.' % (product_category.id, product_category.name)

        @staticmethod
        def to_activate_product_subcategory_error(product_subcategory):
            return 'Ocorreu uma falha ao ativar a subcategoria de produto #%s - "%s". Tente novamente.' % (product_subcategory.id, product_subcategory.name)

        @staticmethod
        def disable_product_subcategory_error(product_subcategory):
            return 'Ocorreu uma falha ao desativar a subcategoria de produto #%s - "%s". Tente novamente.' % (product_subcategory.id, product_subcategory.name)

        @staticmethod
        def to_activate_city_error(city):
            return 'Ocorreu uma falha ao ativar a cidade #%s - "%s". Tente novamente.' % (city.id, city.name)

        @staticmethod
        def disable_city_error(city):
            return 'Ocorreu uma falha ao desativar a cidade #%s - "%s". Tente novamente.' % (city.id, city.name)

        @staticmethod
        def stock_change_error(product):
            return 'Ocorreu uma falha ao alterar o estoque do produto #%s - "%s". Tente novamente.' % (product.id, product.title)

        @staticmethod
        def stock_change_invalid_form_error(product):
            return 'Formulário inválido. Não foi possível alterar o estoque do produto #%s - "%s". Tente novamente.' % (product.id, product.title)

        @staticmethod
        def image_sent_successfully(image_name):
            return 'A imagem "%s" foi enviada com sucesso.' % image_name

        @staticmethod
        def product_sent_successfully(product):
            return 'O produto #%s - "%s" foi adicionado com sucesso.' % (product.id, product.title)

        @staticmethod
        def city_sent_successfully(city):
            return 'A cidade #%s - "%s" foi adicionada com sucesso.' % (city.id, city.name)

        @staticmethod
        def product_category_sent_successfully(product_category):
            return 'A categoria de produto #%s - "%s" foi adicionada com sucesso.' % (product_category.id, product_category.name)

        @staticmethod
        def product_subcategory_sent_successfully(product_subcategory):
            return 'A subcategoria de produto #%s - "%s" foi adicionada com sucesso.' % (product_subcategory.id, product_subcategory.name)

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
        def product_category_successful_edited(product_category):
            return 'A categoria de produto #%s - "%s" foi editada com sucesso.' % (product_category.id, product_category.name)

        @staticmethod
        def product_successful_edited(product):
            return 'O produto #%s - "%s" foi editado com sucesso.' % (product.id, product.title)

        @staticmethod
        def post_successful_edited(blog_post):
            return 'O post #%s - "%s" foi editado com sucesso.' % (blog_post.id, blog_post.title)

        @staticmethod
        def city_successful_edited(city):
            return 'A cidade #%s - "%s" foi editada com sucesso.' % (city.id, city.name)

        @staticmethod
        def product_subcategory_successful_edited(product_subcategory):
            return 'A subcategoria de produto #%s - "%s" foi editada com sucesso.' % (product_subcategory.id, product_subcategory.name)

        @staticmethod
        def n_image(n):
            return "%sº Imagem" % str(n)

        @staticmethod
        def n_tab_title(n):
            return "Título da %sº aba" % str(n)

        @staticmethod
        def n_tab_content(n):
            return "Conteúdo da %sº aba" % str(n)

        @staticmethod
        def order_details_modal_title(order_id):
            return "Detalhes do pedido #"+ str(order_id)

        @staticmethod
        def price_with_rs(price):
            return "R$ " + str(price).replace(".", ",")

        @staticmethod
        def client_details_modal_title(client_first_name):
            if client_first_name:
                return "Detalhes do cliente " + str(client_first_name)
            else:
                return "Detalhes do cliente"

        @staticmethod
        def get_product_n(n):
            return "Produto " + str(n)

        @staticmethod
        def get_post_n(n):
            return "Post " + str(n)

        @staticmethod
        def get_carousel_n(n):
            return "Carrossel " + str(n)

        @staticmethod
        def get_product_section_n(n):
            return "Seção de produto " + str(n)

        @staticmethod
        def get_blog_section_n(n):
            return "Seção de blog " + str(n)

        @staticmethod
        def get_save_carousel_error_msg(carousel_number):
            return "Não foi possível salvar os novos dados do carrossel %s. Verifique os valores e tente novamente." % carousel_number

        @staticmethod
        def get_save_carousel_success_msg(carousel_number):
            return "Os dados do carrossel %s foram atualizados com sucesso." % carousel_number

        @staticmethod
        def get_save_product_section_error_msg(product_section_number):
            return "Não foi possível salvar os novos dados da seção de produtos %s. Verifique os valores e tente novamente." % product_section_number

        @staticmethod
        def get_save_product_section_success_msg(product_section_number):
            return "Os dados da seção de produto %s foram atualizados com sucesso." % product_section_number

        @staticmethod
        def get_save_blog_section_error_msg(blog_section_number):
            return "Não foi possível salvar os novos dados da seção de blog %s. Verifique os valores e tente novamente." % blog_section_number

        @staticmethod
        def get_save_blog_section_success_msg(blog_section_number):
            return "Os dados da seção de blog %s foram atualizados com sucesso." % blog_section_number

        @staticmethod
        def blog_post_sent_successfully(blog_post):
            return 'O post #%s - "%s" foi adicionado com sucesso.' % (blog_post.id, blog_post.title)

        @staticmethod
        def post_not_editable(blog_post):
            return 'O post #%s - "%s" não pode ser editado.' % (blog_post.id, blog_post.title)

        @staticmethod
        def product_category_not_editable(product_category):
            return 'A categoria de produto #%s - "%s" não pode ser editada.' % (product_category.id, product_category.name)

        @staticmethod
        def product_not_editable(product_title):
            return 'O produto "%s" não pode ser editado.' % product_title

        @staticmethod
        def get_product_summary_example():
            return R.string.product_example_summary

        @staticmethod
        def get_product_tab_content_example():
            return \
                "###" + R.string.product_example_tab_1_title + "\n" + \
                "***" + "\n" + \
                R.string.product_example_tab_1_content + "\n\n" \
                "###" + R.string.product_example_tab_2_title + "\n" + \
                "***" + "\n" + \
                R.string.product_example_tab_2_content + "\n\n" \
                "###" + R.string.product_example_tab_3_title + "\n" + \
                "***" + "\n" + \
                R.string.product_example_tab_3_content + "\n\n" \
                "###" + R.string.product_example_tab_4_title + "\n" + \
                "***" + "\n" + \
                R.string.product_example_tab_4_content + "\n\n" \
                "###" + R.string.product_example_tab_5_title + "\n" + \
                "***" + "\n" + \
                R.string.product_example_tab_5_content + "\n"

        @staticmethod
        def tab_n(n):
            return "Tab %s" % str(n)

        @staticmethod
        def get_tab_n_active(n):
            return "%sº aba ativa" % n

        @staticmethod
        def get_admin_home_new_orders_message(new_orders_href, n_new_orders):
            return "Há <a href='%s'>%s novos pedidos</a> a serem enviados." % (new_orders_href, n_new_orders)

        @staticmethod
        def product_stock_insufficient_to_send_order(limiting_product):
            return 'O estoque do produto #%s - "%s" é insuficiente para o pedido em questão. Por favor, atualize o estoque deste produto.' % (limiting_product.id, limiting_product.title)

        @staticmethod
        def prohibited_image_name(image_name):
            return 'O nome de imagem "%s" não é permitido. Por favor, troque o nome da imagem.' % image_name

        @staticmethod
        def cart_popup_title(n_items, products_total_price_as_string):
            if n_items == 0:
                return "Carrinho vazio"
            elif n_items == 1:
                return str(n_items) + " item | " + str(products_total_price_as_string)
            else:
                return str(n_items) + " items | " + str(products_total_price_as_string)

        @staticmethod
        def get_product_amount_subtotal(amount, unit_price):
            return str(amount) + " x " + str(unit_price)

        @staticmethod
        def get_products_by_category_title(category_name):
            return "Categoria " + category_name

        @staticmethod
        def get_products_by_subcategory_title(subcategory_name):
            return "Subcategoria " + subcategory_name

        @staticmethod
        def get_products_by_search_title(search_title):
            return "Busca: " + search_title

        @staticmethod
        def get_password_length_message():
            return "A senha deve possuir entre %s e %s caracteres." % (R.dimen.password_min_length, R.dimen.password_max_length)

        @staticmethod
        def account_successful_created(email):
            return "<b>Conta criada com sucesso!</b> Para entrar é necessário confirmar o email <b>%s</b> clicando no link da mensagem que acabamos de enviar." % email

        @staticmethod
        def email_successful_confirmed(email):
            return "O email <b>%s</b> foi confirmado com sucesso!" % email

        @staticmethod
        def email_or_password_invalid():
            return "Email ou senha incorretos. Caso tenha esquecido sua senha clique <a href='%s'>aqui</a>." % str(url_for("client_user_management.want_redefine_password"))

        @staticmethod
        def email_not_confirmed(email):
            return "O email <b>%s</b> ainda não foi confirmado. Para reenviar o email de confirmação, clique <a href='%s'>aqui</a>." % (email, url_for("client_user_management.resend_confirmation_email"))

        @staticmethod
        def email_not_found(email):
            return "O email <b>%s</b> não foi encontrado em nosso banco de dados. Tente novamente." % email

        @staticmethod
        def successful_send_redefine_password_email(email):
            return "O email de redefinição de senha foi enviado com sucesso para <b>%s</b>." % email

        @staticmethod
        def account_never_created(email):
            return "A conta com o email <b>%s</b> nunca foi criada, para criá-la clique <a href='%s'>aqui</a>." % (email, url_for("client_user_management.register", **{R.string.email_arg_name: email}))

        @staticmethod
        def successful_resend_of_confirmation_email(email):
            return "O email de confirmação foi reenviado com sucesso para <b>%s</b>." % email

        @staticmethod
        def decimal_price_as_string(price_as_decimal, include_rs=False):
            s = ""
            if include_rs:
                s += "R$ "
            s += str(price_as_decimal).replace('.', ',')
            return s

        @staticmethod
        def add_to_cart_error_msg_amount_exceeded_stock(product, amount):
            return 'Não foi possível adicionar %s unidade(s) do produto "%s" ao seu carrinho. Há apenas %s unidades disponíveis no estoque.' % (str(amount), product.title, str(product.available))

        @staticmethod
        def main_image_of_product(product_title):
            return 'Imagem principal do produto "%s"' % product_title

        @staticmethod
        def product_removed_from_cart(product_title):
            return 'O produto "%s" foi removido do carrinho.' % product_title

        @staticmethod
        def product_added_to_cart_without_stock_overflow(amount, product_title):
            if amount == 1:
                return '%s unidade do produto "%s" foi adicionada ao seu carrinho.' % (str(amount), product_title)
            else:
                return '%s unidades do produto "%s" foram adicionadas ao seu carrinho.' % (str(amount), product_title)

        @staticmethod
        def product_added_to_cart_with_stock_overflow(amount, product_title):
            if amount == 1:
                return 'Limite do estoque atingido! %s unidade do produto "%s" foi adicionada ao seu carrinho.' % (str(amount), product_title)
            else:
                return 'Limite do estoque atingido! %s unidades do produto "%s" foram adicionadas ao seu carrinho.' % (str(amount), product_title)

        @staticmethod
        def amount_of_product_changed(product_title):
            return 'Devido a alterações recentes no estoque, a quantidade do produto "%s" foi alterada no seu carrinho.' % product_title

        @staticmethod
        def product_removed_due_stock_changes(product_title):
            return 'Devido a alterações recentes no estoque, o produto "%s" não está mais disponível e foi removido do seu carrinho.' % product_title

        @staticmethod
        def welcome_message(first_name):
            if first_name is None:
                return "Seja bem vindo!"
            else:
                return "Seja bem vindo, %s!" % first_name

        @staticmethod
        def search_for(q):
            return 'Busca por "%s"' % q

        @staticmethod
        def email_not_registered_with_facebook(email):
            return "O email <b>%s</b> não foi cadastrado utilizando o Facebook. Utilize o email e a senha cadastrados." % email

        @staticmethod
        def user_registered_with_facebook(email):
            return "O email <b>%s</b> foi cadastrado utilizando o Facebook. Entre utilizando o Facebook." % email

        @staticmethod
        def discount_format(discount_percentage):
            return "-%s%%" % discount_percentage

        @staticmethod
        def category_n(n):
            return "Categoria %s" % n

        @staticmethod
        def subcategory_n_of_category_m(n, m):
            return "Subcategoria %s da categoria %s" % (n, m)

        @staticmethod
        def image_of_category_n(n):
            return "Imagem da categoria %s" % n

        @staticmethod
        def image_of_tag_n(n):
            return "Imagem da tag %s" % n

        @staticmethod
        def title_of_tag_n(n):
            return "Título da tag %s" % n

        @staticmethod
        def subtitle_of_tag_n(n):
            return "Subtítulo da tag %s" % n

        @staticmethod
        def product_image_prefix(product_id):
            return "produto_" + str(product_id) + "_"

        @staticmethod
        def format_price(price, include_rs=True):
            s = ""
            if include_rs:
                s += "R$ "
            s += str(price).replace('.', ',')
            return s

        @staticmethod
        def default_date_format(datetime):
            return datetime.strftime("%d/%m/%Y")

        @staticmethod
        def default_datetime_format(datetime):
            return datetime.strftime("%d/%m/%Y\n%H:%M")

        @staticmethod
        def get_additional_categories(n):
            return "Categoria " + str(n) + " da seção 'Mais para você'"

        @staticmethod
        def tag_n_header(n):
            return "Tag " + str(n)

        @staticmethod
        def order_status_successfully_changed_message(order_id, new_status):
            return "O pedido '#%s' alterou com sucesso seu status para '%s'" % (
                str(order_id),
                R.string.get_order_status_as_string(new_status)
            )

        @staticmethod
        def get_order_status_as_string(order_status):
            if order_status == R.id.ORDER_STATUS_ANY:
                return R.string.any
            if order_status == R.id.ORDER_STATUS_CANCELED:
                return R.string.canceled
            elif order_status == R.id.ORDER_STATUS_PAID:
                return R.string.paid
            elif order_status == R.id.ORDER_STATUS_SENT:
                return R.string.sent
            elif order_status == R.id.ORDER_STATUS_DELIVERED:
                return R.string.delivered
            else:
                return order_status

        @staticmethod
        def month_as_string(month):
            if month==1:
                return "Janeiro"
            elif month==2:
                return "Fevereiro"
            elif month==3:
                return "Março"
            elif month==4:
                return "Abril"
            elif month==5:
                return "Maio"
            elif month==6:
                return "Junho"
            elif month==7:
                return "Julho"
            elif month==8:
                return "Agosto"
            elif month==9:
                return "Setembro"
            elif month==10:
                return "Outubro"
            elif month==11:
                return "Novembro"
            elif month==12:
                return "Dezembro"
            else:
                return "-"

    # noinspection PyPep8Naming
    @unique
    class id(Enum):
        DEFAULT =                               0

        # Admin navbar
        ADMIN_NAVBAR_HOME =                     1
        ADMIN_NAVBAR_PRODUCTS =                 2
        ADMIN_NAVBAR_ORDERS =                   3
        ADMIN_NAVBAR_BLOG =                     4
        ADMIN_NAVBAR_CLIENTS =                  5
        ADMIN_NAVBAR_IMAGES =                   6
        ADMIN_NAVBAR_CONTENT =                  7
        ADMIN_NAVBAR_ATTENDED_CITIES =          8

        # Super table column types
        COL_TYPE_IMAGE =                        101
        COL_TYPE_TEXT =                         102
        COL_TYPE_ACTION =                       103
        COL_TYPE_BOOL =                         104
        COL_TYPE_MIN_UUID =                     105

        # Super table action element types
        ACTION_TYPE_BUTTON =                    201
        ACTION_TYPE_LINK_BUTTON =               202
        ACTION_TYPE_INT_WITH_BUTTON =           203
        ACTION_TYPE_ACTIVATE_DISABLE_BUTTON =   204

        # Sort methods
        SORT_METHOD_TITLE =                     301
        SORT_METHOD_LOWEST_PRICE =              302
        SORT_METHOD_HIGHER_PRICE =              303
        SORT_METHOD_LOWEST_STOCK =              304
        SORT_METHOD_HIGHER_STOCK =              305
        SORT_METHOD_BEST_SELLER =               306
        SORT_METHOD_LESS_SOLD =                 307
        SORT_METHOD_CLIENT_EMAIL =              308
        SORT_METHOD_LOWER_TOTAL_PRICE =         309
        SORT_METHOD_HIGHER_TOTAL_PRICE =        310
        SORT_METHOD_NEWEST =                    311
        SORT_METHOD_OLDER =                     312
        SORT_METHOD_CLIENT_NAME =               313
        SORT_METHOD_ID =                        314
        SORT_METHOD_NAME =                      315
        SORT_METHOD_LOWEST_RESERVED =           316
        SORT_METHOD_HIGHER_RESERVED =           317
        SORT_METHOD_LOWEST_AVAILABLE =          318
        SORT_METHOD_HIGHER_AVAILABLE =          319
        SORT_METHOD_PRIORITY =                  320

        # Order status
        ORDER_STATUS_ANY =                      400
        ORDER_STATUS_PAID =                     401
        ORDER_STATUS_SENT =                     402
        ORDER_STATUS_DELIVERED =                403
        ORDER_STATUS_CANCELED =                 404

        ADD_TO_CART_EXCEEDED_STOCK =            500
        ADD_TO_CART_NOT_EXCEEDED_STOCK =        501


    # noinspection PyPep8Naming
    class dimen(object):
        example = 42
        min_page = 1

        product_category_name_max_length = 48
        product_subcategory_name_max_length = 48
        tab_title_max_length = 48
        product_title_max_length = 96
        email_max_length = 256
        password_min_length = 6
        password_max_length = 32
        first_name_max_length = 64
        last_name_max_length = 64
        address_max_length = 256
        address_complement_max_length = 32
        address_number_max_length = 9
        cep_max_length = 9
        tel_max_length = 15
        state_name_max_length = 2
        city_name_max_length = 48
        datetime_important_chars_size = 16
        carousel_title_max_length = 64
        carousel_subtitle_max_length = 128
        product_section_name_max_length = 32
        blog_post_title_max_length = 128
        blog_section_name_max_length = 32
        contact_address_max_length = 96
        footer_lower_text_max_length = 96

        freight = Decimal("5.00")

        product_example_price = Decimal("9.90")
        product_example_stock = 100
        product_example_min_available = 10
        product_example_sales_number = 32
        uuid_length = 36

        test_stock = 42
        test_min_available = 12
        super_table_text_max_length = 32
        # TODO: Change timeout in production
        cache_timeout = 1
        link_max_length = 1024
        item_inner_max_length = 38
        day_in_seconds = 24*60*60
        max_value_of_int_field = 999999999
        min_value_of_int_field = -999999999

        product_search_limit = 12
        blog_post_search_limit = 4

        csrf_length = 32
        blog_post_n_comments = 5

        default_n_visible_categories = 4

        default_product_category_priority = 10

        tag_title_max_length = 32
        tag_subtitle_max_length = 128

        blog_post_preview_title_max_length = 48
        image_name_max_size = 64
        filename_max_size = 128

        n_max_images_per_product = 4

        product_image_width = 400
        product_image_height = 400

        blog_tag_max_length = 128
        id_with_hashtag_max_size = 32
        n_blog_posts_per_page = 4


R = Resources()
