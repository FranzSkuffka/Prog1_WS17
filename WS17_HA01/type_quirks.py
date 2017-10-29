#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


""" Demonstrate the python type system """
__author__      = "Jan Wirth <contact@jan-wirth.de"
__version__      = "0.0.1"


i = 3
j = 2
k = 1.5
s = " hello "
b = True
jk = j + k
svar1 = s * i
svar2 = s * 3
ib = i + b



print("i", i, type(i), "Literal constant as defined")
print("j", j, type(j), "Literal constant as defined")
print("k", k, type(k), "Literal constant as defined")
print("s", s, type(s), "Literal constant as defined")
print("b", b, type(b), "Literal constant as defined")
print("jk", jk, type(jk), "Int gets casted to float, 'the least common denominator type'. Then values are added.")
print("svar1", svar1, type(svar1), "The string typeclass defines this behavior for multiplication with integers.")
print("svar2", svar2, type(svar2), "The string typeclass defines this behavior for multiplication with integers.")
print("ib", ib, type(ib), "Bool is a subclass of int. True == 1, False == 2.")
