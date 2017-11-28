#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

""" A basic week planner. Takes a day at a time."""
__author__      = "Jan Wirth <contact@jan-wirth.de"
__version__     = "0.0.1"

def check_equality(a, b):
  if a == b :
    print("SAME VALUE: " + str(a))
  else:
    print("DIFFERENT VALUES")
    print("FIRST: " + str(a))
    print("SECOND: " + str(b))


def main():
  first = input('First value: ').strip('')
  second = input('Second value: ').strip('')
  check_equality(first, second)

if __name__ == "__main__":
  main()
