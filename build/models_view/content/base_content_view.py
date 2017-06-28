from models_view.proj_base_view import ProjBaseView
from r import R


class BaseContentView(ProjBaseView):
    category = R.string.content

    can_delete = False
    can_create = False
