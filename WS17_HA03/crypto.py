#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


""" A basic cryptographic algorithm. Takes a char at a time."""
__author__      = "Jan Wirth <contact@jan-wirth.de"
__version__     = "0.0.1"

def user_input(msg):
  """ Asks the user for integers and only accepts integers ;) """
  try:
    return int(input(msg))
  except ValueError:
    print('')
    return user_input(msg)

if __name__ == "__main__":
  main()
