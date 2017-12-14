#! /usr/bin/env python3

# -----------------------------------
# Version: 0.0.1
# Author: Lennard Böhnke
# Description: Extract ngram sequences from tokenized file
# Last modified: 2017-12-12T18:02:19.239Z
# -----------------------------------

import sys


def conll_reader(filename, n, output_file):
    """This function extracts tokens from a given file, picks out n-long sequences of ngrams and sorts them into a new list. Items of that list are written into a new file and separated by linebreaks."""

    with open(filename) as active_file:
        lines = active_file.readlines()
        word_list = [line.split()[3] for line in lines if line.strip()
                     and not line.startswith("#")]
        extract_ngrams = [
            word_list[i:i + int(n)] for i in range(len(word_list) - int(n) + 1)]

    with open(output_file, "w") as output:
        for item in sorted(extract_ngrams):
            output.write(str(item))
            output.write("\n")

    return


if __name__ == "__main__":
    print(conll_reader(sys.argv[1], sys.argv[2], sys.argv[3]))
