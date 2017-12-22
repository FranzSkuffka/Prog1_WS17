#! /usr/bin/env python3

doc = """

# -----------------------------------
# Version: 0.0.1
# Author: Jan Wirth
# Description: Analyse a corpus of text.
# 
# Usage:
# python3 text_statistics.py word ./on-conll12-eng-train-bn/ .v4_gold_conll CC
# python3 text_statistics.py sent ./on-conll12-eng-train-bn/ .v4_gold_conll CC
# -----------------------------------
"""

import sys
import re
import glob
import nltk
from itertools import groupby

def load_text(path):
  return open(path, 'r').read()

def load_corpus_lines(path, file_identifier):
  pattern = path + '/**/*' + file_identifier
  files = glob.iglob(pattern, recursive=True)
  corpus = '\n'.join(list(map(load_text, files)))
  lines = corpus.split('\n')
  valid_lines = filter(lambda line: line[:2] == 'bn', lines)
  return valid_lines

if __name__ == "__main__":
  mode = sys.argv[1]
  path = sys.argv[2]
  file_identifier = sys.argv[3]
  if mode == 'word':
    word_type = sys.argv[4]
    print('Analysing words with type ' + word_type)
    lines = load_corpus_lines(path, file_identifier)
    lines_in_cells = map(lambda line: list(filter(lambda col: col != '', line.split(' '))), lines)
    relevant_data = map(lambda parts: (parts[3], parts[4]), lines_in_cells)
    only_words_with_given_type = filter(lambda word: word[1] == word_type, relevant_data)

    # sort | uniq -c
    groups_iterable = groupby(sorted(only_words_with_given_type, key=lambda word: word[0]), lambda word: word[0])
    # convert from iterable object to the real shit
    groups = map(lambda group: (group[0], list(group[1])), groups_iterable)

    # sort
    groups_by_size = sorted(groups, key=lambda group: len(list(group[1])))

    print('Frequency of words identified by ' + word_type + ' in the corpus ' + file_identifier)
    list(map(lambda group: print(len(group[1]), group[0]), reversed(groups_by_size)))
