#! /usr/bin/env python3

# -----------------------------------
# Version: 0.0.1
# Author: Jan Wirth
# -----------------------------------

"""This module analyzes data provided by the crossword script and prints output after analysis."""

def extract_masking_information(masked_word, masked_char):
  """Takes given word and returns a list of masked indices."""
  maskedcharsatindex = []
  for i in range(len(masked_word)):
    if masked_word[i] == masked_char:
      maskedcharsatindex.append(i)
  return maskedcharsatindex

def maskword(word, masked_char, maskedcharatindex):
  """Takes a word and a list of indices, returns a masked word."""
  output = []
  for i in range(len(word)):
    if i in maskedcharatindex:
      output.append(masked_char)
    else:
      output.append(word[i])
  return "".join(output)

def makematchingwordsdict(word_freq, masked_word, masked_char):
  """Collects all words that match a masked word in a dictionary(clearword:freq)."""
  out = {}
  maskedcharsatindex = extract_masking_information(masked_word, masked_char)
  temporaryword = ""
  for i in word_freq.keys():
    temporaryword = maskword(i, masked_char, maskedcharsatindex)
    if masked_word == temporaryword:
      out[i]=word_freq[i]
  return out

def makedictlist(word_freq, masked_words, masked_char):
  """Creates dictionary list as required by worksheet."""
  dictlist = []
  for i in masked_words:
    dictlist.append([i, makematchingwordsdict(word_freq, i, masked_char)])
  return dictlist

def output_function(word_freq, masked_char, masked_words, output_file_name="abc"):
  """Writes analyzed data to file provided by user."""
  dictlist = makedictlist(word_freq, masked_words, masked_char)
  preout = [" : ".join([i[0], str(i[1])]) for i in dictlist]
  out = "\n".join(preout)
  with open(output_file_name, "w") as o:
    o.write(out)
