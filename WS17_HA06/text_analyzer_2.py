#!/usr/bin/env python3

"""Das Skript liest eine Benutzerangabe (eine Zeile) interaktiv ein, und gibt eine kleine Wortstatistik über die Eingabe aus.

Die Statistik bezieht folgende Auswertungen ein:
- Anzahl der Wörter (Tokens) in der Eingabe
- Statistik über die Wortfrequenz mit bestimmter Wortlänge
- durchschnittliche Wortlänge

Zur Interpretation der Einheit 'Wort' (Token) werden zwei Optionen bereitgestellt:
- einfach (e): Eingabe wird an Leerzeichen aufgetrennt, d.h. alle Zeichen und zusammenhängende Zeichensequenzen außer beliebige Leerzeichen werden als 'Wort' interpretiert.
- heuristisch (h): wie "einfach", aber Satzzeichen am Anfang oder Ende eines Wortes werden nicht als Teil eines Wortes angesehen

Autor: Eva Mujdricza-Maydt (mujdricza@cl.uni-heidelberg.de), bearbeitet von Jan Wirth
Version: 20171123

Beispielaufruf:

$ python text_analyzer_emm.py
Bitte geben Sie einen Text ein:
Das ist der Text, den der Benutzer eingibt.

Wählen Sie eine Verarbeitungsoption:
- einfach (e) oder
- heuristisch (h):
e

Ergebnis:
Der Text enthält 8 Tokens:
['Das', 'ist', 'der', 'Text,', 'den', 'der', 'Benutzer', 'eingibt.']

Davon:
5 mit 3 Buchstaben
1 mit 5 Buchstaben
2 mit 8 Buchstaben

Die mittlere Wortlänge ist 4.5.

"""

import nltk

def _get_word_frequency_statistics(word_list):
    """Berechnet eine kleine Statistik über die Eingabeliste, und gibt die Ergebnisse aus.

    :param word_list: Wortliste
    :return: None
    """
    len_dict = {}
    char_count = 0
    for word in word_list:
        wordlen = len(word)
        len_dict.setdefault(wordlen, 0)
        len_dict[wordlen] += 1
        char_count += wordlen
    print("\nErgebnis:\nDer Text enthält {} Tokens:\n{}".format(len(word_list), word_list))
    print("\nDavon:")

    for charlen, freq in len_dict.items():
        print("{} mit {} Buchstaben".format(freq, charlen))

    avg_wordlen = 0
    if len(word_list):
        avg_wordlen = char_count / len(word_list)
    print("\nDie mittlere Wortlänge ist {}.".format(avg_wordlen))


def _tokenize_simple(text):
    """Tokenisiert den Eingabestring durch einfacher Auftrennung an Leerzeichen.

    :param text: ein String
    :return: Liste der Wörter
    """
    return text.strip().split()


def _tokenize_heuristic(text, punctuation):
    """Tokenisiert den Eingabestring durch eine einfache Heuristik: Wörter werden an Leerzeichen aufgetrennt, führende oder nachgestellte Satzzeichen werden von den Wörtern entfernt.

        :param text: ein String
        :param punctuation: Liste der Satzzeichen
        :return: Liste der Wörter
        """
    word_list_raw = text.strip().split()
    word_list = []
    for word in word_list_raw:
        word_list.append(word.strip(punctuation))
    return word_list


def analyze_text_simple(text):
    """Analysiert die Wörter des Eingabetexts mit einfacher Tokenisierung.

    :param text: Eingabetext
    :return: None
    """

    word_list = _tokenize_simple(text)
    _get_word_frequency_statistics(word_list)


def analyze_text_heuristic(text, punctuation=".,;!?"):
    """Analysiert die Wörter des Eingabetexts mit heuristischer Tokenisierung.

        :param text: Eingabetext
        :return: None
        """

    word_list = _tokenize_heuristic(text, punctuation)
    _get_word_frequency_statistics(word_list)

def analyze_text_nltk(text, language):
    """Analysiert die Wörter des Eingabetexts mit nltk Tokenisierung. Bei keiner language Angabe oder einer nicht gefundenen language wird die Standardsprache English gewählt."""

    if not language:
        print("Sie haben keine Sprache eingegeben. Standardsprache 'English' wird verwendet.")
        word_list = nltk.tokenize.word_tokenize(text)
        _get_word_frequency_statistics(word_list)
    else:
        try:
            word_list = nltk.tokenize.word_tokenize(text, language)
            _get_word_frequency_statistics(word_list)
        except LookupError as le:
            print("Die eingegebene Sprache steht leider nicht zur Verfügung. Standardsprache 'English' wird verwendet.")
            word_list = nltk.tokenize.word_tokenize(text)
            _get_word_frequency_statistics(word_list)


if __name__ == "__main__":

    text = input("Bitte geben Sie einen Text ein:\n")
    mode = input("\nWählen Sie eine Verarbeitungsoption:\n- einfach (e) oder\n- heuristisch (h) oder\n- nltk (n):\n ")

    if mode.startswith("e"):
        analyze_text_simple(text)
    elif mode.startswith("h"):
        analyze_text_heuristic(text)
    elif mode.startswith("n"):
        language = input("Sprache der Eingabe: ")
        analyze_text_nltk(text, language)
    else:
        print("Unbekannte Option: '{}'".format(mode))
