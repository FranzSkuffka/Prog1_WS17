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
from functools import reduce

def load_text(path):
  filename = path.split('/')[-1]
  return (filename, open(path, 'r').read())


def load_corpus_lines(pattern):
  corpus = load_corpus(pattern)
  lines = corpus.split('\n')
  valid_lines = filter(lambda line: line[:2] == 'bn', lines)
  return valid_lines

def load_corpus(pattern):
  files = glob.iglob(pattern, recursive=True)
  return '\n'.join( map(lambda loaded_file: loaded_file[1], map(load_text, files)) )

def load_corpus_by_file(pattern):
  files = glob.iglob(pattern, recursive=True)
  return list(map(load_text, files))

def analyse_file_corpus_sentences(file_with_corpus):
  corpus = file_with_corpus[1]
  sentences_in_words = list(map(lambda sent: sent.split('\n'), corpus.split('\n\n')))
  sentences_with_sum = list(map(len, sentences_in_words))
  total_sentence_length = reduce(lambda a, b: a + b, sentences_with_sum)
  return (file_with_corpus[0], len(sentences_in_words), total_sentence_length / len(sentences_in_words))

def summarize_sentence_analysis (sentences_meta):
  total_sentence_count = reduce(lambda a, b: a + b, map(lambda sent: sent[1], sentences_meta))
  sorted_meta = list(reversed(sentences_meta))
  avg_sentence_length = reduce(lambda a, b: a+b, map(lambda meta: meta[2], sorted_meta))/ len(sorted_meta)
  print('Analysed', len(sentences_meta), 'files with a total of', total_sentence_count,'sentences.')
  print('Avg sentence length is', round(avg_sentence_length, 2))
  print('#sentences\tavg sentence length\tfilename')
  list(map(lambda sent: print(str(sent[1]) + '\t\t' + str(round(sent[2], 2)) + '\t' + str(sent[0])), reversed(sorted_meta)))

if __name__ == "__main__":
  mode = sys.argv[1]
  path = sys.argv[2]
  file_identifier = sys.argv[3]
  pattern = path + '/**/*' + file_identifier
  if mode == 'word':
    word_type = sys.argv[4]
    files = load_corpus_by_file(pattern) # glad the computer is not as lazy as I am
    lines = load_corpus_lines(pattern)
    lines_in_cells = map(lambda line: list(filter(lambda col: col != '', line.split(' '))), lines)
    relevant_data = map(lambda parts: (parts[3], parts[4]), lines_in_cells)
    only_words_with_given_type = list(filter(lambda word: word[1] == word_type, relevant_data))

    # sort | uniq -c
    groups_iterable = groupby(sorted(only_words_with_given_type, key=lambda word: word[0]), lambda word: word[0])
    # convert from iterable object to the real shit
    groups = map(lambda group: (group[0], list(group[1])), groups_iterable)

    # sort
    groups_by_size = sorted(groups, key=lambda group: len(list(group[1])))

    print('Analysing words with type ' + word_type)
    print('Read', len(files), 'files and found', len(only_words_with_given_type), 'words with the given type.')
    print('Frequency of words identified by ' + word_type + ' in the corpus ' + file_identifier)
    list(map(lambda group: print(len(group[1]), group[0]), reversed(groups_by_size)))
  elif mode == 'sent':
    print('mode', mode)
    sentence_corpora = load_corpus_by_file(pattern)
    clean_sentence_corpora = list(map(lambda file_corpus: (file_corpus[0], '\n'.join(file_corpus[1].split('\n')[1:-3])), sentence_corpora))
    analysed_files = list(map(analyse_file_corpus_sentences, clean_sentence_corpora))
    summarize_sentence_analysis(analysed_files)
  else:
    print('unsupported mode', mode)
