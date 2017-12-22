#! /usr/bin/env python3

doc = """

# -----------------------------------
# Version: 0.0.1
# Author: Jan Wirth
# Description: Create and analyze a DNA sequence
# 
# Usage:
# python3 dna.py generate my_dna random 10
# python3 dna.py generate my_dna matching 10
#
# python3 dna.py analyse my_dna
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

def compare (pair):
  type = pair[0]
  a = pair[1][0]
  b = pair[1][1]
  if len(a) == len(b):
    mismatch_count = 0
    for i in range(len(a)):
      if a[i] != b[i]:
        mismatch_count = mismatch_count + 1
    if mismatch_count == 1 and type == 'minimal': # TRUE POSITIVE
      return (type, pair[1], 'TP')
    elif type == 'minimal': # FALSE NEGATIVE
      return (type, pair[1], 'FN')
    elif mismatch_count == 1 and type == 'notminimal': # FALSE POSITIVE
      return (type, pair[1], 'FP')
    elif type == 'notminimal': # TRUE NEGATIVE
      return (type, pair[1], 'TN')


def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

if __name__ == "__main__":
  print("\nstarting minimal pair checker")
  pairs = read(sys.argv[1])
  print(pairs)
  print(list(map(compare, pairs)))
