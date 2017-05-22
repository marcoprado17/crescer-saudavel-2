import os

from flask_admin import form
from flask_admin.form import rules
from markupsafe import Markup
from flask_bombril.form_validators.required.required import Required
from flask_bombril.form_validators.unique import Unique
from flask_bombril.utils.utils import merge_dicts
from models_view.proj_base_view import ProjBaseView
from r import R
from configs import default_app_config as config
from os.path import join


class ImageView(ProjBaseView):
    def _image_formatter(view, context, model, name):
        return Markup("<img style='max-width: 100px;max-height: 100px;' src='%s'>" % model.get_src())

    def _link_formatter(view, context, model, name):
        return model.get_src()

    can_edit = False

    column_labels = merge_dicts(ProjBaseView.column_labels)
    column_list = ["filename", "link", "image"]
    column_formatters = dict(
        image=_image_formatter,
        link=_link_formatter
    )

    @staticmethod
    def build_form_extra_fields(folder_full_path, folder_name, model, field):
        return dict(
            filename=form.ImageUploadField(R.string.image,
                                           validators=[
                                               Required(),
                                               Unique(
                                                   model=model,
                                                   field=field,
                                                   message=R.string.filename_already_exist,
                                                   data_key="filename")],
                                           base_path=folder_full_path,
                                           url_relative_path=join(config.IMAGES_FOLDER, folder_name, folder_name))
        )

    def after_model_delete(self, model):
        model.delete_file()
