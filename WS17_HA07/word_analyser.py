from corpus_loader import load_corpus_by_file, load_corpus_lines
from itertools import groupby
from functools import reduce


def analyse_mode_word(pattern, word_type):
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
    print('Frequency of words identified by ' + word_type + ' in the corpus ' + pattern.split('.')[-1])
    list(map(lambda group: print(len(group[1]), group[0]), reversed(groups_by_size)))
