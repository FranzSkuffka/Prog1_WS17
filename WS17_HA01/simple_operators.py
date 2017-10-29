#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


""" Demonstrate operators in python """
__author__      = "Jan Wirth <contact@jan-wirth.de"
__version__      = "0.0.1"

badOperations = []
goodOperations = []

def add (a, b): return a + b
def subtract (a, b): return a - b
def multiply (a, b): return a * b
def divide (a, b): return a / b

myint = 7
myfloat = 3.4
mystring = "Foo"

print('myint = 7')
print('myfloat = 3.4')
print('mystring = "Foo"')

print(' ')

# This should be refactored to automatically determine all permutations.
# However, this implemetation is more explicit.
# I'll just leave it like that it's not supposed to scale anyways.
def test (operator, myint, mystring, myfloat):
  print('')
  print('')
  print('')
  print('')
  print(operator)
  # identical
  # 
  print('mystring, mystring')
  try:
    res = operator(mystring, mystring)
    print(res)
    print(type(res))
    goodOperations.append([operator, type(mystring), type(mystring), res, type(res)])
  except TypeError as err:
    print(err)
    badOperations.append([operator, type(mystring), type(mystring), err])

  print('')
  print('myint, myint')
  try:
    res = operator(myint, myint)
    print(res)
    print(type(res))
    goodOperations.append([operator, type(myint), type(myint), res, type(res)])
  except TypeError as err:
    print(err)
    badOperations.append([operator, type(myint), type(myint), err])

  print('')
  print('myfloat, myfloat')
  try:
    res = operator(myfloat, myfloat)
    print(res)
    print(type(res))
    goodOperations.append([operator, type(myfloat), type(myfloat), res, type(res)])
  except TypeError as err:
    print(err)
    badOperations.append([operator, type(myfloat), type(myfloat), err])

  # non-identical combinations
  # 
  print('')
  print('mystring, myint')
  try:
    res = operator(mystring, myint)
    print(res)
    print(type(res))
    goodOperations.append([operator, type(mystring), type(myint), res, type(res)])
  except TypeError as err:
    print(err)
    badOperations.append([operator, type(mystring), type(myint), err])

  print('')
  print('myint, myfloat')
  try:
    res = operator(myint, myfloat)
    print(res)
    print(type(res))
    goodOperations.append([operator, type(myint), type(myfloat), res, type(res)])
  except TypeError as err:
    print(err)
    badOperations.append([operator, type(myint), type(myfloat), err])

  print('')
  print('myfloat, mystring')
  try:
    res = operator(myfloat, mystring)
    print(res)
    print(type(res))
    goodOperations.append([operator, type(myfloat), type(mystring), res, type(res)])
  except TypeError as err:
    print(err)
    badOperations.append([operator, type(myfloat), type(mystring), err])

  # reversed
  # 
  print('')
  print('myint, mystring')
  try:
    res = operator(myint, mystring)
    print(res)
    print(type(res))
    goodOperations.append([operator, type(myint), type(mystring), res, type(res)])
  except TypeError as err:
    print(err)
    badOperations.append([operator, type(myint), type(mystring), err])

  print('')
  print('myfloat, myint')
  try:
    res = operator(myfloat, myint)
    print(res)
    print(type(res))
    goodOperations.append([operator, type(myfloat), type(myint), res, type(res)])
  except TypeError as err:
    print(err)
    badOperations.append([operator, type(myfloat), type(myint), err])

  print('')
  print('mystring, myfloat')
  try:
    res = operator(mystring, myfloat)
    print(res)
    print(type(res))
    goodOperations.append([operator, type(mystring), type(myfloat), res, type(res)])
  except TypeError as err:
    print(err)
    badOperations.append([operator, type(mystring), type(myfloat), err])

test(add, myint, mystring, myfloat)
test(subtract, myint, mystring, myfloat)
test(multiply, myint, mystring, myfloat)
test(divide, myint, mystring, myfloat)


print("")
print("")

print("SUMMARY")

print("")
print("What went well")
for report in goodOperations:
  print(report)


print("")
print("What went sideways")
for report in badOperations:
  print(report)


"""
Exercise 4

- We get the error

  TypeError: cannot concatenate 'str' and 'int' objects

  when running `"string" + 1`.

- Python3, in comparison to, say, ES6 does not casting int to string when using the '+' operator.

"""
