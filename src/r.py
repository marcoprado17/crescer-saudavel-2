# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from decimal import Decimal

from enum import Enum, unique

from flask_bombril.utils import stringfy_list


class Resources(object):
    # noinspection PyPep8Naming
    class string(object):
        footer_lower_text = "Crescer saudável - CNPJ 01.517.384/0001-87 -  © 2016 - 2017 "
        lower_text = "Texto inferior"
        edit_footer = "Editar rodapé"
        thumbnail = "Thumbnail"
        thumbnail_tooltip = "Imagem principal do post em questão"
        tabs = "Abas"

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
        blog = "Blog"
        add_new_post = "Adicionar novo post"
        posts_table = "Tabela de posts"
        customers = "Clientes"
        images = "Imagens"
        add_new_image = "Adicionar nova imagem"
        images_table = "Tabela de imagens"
        content = "Conteúdo"
        contact = "Contato"
        about_us = "Sobre nós"
        faq = "FAQ"
        attended_cities = "Cidades atendidas"
        add_new_city = "Adicionar nova cidade"
        cities_table = "Tabela de cidades"

        # Admin image
        no_file_selected = "Nenhum arquivo foi selecionado."
        image = "Imagem"
        upload = "Enviar"
        add_image = "Adicionar nova imagem"
        allowed_image_extensions = ["png", "jpg", "jpeg"]
        image_sent_failure = "Ocorreu um erro no envio da imagem %(image_name)s."

        find_image = "Procurar imagem"
        upload_image_auxiliar_text = "Os formatos de imagem aceitos são: " + stringfy_list(allowed_image_extensions)

        images_table_id = "images-table"
        products_table_id = "products-table"
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
        subcategory_id_arg_name = "subcategory_id"
        order_status_id_arg_name = "status"
        state_id_arg_name = "state_id"
        city_id_arg_name = "city_id"
        active_arg_name = "active"

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
        product_title_example = "Ex.: Papinha de maça - 500g"
        product_price_example = "Ex.: 8,80"
        product_stock_quantity_example = "Ex.: 42"
        product_stop_sell_stock_quantity_example = "Ex.: 5"
        markdown = "Markdown"
        example = "Exemplo"
        preview = "Pré-visualização"
        markdown_href = "https://dwoond.github.io/O-basico-de-Markdown/"
        close = "Fechar"
        loading = "Carregando..."
        markdown_preview_error = "Ocorreu uma falha na tradução do texto Markdown. Tente novamente."
        tab_title_example = "Ex.: Informação nutricional"
        active = "Ativo"
        product_category_col_id = "product-category-col"
        product_price_col_id = "product-price-col"
        price_in_real = "Preço em R$"
        product_stock_col_id = "product-stock-col"
        in_stock = "Em estoque"
        product_min_stock_col_id = "product-min-stock-col"
        min_stock = "Mín. Estoque"
        min_stock_tooltip = "Quando o estoque do produto atingir o valor estabelecido em mín. estoque, o produto não será mais disponibilizado para venda na loja virtual."
        product_sales_number_col_id = "product-sales-number-col"
        sales = "Vendas"
        empty_subcategory_symbol = "Nenhuma"
        sort_method_label = "Ordenar por:"

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
        quantity = "Quantia"
        subtotal_tooltip = "Valor do produto multiplicado por sua quantia (em R$)"
        product_price_tooltip = "Valor do produto em R$"
        order_total_value = "Valor total do pedido"
        register_date = "Data de cadastro"
        clients = "Clientes"
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
        tel_tooltip = "Formatos de telefone aceitos: (XX) XXXX-XXXX ou (XX) XXXXX-XXXX."
        facebook = "Facebook"
        twitter = "Twitter"
        google_plus = "Google+"
        pintrest = "Pintrest"
        youtube = "Youtube"
        save_contact_error_msg = "Não foi possível salvar os novos dados de contato. Verifique os valores e tente novamente."
        save_contact_success_msg = "Os dados de contato foram atualizados com sucesso."
        save_about_us_error_msg = 'Não foi possível salvar os novos dados da página "Sobre nós". Verifique os valores e tente novamente.'
        save_about_us_success_msg = 'Os dados da página "Sobre nós" foram atualizados com sucesso.'
        save_faq_error_msg = 'Não foi possível salvar os novos dados da página "FAQ". Verifique os valores e tente novamente.'
        save_faq_success_msg = 'Os dados da página "FAQ" foram atualizados com sucesso.'
        save_footer_error_msg = 'Não foi possível salvar os novos dados do rodapé. Verifique os valores e tente novamente.'
        save_footer_success_msg = 'Os dados do rodapé foram atualizados com sucesso.'
        edit_about_us_page_content = 'Editar conteúdo da página "Sobre nós"'
        edit_faq_page_content = 'Editar conteúdo da página "FAQ"'
        footer = "Rodapé"
        date = "Data"
        default_datetime_format = "%d/%m/%Y"
        posts = "Posts"
        edit_post = "Editar post"
        product_category_example = "Ex.: Frutas"
        product_subcategory_example = "Ex.: Frutas vermelhas"
        product_category = "Categoria de produto"
        address_example = "R. Vinte e Sete de Julho, 231 - São José dos Campos - SP"
        tel_example = "(11) 2352-2458"
        email_example = "contato@crescersaudavel.com"
        blog_post_title_example = "Ex.: Nutricionista fala sobre introdução dos alimentos nas papinhas dos bebês"


        blog_example_title = "Nutricionista fala sobre introdução dos alimentos nas papinhas dos bebês"
        blog_example_thumbnail = "post_exemplo_bebe_comendo.jpg"
        product_category_example_name = "Frutas"
        carousel_title_example = "Ex.: Conheça nossa loja física"
        carousel_subtitle_example = "Ex.: Localização: " + address_example
        product_section_name_example = "Ex.: Novidades"
        blog_section_name_example = "Ex.: Posts mais recentes"
        address_placeholder = "Ex.: " + address_example
        tel_placeholder = "Ex.: " + tel_example
        email_placeholder = "Ex.: " + email_example
        link_placeholder = "Ex.: https://www.google.com.br"
        footer_lower_text_placeholder = "Ex.: " + footer_lower_text
        city_placeholder = "Ex.: São José dos Campos"
        category_name = "Nome da categoria"
        subcategory_name = "Nome da subcategoria"
        cancel_order = "Cancelar pedido"
        mark_as_paid = "Marcar como pago"

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
Carboidrato        | 87g
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
""" Conservar este produto congelado até o seu uso. Após Aberto e descongelado, consumir em até 12 horas.
Nenhum produto após o descongelamento poderá ser recongelado."""


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
Unicode is supported.



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

![Abóbora](/static/imgs/post_exemplo_abobora.jpg "Abóbora")

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
Karin alerta que **apenas as verduras e as carnes podem ser processadas no liquidificador. Os demais alimentos devem ser amassados.** No inicio, os alimentos devem ser mais “amassadinhos” e, com o tempo, é indicado deixar uns pedacinhos maiores. Desta forma, o bebê exercita a musculatura tanto para mastigação quanto para a fala, diz.

Na hora da introdução das carnes, Karin indica o frango sem pele e a carne de boi (patinho, acém ou músculo, moídos ou cozidos). A carne, como dito anteriormente deve ser processada no liquidificador. A partir do sétimo mês, alguns pedaços desfiados podem ser introduzidos.

As leguminosas como feijão, arroz, ervilha e lentilha são os próximos alimentos a serem incorporados à alimentação do bebê. Primeiro deve ser dado só o caldo. Depois, o alimento processado, e após o oitavo mês, ele pode já conseguir mastigar uns “grãozinhos”, explica.

Depois de introduzir todos estes tipos de alimentos, o bebê já vai ter um cardápio variado. Karin destaca ainda os temperos, que aguçam o paladar da criança. Ela recomenda uma pitadinha de sal, um fio de azeite, cebola e algumas ervinhas.

A nutricionista faz ressalvas quanto a alguns alimentos. Beterraba, espinafre, aipo e ovo, assim como a mandioca, Karin recomenda a introdução a partir do nono mês. Os peixes, ela recomenda entre 1 ano e meio e dois anos e os frutos do mar só a partir dos dois anos.

>"É importante fazer a introdução correta de cada alimento para evitar processos alérgicos, de intolerância e até mesmo reações adversas no corpo do bebê. No final, até os três anos, a criança já deve ter conhecido de todos os alimentos." *Karin Honorato*

[fonte](http://g1.globo.com/minas-gerais/noticia/2015/02/nutricionista-fala-sobre-introducao-dos-alimentos-nas-papinhas-dos-bebes.html)
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
            return 'Ocorreu uma falha alterar o estoque do produto #%s - "%s". Tente novamente.' % (product.id, product.title)

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
        def formatted_datetime(datetime):
            if datetime == None:
                return ""
            return str(datetime)[0:R.dimen.datetime_important_chars_size]

        @staticmethod
        def client_details_modal_title(client_first_name):
            if client_first_name:
                return "Detalhes do cliente " + str(client_first_name)
            else:
                return "Detalhes do cliente"

        @staticmethod
        def order_panel_title(order_id):
            return "Pedido #" + str(order_id)

        @staticmethod
        def get_formatted_date(paid_datetime):
            return str(paid_datetime)[0:10]

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
        def get_tab_n_active(n):
            return "%sº aba ativa" % n

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

        # Order status
        ORDER_STATUS_ANY =                      400
        ORDER_STATUS_PAID =                     401
        ORDER_STATUS_SENT =                     402
        ORDER_STATUS_DELIVERED =                403
        ORDER_STATUS_CANCELED =                 404


    # noinspection PyPep8Naming
    class dimen(object):
        example = 42
        min_page = 1

        product_category_name_max_length = 48
        product_subcategory_name_max_length = 48
        tab_title_max_length = 48
        product_title_max_length = 96
        email_max_length = 256
        password_max_length = 32
        first_name_max_length = 256
        last_name_max_length = 256
        address_max_length = 256
        address_complement_max_length = 32
        cep_max_length = 9
        tel_max_length = 15
        state_name_max_length = 32
        city_name_max_length = 32
        datetime_important_chars_size = 16
        carousel_title_max_length = 64
        carousel_subtitle_max_length = 128
        product_section_name_max_length = 32
        blog_post_title_max_length = 128
        blog_section_name_max_length = 32
        contact_address_max_length = 96
        footer_lower_text_max_length = 256

        freight = Decimal("5.00")

        product_example_price = Decimal("9.90")
        product_example_stock = 100
        product_example_min_stock = 10
        product_example_sales_number = 32


R = Resources()
