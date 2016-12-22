# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================
from flask_bombril.utils import AutoNumber


class Resources:
    def __init__(self):
        self.string = self.__Strings()
        self.id = self.__Ids()
        self.dimen = self.__Dimens()

    class __Strings:
        def __init__(self):
            self.temp_error_html = "Ocorreu um erro inesperado em nossos servidores, nossa equipe técnica resolverá o problema assim que possível. Clique <a href=%(home_page_href)s>aqui</a> para voltar à pagina inicial."

    class __Ids:
        def __init__(self):
            pass

        class Enum1(AutoNumber):
            value_1 = ()
            value_2 = ()

        class Enum2(AutoNumber):
            value_1 = ()
            value_2 = ()
            value_3 = ()

    class __Dimens:
        def __init__(self):
            self.example = 42

R = Resources()
