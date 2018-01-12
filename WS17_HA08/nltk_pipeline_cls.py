#! /usr/bin/env python3

# -----------------------------------
# Version: 0.0.1
# Author: Jan Wirth
# Description: OO NLTK Pipeline for tagging and lemmatising
# -----------------------------------

import nltk

from shared import read_file, write_file

from Word import Word

class Sentence:
  """ Supports tokenizing, tagging and lemmatizing """

  def tokenize(self):
    tokens = nltk.word_tokenize(self.text, language='english', preserve_line=False)
    self.words = list(map(Word, tokens))

  def tag(self):
    tokens = list(map(lambda w: w.text, self.words))
    tagged_tokens = nltk.pos_tag(tokens, tagset=None, lang='eng')
    for i, pair in enumerate(tagged_tokens):
      self.words[i].set_tag(pair[1])

  def lemmatize(self):
    for w in self.words:
      w.lemmatize()

  def render(self):
    lines = []
    for i, w in enumerate(self.words):
      lines.append(str(i) + '\t' + w.render())
    return lines

  def __init__(self, text):
    self.text = text
    self.tagged_tokens = []


def annotate_corpus_with_nltk_pipeline(input_filename, language):
  text = read_file(input_filename)
  sentences = extract_sentences(text)
  for sent in sentences:
    sent.tokenize()
    sent.tag()
    sent.lemmatize()
  return sentences
  # annotated_sentences = list(map(process_sentence, sentences))
  # return annotated_sentences

def extract_sentences(corpus):
  sentences = nltk.sent_tokenize(corpus, language='english')
  return list(map(Sentence, sentences))

# """ Take a sentence as string. Return array of (original_word, lemmatized, POS) """
# def process_sentence(sent):
#   tokenized = nltk.word_tokenize(sent, language='english', preserve_line=False)
#   tagged = nltk.pos_tag(tokenized, tagset=None, lang='eng')
#   return list(map(lemmatize_word, tagged))

def write_conll_format_output(output_filename, sentences):
  rendered_sentences = list(map(lambda s: s.render(), sentences))
  lines = []
  for i, sent in enumerate(rendered_sentences):
    for line in sent:
      lines.append(str(i) + '\t' + line + '\n')
  write_file(output_filename, lines)
