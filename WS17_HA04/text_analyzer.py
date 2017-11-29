#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

""" A basic text analysis tool."""
__author__      = "Jan Wirth <contact@jan-wirth.de"
__version__     = "0.0.1"

from itertools import groupby

def _input(msg):
  """
  a wrapper for `input`
  """
  return input(msg)

def _print(msg):
  """
  a wrapper for `print`
  """
  return print(msg)

def simple (text):
  tokens = text.split(' ')
  _print('The text contains ' + str(len(tokens)) + ' words:'),
  groups = {key:list(group) for key, group in groupby(sorted(tokens, key=len), len)}
  for key in groups:
    _print(str(len(groups[key])) + ' word(s) with ' + str(key) + ' letters')

def heuristic (text):
  _print('loool')

def interactive_analysis():
  modes = {
    's': simple,
    'h': heuristic
  }
  text = _input('Please enter some text here: ')
  mode = _input('Please choose (s)imple (h)euristic: ')
  modes[mode](text)



def main():
  interactive_analysis()

if __name__ == "__main__":
  main()
