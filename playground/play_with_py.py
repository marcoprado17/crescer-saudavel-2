# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
class A(object):
    @classmethod
    def foo(cls):
        x = cls()
        x.boo()

    def my_abstract_method(self):
        raise NotImplementedError

class B(A):
    def boo(self):
        print "boo"

b = B()
b.my_abstract_method()
B.foo()