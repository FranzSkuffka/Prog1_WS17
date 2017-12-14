#! /usr/bin/env python3

# -----------------------------------
# Version: 0.0.1
# Author: Lennard Böhnke
# Description: Insert description here
# Last modified: 2017-12-12T20:22:51.699Z
# -----------------------------------

import sys
import time


def extract_words(filename):
    """Extracts words from given file."""
    with open(filename) as active_file:
        line_list = []
        for line in active_file:
            if line.strip() and not line.startswith("#"):
                line_list.append(line)

    return line_list


def process_v1(line_list):
    """Extracts words from lines and concatenates them into a string."""
    concatenated = ""
    for line in line_list:
        concatenated = concatenated + line.split()[3]
    return concatenated


def process_v2(line_list):
    """Extracts words from lines and concatenates them into a string, this time via extended allocation."""
    concatenated = ""
    for line in line_list:
        concatenated += line.split()[3]
    return concatenated


def process_v3(line_list):
    """Extracts words from lines and joins them in a string."""
    word_list = []
    for line in line_list:
        split = line.split()[3]
        word_list.append(split)
    return "".join(word_list)


def process_v4(line_list):
    """Same as process_v3, but this time using a list comprehension instead of a regular for loop."""
    word_list = []
    word_list = [line.split()[3] for line in line_list]
    return "".join(word_list)


def search_v1(word_list, term="prosecuted"):
    """Checks if term in list, returns index of that term within list."""
    if term in word_list:
        return word_list.index(term)


def search_v2(word_list, term="prosecuted"):
    """Checks if term in list, returns boolean."""
    if term in word_list:
        return True


def search_v3(word_list):
    """Find index in list for given term and returns term."""
    index = word_list.index("prosecuted")
    return word_list[index]


def search_v4(word_list, term="prosecuted"):
    """Checks for term in set of list, returns boolean."""
    if term in set(word_list):
        return True


def back_to_the_future_process(iterations, function):
    """Duration tests by iteration of process functions."""
    print("\n{}-maliger AUFRUF von ’{}’".format(iterations, function))
    start = time.time()
    for i in range(int(iterations)):
        function(line_list)
    end = time.time()
    print(" -> TIME: ’{}’ sec.".format(end - start))


def back_to_the_future_search(iterations, function):
    """Duration tests by iteration of search functions."""
    word_list = [line.split()[3] for line in line_list]

    print("\n{}-maliger AUFRUF von ’{}’".format(iterations, function))
    start = time.time()
    for i in range(int(iterations)):
        function(word_list)
    end = time.time()
    print(" -> TIME: ’{}’ sec.".format(end - start))


if __name__ == "__main__":

    line_list = extract_words(sys.argv[1])
    iterations = sys.argv[2]
    functions_process = [process_v1, process_v2, process_v3, process_v4]
    functions_search = [search_v1, search_v2, search_v3, search_v4]

    for function in functions_process:
        back_to_the_future_process(iterations, function)

    for function in functions_search:
        back_to_the_future_search(iterations, function)


"""

1) Sets enthalten keine Duplikate, sind ungeordnet, und Werte werden einem hash zugewiesen. Listen können Duplikate enthalten, sind geordnet, und werden per index sortiert.

2) Die suche nach einem hash hat die Geschwindigkeit O(1), da Python nur schauen muss, ob das Objekt vom angegebenen Hash im set existiert. Listen haben die Geschwindigkeit von O(n), über die Liste von Anfang an iteriert werden muss, bis das gesuchte Element gefunden wird.

3) Die methode .join ist schneller, da einfach alle Listenelemente aneinandergehängt werden, anstatt dass jedes mal bei der Konkatenation die Liste kopiert und der neue Teil angefügt wird.

4) Dasselbe Problem existiert bei Listen, lässt sich jedoch mittels erweiterter Zuweisung reduzieren.


"""
