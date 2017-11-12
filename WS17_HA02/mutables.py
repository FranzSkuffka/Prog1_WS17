#!/usr/bin/env python3

"""Übung zu veränderbaren Objekten, hier auf Listen konzentriert.

Hauptfrage: Wie werden veränderbare und unveränderbare Objekte geändert?
"""

"""VORÜBUNG:
- Führen Sie die einzelnen Anweisungen in check_mutables() im Python-Interpreter aus,
- und lassen Sie immer wieder die einzelnen Objekte anzeigen.
- Vollziehen Sie Schritt-für-Schritt nach, was mit den Objekten passiert.
"""


def check_mutables():
    """Anweisungssequenz zum Üben der Änderungen von Listen"""
    
    liste1 = []                         # 1
    liste1.append(1)                    # 2
    s = "2"                             # 3
    liste1.append(s)                    # 4
    list_internal = list(range(2, 5))   # 5
    liste1.append(list_internal)        # 6
    liste1.append(6)                    # 7
    liste2 = liste1                     # 8
    liste1.append(7)                    # 9
    s += "2"                            # 10
    list_internal.append(55)            # 11
    liste2.remove(1)                    # 12 remove() ist eine Listenfunktion, sie entfernt das im Argument angegebene Element von der Liste
    del liste2                          # 13 del löscht das angegebene Objekt aus dem Namensraum
    
    """FRAGEN:
    
    - Wie viele neue Objekte und wie viele neue Variablennamen wurden in der Funktion insgesamt erzeugt? Anhand welcher Eigenschaft kann man die Anzahl der Objekte nachvollziehen?
        ANTWORT: neue Objekte:
                 neue Namen:
                 Erzeugung neuer Objekte nachvollziehbar durch:

    - Listen Sie die veränderbaren und unveränderbaren Datentypen auf, die in der Funktion verwendet wurden.
        ANTWORT: VERÄNDERBAR:
                 UNVERÄNDERBAR:

    - Wie viele Elemente hat
     * liste1 nach #7? ANTWORT:
     * liste2 nach #9: ANTWORT:

    - Wie sieht das angegebene Objekt aus?
     * list_internal nach #5: ANTWORT:
     * liste1 nach #6:  ANTWORT:
     * liste1 nach #10: ANTWORT:
     * liste1 nach #11: ANTWORT:
     * liste1 nach #12: ANTWORT:
     * liste2 nach #12: ANTWORT:
     * liste1 nach #13: ANTWORT:

    - Warum haben #10 und #11 unterschiedliche Auswirkungen auf liste1?
     * Auswirkung von #10 auf liste1: ANTWORT:
     * Auswirkung von #11 auf liste1: ANTWORT:
     * Grund des Unterschieds: ANTWORT:

    - Wie verhält sich liste2 ab #8 zu liste1? Was passiert bei Änderungen am liste1 oder am liste2?
       ANTWORT:

     * Warum kann man nach #13 auf liste1 zugreifen?
       ANTWORT:

    """
