from models_view.proj_base_view import ProjBaseView
from r import R


class CityView(ProjBaseView):
    name = R.string.attended_cities
    endpoint = R.string.cities_endpoint

    can_delete = False

    column_list = ['active', 'state', 'name']
    column_filters = ['active', 'state']
    column_editable_list = ['name', 'state', 'active']
