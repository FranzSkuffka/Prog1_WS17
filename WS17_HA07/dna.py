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
import random

def find_ngrams(input_list, n):
  return zip(*[input_list[i:] for i in range(n)])


bases = [
  "T",
  "C",
  "A",
  "G"
]

complements = {
  "A": "T",
  "G": "C",
  "T": "A",
  "C": "G"
}

def generate_dna(length, matching):
  rna = generate_rna(length)
  if matching:
    return list(map(lambda base: [base, matching_base(base)], rna))
  else:
    return list(map(lambda base: [base, random_base(base)], rna))

def matching_base(source):
  return complements[source]

def random_base(_):
  return bases[random.randrange(0, 4)]

def generate_rna(length):
  skeleton = list(range(0, length))
  return list(map(random_base, skeleton))

def write_rendered (path, dna_render):
    with open(path, "w") as output:
      output.write(dna_render)
    return

def matches(pair):
  return pair[1] == complements[pair[0]]

def check_dna(path):
  with open(path) as active_file:
    lines = active_file.readlines()

    print('Analysing DNA')
    print('\n'.join(lines))
    match_list = list(map(lambda line: matches(line.split()), lines))
    total_base_count = len(match_list)
    matching_base_count = len(list(filter(lambda i: i, match_list)))
    matching_percent = matching_base_count / total_base_count * 100

    print( "DNA pairs match with " + str(matching_percent) + "%")

def render_dna (dna):
  return ''.join(list(map(lambda pair: pair[0] + " " + pair[1] + "\n", dna)))

def generate_and_write(path, mode, length):
  if mode == 'random':
    generated  = generate_dna(int(length), False)
  elif mode == 'matching':
    generated  = generate_dna(int(length), True)
  else:
    print("ERROR, UNSUPPORTED MODE: " + mode)
    return print(doc)

  rendered = render_dna(generated)
  print("writing new " + mode + " DNA with length " + length + " to file " + path)
  print(rendered)
  write_rendered(path, rendered)
  

if __name__ == "__main__":
  print("starting DNA tools")
  try:
    mode = sys.argv[1]
    file_path = sys.argv[2]
    if mode == 'generate':
      generation_mode = sys.argv[3]
      length = sys.argv[4]
      generate_and_write(file_path, generation_mode, length)
    elif mode == 'analyse':
      check_dna(file_path)
    else:
      print(doc)
  except:
    print("ERROR")
    print(doc)
