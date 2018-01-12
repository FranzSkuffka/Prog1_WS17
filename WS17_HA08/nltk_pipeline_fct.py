#! /usr/bin/env python3

# -----------------------------------
# Version: 0.0.1
# Author: Jan Wirth
# Description: Functional NLTK Pipeline for tagging and lemmatising
# -----------------------------------

import nltk
from shared import read_file, write_file, lemmatize

""" Take a sentence as string. Return array of (original_word, lemmatized, POS) """
def process_sentence(sent):
  tokenized = nltk.word_tokenize(sent, language='english', preserve_line=False)
  tagged = nltk.pos_tag(tokenized, tagset=None, lang='eng')
  return list(map(lemmatize_word, tagged))

def lemmatize_word(word_tuple):
  lemma = lemmatize(word_tuple[0], word_tuple[1])
  return (word_tuple[0], lemma, word_tuple[1])

def annotate_corpus_with_nltk_pipeline(input_filename, language):
  text = read_file(input_filename)
  sentences = nltk.sent_tokenize(text, language='english')
  annotated_sentences = list(map(process_sentence, sentences))
  return annotated_sentences

def flatten_and_render(sentences):
  lines = []
  for si, sent in enumerate(sentences):
    for wi, word in enumerate(sent):
      line = str(si) + '\t' + str(wi) + '\t' + str(word[0]) + '\t' + str(word[1]) + '\t' + str(word[2]) + '\n'
      print(line)
      lines.append(line)
  return lines

def write_conll_format_output(output_filename, sentences):
  lines = flatten_and_render(sentences)
  write_file(output_filename, lines)
