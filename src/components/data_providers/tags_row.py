# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 28/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.content.tags_row import TagsRow


class TagsRowDataProvider(object):
    def get_data(self):
        return TagsRow.get()

tags_row_data_provider = TagsRowDataProvider()
