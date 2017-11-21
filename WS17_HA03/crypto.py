#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


""" A basic cryptographer. Takes a word at a time."""
__author__      = "Jan Wirth <contact@jan-wirth.de"
__version__     = "0.0.1"

import re

def _input():
  """
  a wrapper for `input`
  """
  return input()

def _print(msg):
  """
  a wrapper for `print`
  """
  return print(msg)

def user_input():
  word = _input()
  try:
    re.match('^[a-z]*$', word).group()
    return word
  except AttributeError:
    remind_user_of_supported_stuff()
    return user_input()

def remind_user_of_supported_stuff():
    _print('Only lowercase characters are supported')

def encrypt (word, shiftBy = 13):
  """
  Shift a character from /[a-z]/ to the nth next charater
  where `n` defaults to 13.
  """
  return crypto(char, shiftBy)

def encrypt (word, shiftBy = -13):
  """
  Shift a character from /[a-z]/ to the -nth next charater
  where `n` defaults to 13.
  """
  return ''.join(
     list(
        map(cryptoWith(), list(word))
     )
  )

def cryptoWith(shiftBy = 13):
  """
  ALbAM Algorithm
  """
  return lambda char: shiftLower(char, shiftBy)

def shiftLower (char,by):
  """ shifts a char on the ring a-z by n """
  lo = ord('a')
  hi = ord('z')
  newPos = ord(char) + by
  if newPos > hi:
    return chr(newPos - 24)
  elif newPos < lo:
    return chr(newPos + 24)
  else:
    return chr(newPos)


def encrypt_successive_inputs():
  word = user_input()
  if word != '':
    _print(encrypt(word))
    encrypt_successive_inputs()
  else:
    _print('end')
    return

def main():
  encrypt_successive_inputs()

if __name__ == "__main__":
  main()
