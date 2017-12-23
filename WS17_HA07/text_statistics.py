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

from sentence_analyser import analyse_mode_sentence
from word_analyser import analyse_mode_word
from normalise_analyser import analyse_mode_normalise

if __name__ == "__main__":
  mode = sys.argv[1]
  path = sys.argv[2]
  file_identifier = sys.argv[3]
  pattern = path + '/**/*' + file_identifier
  if mode == 'word':
    print('STARTING MODE', mode)
    word_type = sys.argv[4]
    analyse_mode_word(pattern, word_type)

  elif mode == 'sent':
    print('STARTING MODE', mode)
    analyse_mode_sentence(pattern)

  elif mode == 'normalise':
    word_frequency_threshold = sys.argv[4]
    print('STARTING MODE', mode)
    analyse_mode_normalise(pattern, int(word_frequency_threshold))

  else:
    print('unsupported mode', mode)
