from flask_bombril.utils.utils import merge_dicts
from models_view.proj_base_view import ProjBaseView
from r import R


class CityView(ProjBaseView):
    can_delete = False
    column_labels = merge_dicts(ProjBaseView.column_labels, dict(active=R.string.active_in_female, name=R.string.name))
    column_list = ['active', 'name', 'state']
    column_filters = ['active', 'state']
    column_editable_list = ['name', 'state', 'active']

    def __init__(self, *args, **kwargs):
        kwargs["name"] = R.string.attended_cities
        kwargs["endpoint"] = R.string.cities.lower()
        super(CityView, self).__init__(*args, **kwargs)