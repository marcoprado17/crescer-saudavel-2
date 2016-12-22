# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from routers.debug import debug_blueprint


@debug_blueprint.route("/test")
def test():
    return "Hello World!"
