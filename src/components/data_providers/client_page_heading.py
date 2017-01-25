# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 25/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================


class ClientPageHeadingDataProvider(object):
    def get_data(self):
        return dict(
            path=[
                dict(
                    name="Home",
                    href="#",
                ),
                dict(
                    name="Sobre nós",
                )
            ],
            title="Sobre nós",
        )


client_page_heading_data_provider = ClientPageHeadingDataProvider()
