doc = """
# -----------------------------------
# Version: 0.0.1
# Author: Jan Wirth
# Description: Load corpora given a glob pattern.text.
# -----------------------------------
"""

import glob

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
