from flask import url_for
from markupsafe import Markup

from models_view.proj_base_view import ProjBaseView
from r import R


class UserView(ProjBaseView):
    def _orders_formatter(view, context, model, name):
        table_rows = []
        if model.orders is not None and len(model.orders) > 0:
            for order in model.orders:
                order_id = order.id
                order_products_total_price = order.products_total_price
                order_paid_datetime = order.paid_datetime
                table_rows.append("<tr>")
                table_rows.append("<td><a href='%s'><b>#%s</b></a></td>" % (
                    url_for(R.string.orders_endpoint + ".details_view", id=order_id),
                    order_id))
                table_rows.append("<td>%s</td>" % R.string.format_price(order_products_total_price))
                table_rows.append("<td>%s</td>" % R.string.default_date_format(order_paid_datetime))
                table_rows.append("</tr>")
            html = [
                "<table class='table'>",
                "   <tr>",
                "       <th style='border-top: 0;'>%s</th>" % R.string.id,
                "       <th style='border-top: 0;'>%s</th>" % R.string.product_total_price,
                "       <th style='border-top: 0;'>%s</th>" % R.string.date,
                "   </tr>"
            ]
            for table_row in table_rows:
                html.append(table_row)
            html.append("</table>")
            return Markup(''.join(html))
        else:
            return R.string.empty_symbol

    name = R.string.clients
    endpoint = R.string.clients_endpoint

    can_create = False
    can_delete = False
    can_edit = False
    can_view_details = True

    column_details_exclude_list = ["_cart_amount_by_product_id", "_password", "authenticated"]
    column_details_list = [
        "id",
        "email",
        "email_confirmed",
        "facebook_login",
        "register_datetime",
        "first_name",
        "last_name",
        "state",
        "city",
        "address",
        "address_number",
        "address_complement",
        "cep",
        "tel",
        "orders"
    ]
    column_filters = ["state", "city"]
    column_formatters = dict(
        first_name=lambda view, context, model, name:
        model.first_name if model.first_name is not None else R.string.empty_symbol,
        last_name=lambda view, context, model, name:
        model.last_name if model.last_name is not None else R.string.empty_symbol,
        state=lambda view, context, model, name:
        model.state if model.state is not None else R.string.empty_symbol,
        city=lambda view, context, model, name:
        model.city if model.city is not None else R.string.empty_symbol,
        address=lambda view, context, model, name:
        model.address if model.address is not None else R.string.empty_symbol,
        address_number=lambda view, context, model, name:
        model.address_number if model.address_number is not None else R.string.empty_symbol,
        address_complement=lambda view, context, model, name:
        model.address_complement if model.address_complement is not None else R.string.empty_symbol,
        cep=lambda view, context, model, name:
        model.cep if model.cep is not None else R.string.empty_symbol,
        tel=lambda view, context, model, name:
        model.tel if model.tel is not None else R.string.empty_symbol,
        register_datetime=lambda view, context, model, name:
        R.string.default_datetime_format(model.register_datetime),
        orders=_orders_formatter
    )
    column_list = ["id", "email", "first_name", "last_name", "state", "city"]
    column_searchable_list = ["email", "first_name", "last_name"]
    column_sortable_list = ["id", "email", "first_name", "last_name"]
