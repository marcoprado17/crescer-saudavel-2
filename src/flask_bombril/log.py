# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
import traceback

from flask import request, current_app


def log_request(log_func):
    log_func("url: " + request.url)
    if request.method == "POST" and len(request.form) > 0:
        form_fields = dict(request.form)
        if "password" in form_fields:
            form_fields["password"] = "******"
        if "password_confirmation" in form_fields:
            form_fields["password_confirmation"] = "******"
        log_func("form_fields: " + str(form_fields))


def log_handled_exception(handled_exception):
    app = current_app._get_current_object()
    app.logger.warning(handled_exception)
    app.logger.warning(traceback.format_exc())
    log_request(app.logger.warning)
