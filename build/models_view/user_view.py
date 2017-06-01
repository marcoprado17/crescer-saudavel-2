from models_view.proj_base_view import ProjBaseView
from r import R


class UserView(ProjBaseView):
    name = R.string.clients
    endpoint = R.string.clients_endpoint

    can_create = False
    can_delete = False
    can_edit = False
    can_view_details = True

    column_details_exclude_list = ["_cart_amount_by_product_id", "_password", "authenticated"]
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
        R.string.default_datetime_format(model.register_datetime)
    )
    column_list = ["id", "email", "first_name", "last_name", "state", "city"]
    column_searchable_list = ["email", "first_name", "last_name"]
    column_sortable_list = ["id", "email", "first_name", "last_name"]
