#!/usr/bin/env python3

""" Examine immutable data types """
__author__      = "Jan Wirth <contact@jan-wirth.de"
__version__     = "0.0.1"


"""Übung zu veränderbaren und unveränderbaren Objekten.

Hauptfrage: Wie werden veränderbare und unveränderbare Objekte geändert?
"""


"""Kopie aus dem Python-Interpreter
Vorübung: Führen Sie diese oder ähnliche Anweisungen durch, und vollziehen Sie die Rückgabewerte nach.
"""
"""
i = 42
id(i)
# 4297638208
i = list(range(3))
i
# [0, 1, 2]
id(i)
# 4339799816
j = "ABBA"
id(j)
# 4339792560
j = j+"C"
j
# 'ABBAC'
id(j)
# 4339792504
k = 4
id(k)
# 4297636992

t = (i, j, k)
t
# ([0, 1, 2], 'ABBAC', 4)
id(t)
# 4339803336

i.append(3)
i
# [0, 1, 2, 3]
id(i)
# 4339799816
t
# ([0, 1, 2, 3], 'ABBAC', 4)
id(t)
# 4339803336
j += "AT"
t
# ([0, 1, 2, 3], 'ABBAC', 4)
id(t)
# 4339803336
k = 5
t
# ([0, 1, 2, 3], 'ABBAC', 4)
id(k)
# 4297637024
"""


def check_immutables():
    """ Anweisungssequenz zum Üben der Änderung einiger unveränderbarer Datentypen """
    objects = set()
    variableNames = set()

    #1
    # print('i Before 1' + str(type(i)) + str(id(i)))
    i = 42              
    variableNames.add('i')
    objects.add(id(i))
    print('i After 1' + str(type(i)) + str(id(i)))

    #2
    # print('i Before 2' + str(type(i)) + str(id(i)))
    i = list(range(3))  
    variableNames.add('i')
    objects.add(id(i))
    print('i After 2' + str(type(i)) + str(id(i)))

    #3
    # print('j Before 3' + str(type(j)) + str(id(j)))
    j = "ABBA"          
    variableNames.add('j')
    objects.add(id(j))
    print('j After 3' + str(type(j)) + str(id(j)))

    #4
    # print('j Before 4' + str(type(j)) + str(id(j)))
    j = j + "C"         
    variableNames.add('j')
    objects.add(id(j))
    print('j After 4' + str(type(j)) + str(id(j)))

    #5
    # print('k Before 5' + str(type(k)) + str(id(k)))
    k = 4               
    variableNames.add('k')
    objects.add(id(k))
    print('k After 5' + str(type(k)) + str(id(k)))

    #6
    # print('t Before 6' + str(type(t)) + str(id(t)))
    t = (i, j, k)       
    variableNames.add('t')
    objects.add(id(t))
    print('t After 6' + str(type(t)) + str(id(t)))

    #7 append() ist eine Listenfunktion, und hängt ein weiteres Element an die Liste
    # print('i Before 7' + str(type(i)) + str(id(i)))
    i.append(3)         
    variableNames.add('i')
    objects.add(id(i))
    print('i After 7' + str(type(i)) + str(id(i)))

    print('i', i)
    print('j', j)
    print('j', j)
    print('k', k)
    print('t', t)

    print('')
    print('OBJECTS')
    print(objects)
    print(len(objects))

    print('')
    print('VARIABLENAMES')
    print(variableNames)
    print(len(variableNames))

    
    """FRAGEN:
    
    - Wie viele neue Objekte und wie viele neue Variablennamen wurden in der Funktion insgesamt erzeugt? Anhand welcher Eigenschaft kann man die Anzahl der Objekte nachvollziehen?
        ANTWORT: neue Objekte: 6
                 neue Namen: 4
                 Erzeugung neuer Objekte nachvollziehbar durch: Ein set mit der ID des objekts nach jeder operation
    
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

check_immutables()
