#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from multiplication import multiply_builtin, multiply_for, multiply_while

"""
tests for multiplication functions.
"""
__author__      = "Jan Wirth <contact@jan-wirth.de"
__version__     = "0.0.1"

def test(a, b):
  print('')
  print(str(a) + ' ' + str(b))
  print(multiply_builtin(a,b))
  print(multiply_while(a,b))
  print(multiply_for(a,b))


def main():
  test(0,0)
  test(0,1)
  test(1,0)
  test(3,1)
  test(1,3)
  test(-3,1)
  test(1,-3)
  test(-3,-5)
  test(-3,-10)
  test(-10,-10)
  test(10,-10)
  test(-10,-3)
  test(100,123)
  test(100,-100)
  test(-100,-30)
  test(-100, 123325234)

if __name__ == "__main__":
  main()
