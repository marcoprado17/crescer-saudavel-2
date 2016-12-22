# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import render_template

from routers.debug import debug_blueprint


@debug_blueprint.route("/test")
def test():
    return render_template("debug/test.html")
