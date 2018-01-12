#! /usr/bin/env python3

# -----------------------------------
# Version: 0.0.1
# Author: Jan Wirth
# Description: General utilities for text processing.
# -----------------------------------

import nltk
Lemmatizer = nltk.stem.WordNetLemmatizer()

""" Read a file by filename its contents """
def read_file(filename):
  with open(filename) as active_file:
    return active_file.read()

""" Write lines to a file """
def write_file(filename, lines):
  with open(filename, 'w') as active_file:
    for line in lines:
      active_file.write(line)


POS_MAP = {
  'N': 'n',
  'V': 'v',
  'J': 'a',
  'R': 'r'
}

"""
get the POS WN constant
ignores ADJ
"""
def get_wn_pos_constant(pos):
  if pos == 'MD'
    key = 'V'
  else
    key = POS_MAP[pos[0:1]]
  try:
    constant = POS_MAP[key]
  except KeyError:
    constant = POS_MAP['N']
  return constant

def lemmatize(word, pos):
  constant = get_wn_pos_constant(pos)
  return Lemmatizer.lemmatize(word, pos=constant)
