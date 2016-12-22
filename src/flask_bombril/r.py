# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# The MIT License (MIT)
# ======================================================================================================================
# Copyright (c) 2016 [Marco Aurélio Prado - marco.pdsv@gmail.com]
# ======================================================================================================================


class Resources:
    def __init__(self):
        self.string = self.__Strings()
        self.id = self.__Ids()
        self.dimen = self.__Dimens()

    class __Strings:
        def __init__(self):
            self.validators = self.__Validators()
            self.test_message = "Mensagem de teste"
            self.test_message_2 = "Mensagem de teste 2"
            self.static = "static"
            self.toast = "toast"
            self.category_separator = "-"

        class __Validators:
            def __init__(self):
                self.required_field = "Campo obrigatório."
                self.invalid_email_format = "Formato de email inválido."
                self.email_already_registered = "Email já cadastrado."
                self.unique_field = "Valor já registrado."
                self.field_min_length_singular = "O campo deve possuir no mínimo %(min_length)d caracter."
                self.field_min_length_plural = "O campo deve possuir no mínimo %(min_length)d caracteres."
                self.field_max_length_singular = "O campo deve possuir no máximo %(max_length)d caracter."
                self.field_max_length_plural = "O campo deve possuir no máximo %(max_length)d caracteres."
                self.field_length_range = "O campo deve possuir entre %(min_length)d e %(max_length)d caracteres."
                self.invalid_field_name = "Invalid field name '%(field_name)s'."
                self.field_must_be_equal_to = "Este campo precisa ser igual ao campo %(other_name)s."
                self.always_error = "Essa mensagem de erro sempre será lançada para esse campo"

    class __Ids:
        def __init__(self):
            self.example = "example"

    class __Dimens:
        def __init__(self):
            self.test_int = 42
            self.test_int_2 = 17

R = Resources()
