#!/usr/bin/env python3

"""Übung zu veränderbaren und unveränderbaren Objekten.

Hauptfrage: Wie werden veränderbare und unveränderbare Objekte geändert?
"""


"""Kopie aus dem Python-Interpreter
Vorübung: Führen Sie diese oder ähnliche Anweisungen durch, und vollziehen Sie die Rückgabewerte nach.

>>> i = 42
>>> id(i)
4297638208
>>> i = list(range(3))
>>> i
[0, 1, 2]
>>> id(i)
4339799816
>>>
>>> j = "ABBA"
>>> id(j)
4339792560
>>> j = j+"C"
>>> j
'ABBAC'
>>> id(j)
4339792504
>>>
>>> k = 4
>>> id(k)
4297636992
>>>
>>> t = (i, j, k)
>>> t
([0, 1, 2], 'ABBAC', 4)
>>> id(t)
4339803336
>>>
>>> i.append(3)
>>> i
[0, 1, 2, 3]
>>> id(i)
4339799816
>>> t
([0, 1, 2, 3], 'ABBAC', 4)
>>> id(t)
4339803336
>>> j += "AT"
>>> t
([0, 1, 2, 3], 'ABBAC', 4)
>>> id(t)
4339803336
>>> k = 5
>>> t
([0, 1, 2, 3], 'ABBAC', 4)
>>> id(k)
4297637024

"""


def check_immutables():
    """ Anweisungssequenz zum Üben der Änderung einiger unveränderbarer Datentypen """
    
    i = 42              #1
    i = list(range(3))  #2
    j = "ABBA"          #3
    j = j + "C"         #4
    k = 4               #5
    t = (i, j, k)       #6
    i.append(3)         #7 append() ist eine Listenfunktion, und hängt ein weiteres Element an die Liste
    
    """FRAGEN:
    
    - Wie viele neue Objekte und wie viele neue Variablennamen wurden in der Funktion insgesamt erzeugt? Anhand welcher Eigenschaft kann man die Anzahl der Objekte nachvollziehen?
        ANTWORT: neue Objekte:
                 neue Namen:
                 Erzeugung neuer Objekte nachvollziehbar durch:
    
    - Listen Sie die veränderbaren und unveränderbaren Datentypen auf, die in der Funktion für die Variablen verwendet wurden.
        ANTWORT: VERÄNDERBAR:
                 UNVERÄNDERBAR:
    
    - Was ist der Datentyp von
     * i nach #2? ANTWORT:
     * j nach #4: ANTWORT:
     * t nach #7: ANTWORT:
    
    - Wie sieht t nach #6 und #7 aus?
     * nach #6: ANTWORT:
     * nach #7: ANTWORT:
     * Warum konnte eine Änderung durchgeführt werden?
       ANTWORT:
     * Wie würde t nach folgender Anweisung aussehen?
       k += 1
       ANTWORT:
    
    """

