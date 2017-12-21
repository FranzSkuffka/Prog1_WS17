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

if __name__ == "__main__":
  print("\nstarting minimal pair checker")
  pairs = read(sys.argv[1])
  print(pairs)
