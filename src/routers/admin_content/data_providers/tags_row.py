# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 28/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from models.content.tags_row import TagsRow
from routers.admin_content.forms import TagsRowForm


class TagsRowDataProvider(object):
    def get_data(self):
        return dict(
            tags_row_form=TagsRowForm(TagsRow.get())
        )

admin_tags_row_data_provider = TagsRowDataProvider()
