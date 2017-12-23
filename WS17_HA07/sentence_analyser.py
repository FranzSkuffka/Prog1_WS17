doc = """
# -----------------------------------
# Version: 0.0.1
# Author: Jan Wirth
# Description: Analyse a corpus of with regard to sentences
# -----------------------------------
"""

from corpus_loader import load_corpus_by_file
from functools import reduce

def analyse_sentences(sentence_corpora):
  clean_sentence_corpora = list(map(lambda file_corpus: (file_corpus[0], '\n'.join(file_corpus[1].split('\n')[1:-3])), sentence_corpora))
  analysed_files = list(map(analyse_file_corpus_sentences, clean_sentence_corpora))
  return analysed_files

def analyse_mode_sentence(pattern):
  sentence_corpora = load_corpus_by_file(pattern)
  summarize_sentence_analysis(analyse_sentences(sentence_corpora))

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
