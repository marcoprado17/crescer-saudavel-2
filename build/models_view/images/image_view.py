from flask_admin import form
from markupsafe import Markup
from flask_bombril.form_validators.required.required import Required
from flask_bombril.form_validators.unique import Unique
from models_view.proj_base_view import ProjBaseView
from r import R
from configs import default_app_config as config
from os.path import join


class ImageView(ProjBaseView):
    can_edit = False

    column_formatters = dict(
        image=lambda view, context, model, name:
        Markup("<img style='max-width: 100px;max-height: 100px;' src='%s'>" % model.get_src()),
        link=lambda view, context, model, name:
        model.get_src()
    )
    column_list = ["filename", "link", "image"]

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
