from corpus_loader import load_corpus_by_file, load_corpus_lines
from sentence_analyser import analyse_sentences
from itertools import groupby
from functools import reduce
import re

def group_tokens(tokens, by):
  if by == 'type':
    key = 1
  if by == 'token':
    key = 0

  # sort | uniq -c
  groups_iterable = groupby(sorted(tokens, key=lambda word: word[key]), lambda word: word[key])
  # convert from iterable object to the real shit
  groups = map(lambda group: (group[0], list(group[1])), groups_iterable)

  # sort
  groups_by_size = sorted(groups, key=lambda group: len(list(group[1])))
  return list(reversed(groups_by_size))

def normalise_token(token):
  lowered = token[0].lower()
  escaped = re.sub('@', '#AT#', lowered)
  normalised = re.sub('[0-9]', '@', escaped)
  return (normalised, token[1])

def replace_below_threshold(tokens, word_frequency_threshold):
  grouped = group_tokens(tokens, 'token')
  above_threshold = list(map(lambda group: (group[0], check_and_replace_below_threshold(group[1], word_frequency_threshold)), grouped))
  return list(reduce(lambda a, b: a + b, map(lambda group: group[1], above_threshold))) # create a list of individual tokens

def check_and_replace_below_threshold(token_group, threshold):
  if threshold > len(token_group):
    return list(map(lambda pair: ('#OTHER', pair[1]), token_group))
  else:
    return token_group

def normalise(tokens, word_frequency_threshold):
  normalised_tokens = list(map(normalise_token, tokens))
  segmented_tokens = replace_below_threshold(normalised_tokens, word_frequency_threshold)
  return segmented_tokens

def create_token_insight(tokens):

  sorted_types = group_tokens(tokens, 'type')
  print('There are', len(sorted_types), 'different word types in the corpus.')
  print('The most frequent type in the corpus is "', sorted_types[0][0], '" with', len(sorted_types[0][1]), 'occurences and a probability of ', round( len(sorted_types[0][1]) / len(tokens), 2), '.')
  print('The second most frequent type in the corpus is "', sorted_types[1][0], '" with', len(sorted_types[1][1]), 'occurences and a probability of ', round( len(sorted_types[1][1]) / len(tokens), 2), '.')

  sorted_tokens = group_tokens(tokens, 'token')
  print('\nThe most frequent word in the corpus is "', sorted_tokens[0][0], '" with', len(sorted_tokens[0][1]), 'occurences.')
  print('The second most frequent word in the corpus is "', sorted_tokens[1][0], '" with', len(sorted_tokens[1][1]), 'occurences.')

def analyse_words(lines, word_frequency_threshold):
    lines_in_cells = map(lambda line: list(filter(lambda col: col != '', line.split(' '))), lines)
    relevant_data = list(map(lambda parts: (parts[3], parts[4]), lines_in_cells))
    normalised_relevant_data = normalise(relevant_data, word_frequency_threshold)

    print('\n\nRAW RESULTS')
    create_token_insight(relevant_data)

    print('\n\nNORMALISED RESULTS')
    create_token_insight(normalised_relevant_data)

def analyse_mode_normalise(pattern, word_frequency_threshold):
    # raw data
    sentence_corpora = load_corpus_by_file(pattern) # glad the computer is not as lazy as I am
    lines = list(load_corpus_lines(pattern))

    # sentence data
    sentence_results = analyse_sentences(sentence_corpora)
    sentence_count = reduce(lambda a, b: a + b, map(lambda sent: sent[1], sentence_results))

    # file data
    file_count = len(sentence_corpora)

    # word_data
    token_count = len(lines)
    print('Read', file_count, 'files with', token_count, 'tokens in', sentence_count, 'sentences.')

    # word analysis
    analyse_words(lines, word_frequency_threshold)
