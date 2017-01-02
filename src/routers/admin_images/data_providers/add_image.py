# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 26/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.admin_images.forms import UploadImageForm


class AdminAddImageDataProvider(object):
    def get_data(self, form=None):
        if not form:
            form = UploadImageForm()

        return dict(
            form=form
        )

admin_add_image_data_provider = AdminAddImageDataProvider()