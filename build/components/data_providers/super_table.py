# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 06/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================

class SuperTableDataProvider(object):
    def get_sort_methods_data(self, selected_sort_method_id, sort_method_ids, sort_method_names):
        sort_method_data = []
        for sort_method_id, sort_method_name in zip(sort_method_ids, sort_method_names):
            sort_method_data.append(dict(
                name=sort_method_name,
                value=str(sort_method_id.value),
                selected=sort_method_id==selected_sort_method_id
            ))
        return sort_method_data


super_table_data_provider = SuperTableDataProvider()