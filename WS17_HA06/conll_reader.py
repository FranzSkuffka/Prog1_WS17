#! /usr/bin/env python3

# -----------------------------------
# Version: 0.0.1
# Author: Jan Wirth
# Description: Extract ngram sequences from tokenized file
# -----------------------------------

import sys

def find_ngrams(input_list, n):
  return zip(*[input_list[i:] for i in range(n)])

def conll_reader(filename, n, output_file):
    print(filename)
    """This function extracts tokens from a given file, picks out n-long sequences of ngrams and sorts them into a new list. Items of that list are written into a new file and separated by linebreaks."""

    with open(filename) as active_file:
        lines = active_file.readlines()
        word_list = [line.split()[3] for line in lines if line.strip()
                     and not line.startswith("#")]
        ngrams = find_ngrams(word_list, n)

    with open(output_file, "w") as output:
        for ngram in sorted(map( lambda ngram: ' '.join(ngram), ngrams)):
            if type(ngram == "<class 'str'>"):
              output.write(str(ngram))
              output.write("\n")

    return


if __name__ == "__main__":
    conll_reader(sys.argv[1], int(sys.argv[2]), sys.argv[3])
