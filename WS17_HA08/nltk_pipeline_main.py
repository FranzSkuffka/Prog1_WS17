#!/usr/bin/env python3

"""NLTK-Pipeline zur Verarbeitung englischsprachiger Texte.

Aufruf: python nltk_pipeline_main.py <option> <eingabedatei> <ausgabedatei>
    <option>:   fct = ohne Klassenabbildung der Wörter
                cls = mit Abbildung der Wörter als Objekte
    <eingabedatei>:     Name der Eingabedatei mit einfachem Text
    <ausgabedatei>:     Name der Ausgabedatei

Verarbeitungsschritte:
- Satzsegmentierung
- Tokenisierung
- Wortartenerkennung
- Lemmatisierung

Annotationsformat:
- tabellarisches Format mit Annotationen zu jedem Token (Wort) je Zeile
- die Annotationsebenen zum aktuellen Token werden durch je einen Tabulator getrennt
- Sätze werden durch eine leere Zeile voneinander getrennt.
- Schematische Darstellung der Annotationsebenen in einer Zeile (für ein Token):

<satzindex>\t<tokenindex>\t<token>\t<lemma>\t<wortart>

Auszug aus einer möglichen Ausgabedatei:
...
531	0	She	She	PRP
531	1	is	be	VBZ
531	2	blowing	blow	VBG
531	3	a	a	DT
531	4	kiss	kiss	NN
531	5	to	to	TO
531	6	everyone	everyone	NN
531	7	.	.	.

Author: emm, mujdricza@cl.uni-heidelberg.de
Version: 20171226
"""

import nltk
import os
import sys

import nltk_pipeline_fct as fctanno
import nltk_pipeline_cls as clsanno


def main_pipeline_fct(input_filename, output_filename, language="english"):
    """Aufruf der Annotations-Pipeline mit funktionsbasierter Implementation"""
    sentences = fctanno.annotate_corpus_with_nltk_pipeline(input_filename, language)
    print(f"{len(sentences)} gelesen ({input_filename})")
    fctanno.write_conll_format_output(output_filename, sentences)
    print(f"Annotierte Ausgabe geschrieben in '{output_filename}'")


def main_pipeline_cls(input_filename, output_filename, language="english"):
    """Aufruf der Annotations-Pipeline mit klassenbasierter Implementation für Wörter"""
    sentences = clsanno.annotate_corpus_with_nltk_pipeline(input_filename, language)
    print(f"{len(sentences)} Sätze gelesen ({input_filename})")
    clsanno.write_conll_format_output(output_filename, sentences)
    print(f"Annotierte Ausgabe geschrieben in '{output_filename}'")


def __usage(msg):
    sys.exit(msg)


if __name__ == "__main__":
    
    option_dict = {
        "fct":"main_pipeline_fct",
        "cls":"main_pipeline_cls"
    }
    
    args = sys.argv
    if len(args) < 4:
        __usage(f"Fehlerhafter Aufruf!\n{__doc__}")
    
    option = args[1]
    input_fn = args[2]
    output_fn = args[3]
    
    if option in option_dict:
        chosen_function = globals()[option_dict[option]] # namensbasierter Zugriff auf die Funktion via globals()
        chosen_function(input_fn, output_fn) # Aufruf der Funktion entsprechend der gewählten Option
    else:
        __usage(f"Unbekannte Option '{option}'\n{__doc__}")

