# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================

from app_contexts.app import app

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000
    )
