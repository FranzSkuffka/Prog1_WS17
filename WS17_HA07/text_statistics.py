#! /usr/bin/env python3

doc = """

# -----------------------------------
# Version: 0.0.1
# Author: Jan Wirth
# Description: Check a list of strings if they are minimal pairs. Supports HTML and TXT formats.
# 
# Usage:
# python3 my_pairs.html
# python3 my_pairs.txt
# -----------------------------------
"""

import sys
import re

def check(pairs):
  print('checking', pairs)

def extract_html_line(line):
  type = re.search('class="(.*)"', line).group().split('"')[1]
  tokens = (
      re.search('>(\S+)', line).group()[1:]
    , re.search('(\S+)<', line).group()[:-1]
  )
  return (type, tokens)


filter_usable = lambda lines: list(filter(lambda line: re.search(re.compile('  '), line), lines))
def extract_txt_lines(type, lines):
  usable = filter_usable(lines.split('\n'))
  matches = list(map( lambda line: re.findall('\S+', line), usable))
  return list(map( lambda match: (type, (match[0], match[1])), matches))

def read(path):
  mode = path.split('.')[1]
  if mode == 'html':
    print('\nHTML MODE')

    with open(path) as active_file:
      lines = active_file.readlines()
      usable_lines = list(filter(lambda line: re.search(re.compile('class'), line), lines))
      pairs = list(map(extract_html_line, usable_lines))

      return pairs

  if mode == 'txt':
    print('\nTXT MODE')

    with open(path) as active_file:
      [minimal_txt, non_minimal_txt] = active_file.read().split('\n\n')

      return extract_txt_lines('minimal', minimal_txt) + extract_txt_lines('notminimal', non_minimal_txt)

def compare_equal_length(pair):
  type = pair[0]
  a = pair[1][0]
  b = pair[1][1]
  mismatch_count = 0
  for i in range(len(a)):
    if a[i] != b[i]:
      mismatch_count = mismatch_count + 1
  if mismatch_count == 1 and type == 'minimal': # TRUE POSITIVE
    return (type, (a, b), 'TP')
  elif type == 'minimal': # FALSE NEGATIVE
    return (type, (a, b), 'FN')
  elif mismatch_count == 1 and type == 'notminimal': # FALSE POSITIVE
    return (type, (a, b), 'FP')
  elif type == 'notminimal': # TRUE NEGATIVE
    return (type, (a, b), 'TN')

def compare_different_length (pair, longer, shorter):
  type = pair[0]
  a = pair[1][0]
  b = pair[1][1]
  for i in range(len(longer)):
    if longer[:i] + longer[i+1:] == shorter:
      return (type, (a, b), 'TP')
  if (type == 'notminimal'):
    return (type, (a, b), 'TN')
  elif (type == 'minimal'):
    return (type, (a, b), 'FN')

def compare (pair):
  type = pair[0]
  a = pair[1][0]
  b = pair[1][1]
  if abs(len(a) - len(b)) > 1:
    return (type, (a, b), 'TN')
  elif len(a) == len(b):
    return compare_equal_length(pair)
  elif len(a) - len(b) == 1:
    return compare_different_length(pair, a, b)
  elif len(b) - len(a) == 1:
    return compare_different_length(pair, b, a)

def summarize(res):
  minimals = list(filter(lambda pair: pair[2] == 'TP', res))
  non_minimals = list(filter(lambda pair: pair[2] == 'TN', res))
  print('\nTOTAL NUMBER OF PAIRS ANALYSED: ' + str(len(res)))
  print('\nTOTAL NUMBER OF MINIMAL PAIRS FOUND: ' + str(len(minimals)))

  print('\nMATCHED')
  list(map(lambda analysed_pair: print(analysed_pair[1][0], analysed_pair[1][1]), minimals))
  print('\nNOT MATCHED')
  list(map(lambda analysed_pair: print(analysed_pair[1][0], analysed_pair[1][1]), non_minimals))

if __name__ == "__main__":
  print("\nstarting minimal pair checker")
  pairs = read(sys.argv[1])
  res = list(map(compare, pairs))
  summarize(res)
