#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


""" Examine type precedences """
__author__      = "Jan Wirth <contact@jan-wirth.de"
__version__     = "0.0.1"



a = ((1 + (2 * 3)) - 4)
b = (a ** (2 ** a))
c = (a == 23)
d = (([] or None) and [1 ,2 ,3]) # eval of [1, 2, 3] not necessary because `None and whatever` an `whatever and None` are always `None`
e = ([0] or None)
f = ((not True) or (d == 0))
g = (3 and -4) + 1 # -4 not evaluated - for two integer operands, the `and` binary operator always returns the second operand


print("a = " + str (a) + " -- erwarteter Wert : 3")
print("bool(a) = " + str( bool (a) ) + " -- erwarteter boolscher Wert : True")
print("")

print("b = " + str (b) + " -- erwarteter Wert : 6561")
print("bool(b) = " + str( bool (b) ) + " -- erwarteter boolscher Wert : True")
print("")

print("c = " + str (c) + " -- erwarteter Wert : False")
print("bool(c) = " + str( bool (c) ) + " -- erwarteter boolscher Wert : False")
print("")

print("d = " + str (d) + " -- erwarteter Wert : None")
print("bool(d) = " + str( bool (d) ) + " -- erwarteter boolscher Wert : False")
print("")

print("e = " + str (e) + " -- erwarteter Wert : [0]")
print("bool(e) = " + str( bool (e) ) + " -- erwarteter boolscher Wert : True")
print("")

print("f = " + str (f) + " -- erwarteter Wert : False")
print("bool(f) = " + str( bool (f) ) + " -- erwarteter boolscher Wert : False")
print("")

print("g = " + str (g) + " -- erwarteter Wert : -3")
print("bool(g) = " + str( bool (g) ) + " -- erwarteter boolscher Wert : True")
print("")

