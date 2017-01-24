# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 04/01/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================


class InvalidIdError(Exception):
    pass


class InvalidOrderStatusIdError(Exception):
    pass


class InvalidSortMapError(Exception):
    pass


class InvalidNUnitsError(Exception):
    pass


class InvalidOrderStatusChange(Exception):
    pass


class InsufficientStockToSendOrder(Exception):
    def __init__(self, limiting_product):
        super(InsufficientStockToSendOrder, self).__init__()
        self.limiting_product = limiting_product


class InconsistentDataBaseError(Exception):
    pass


class InvalidClientToOrder(Exception):
    pass


class InvalidOrderError(Exception):
    pass
