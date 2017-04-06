# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 24/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
import os

from flask import render_template, request, flash, current_app, redirect, url_for
from flask_login import login_required
from werkzeug.utils import secure_filename
from proj_decorators import valid_form, admin_required
from flask_bombril import R as bombril_R
from proj_forms import SubmitForm
from proj_utils import create_product_image
from r import R
from routers.admin_images import admin_images_blueprint
from routers.admin_images.data_providers import admin_images_data_provider, admin_add_image_data_provider
from routers.admin_images.forms import UploadImageForm


@admin_images_blueprint.route("/")
@login_required
@admin_required
def images():
    return render_template("admin_images/images.html", data=admin_images_data_provider.get_data())


@admin_images_blueprint.route("/remover-imagem/<string:image_name>", methods=["POST"])
@login_required
@admin_required
@valid_form(FormClass=SubmitForm)
def remove_image(image_name, form):
    if (image_name in admin_images_data_provider.fixed_images) or (
        image_name in admin_images_data_provider.irremovable_images):
        return "", 403

    file_path = os.path.join(current_app.config['UPLOADED_IMAGES_FOLDER_FULL_PATH'], image_name)

    if os.path.exists(file_path):
        os.remove(file_path)

    file_path = os.path.join(current_app.config['PRODUCTS_IMAGES_FOLDER_FULL_PATH'], image_name)

    if os.path.exists(file_path):
        os.remove(file_path)

    return "", 204


@admin_images_blueprint.route("/adicionar-imagem", methods=["GET", "POST"])
@login_required
@admin_required
def add_image():
    if request.method == "GET":
        return render_template("admin_images/add_image.html", data=admin_add_image_data_provider.get_data())
    else:
        upload_image_form = UploadImageForm()
        if upload_image_form.validate_on_submit():
            image = request.files[upload_image_form.image.name]
            filename = secure_filename(image.filename)
            image.save(os.path.join(current_app.config['UPLOADED_IMAGES_FOLDER_FULL_PATH'], filename))
            create_product_image(os.path.join(current_app.config['UPLOADED_IMAGES_FOLDER_FULL_PATH'], filename),
                                 filename)
            flash(R.string.image_sent_successfully(filename),
                  bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.success))
            flash(R.string.image_sent_successfully(filename),
                  bombril_R.string.get_message_category(bombril_R.string.static, bombril_R.string.success))
            return redirect(url_for("admin_images.add_image"))
        else:
            flash(R.string.add_image_error,
                  bombril_R.string.get_message_category(bombril_R.string.toast, bombril_R.string.error))
            return render_template("admin_images/add_image.html",
                                   data=admin_add_image_data_provider.get_data(upload_image_form=upload_image_form))
