#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

""" A basic text analysis tool."""
__author__      = "Jan Wirth <contact@jan-wirth.de"
__version__     = "0.0.1"

from itertools import groupby
from functools import reduce
import re

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

def analyze (tokens):
  """ Analyzes a given string with regard to token lengths """
  _print('The text contains ' + str(len(tokens)) + ' words:'),
  groups = {key:list(group) for key, group in groupby(sorted(tokens, key=len), len)}
  for key in groups:
    _print(str(len(groups[key])) + ' word(s) with ' + str(key) + ' letters')

  lengths = list(map(len, tokens))
  total_length = reduce(sum, lengths)
  avg_len = total_length / len(tokens)
  _print('Average word length is ' + str(avg_len) + '.')

def preprocess (token):
  return re.sub('[^a-zA-Z]', '', token)

""" a fp helper for reduce """
def sum (a = 0, b = 0): return a + b

def interactive_analysis():
  text = _input('Please enter some text here: ')
  mode = _input('Please choose (s)imple (h)euristic: ')
  tokens = text.split(' ')
  if mode == 's':
    analyze(tokens)
  elif mode == 'h':
    analyze(list(map(preprocess, tokens)))
  else:
    _print('Mode not supported: "' + mode + '"')



def main():
  interactive_analysis()

if __name__ == "__main__":
  main()
