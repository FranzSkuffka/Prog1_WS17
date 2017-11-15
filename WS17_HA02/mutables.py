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
    objects = set()
    variableNames = set()

    print(1)
    liste1 = []                         # 1
    print(("liste1 after 1", liste1))
    variableNames.add("liste1")
    objects.add(id(liste1))
    

    print(2)
    liste1.append(1)                    # 2
    print(("liste1 after 2", liste1))
    variableNames.add("liste1")
    objects.add(id(liste1))
    

    print(3)
    s = "2"                             # 3
    print(("s after 3", s))
    variableNames.add("s")
    objects.add(id(s))
    

    print(4)
    liste1.append(s)                    # 4
    print(("liste1 after 4", liste1))
    variableNames.add("liste1")
    objects.add(id(liste1))
    

    list_internal = list(range(2, 5))   # 5
    print(("list_internal after 5", list_internal))
    variableNames.add("list_internal")
    objects.add(id(list_internal))
    

    print(6)
    liste1.append(list_internal)        # 6
    print(("liste1 after 6", liste1))
    variableNames.add("liste1")
    objects.add(id(liste1))
    

    print(7)
    liste1.append(6)                    # 7
    print(("liste1 after 7", liste1))
    variableNames.add("liste1")
    objects.add(id(liste1))
    

    print(8)
    liste2 = liste1                     # 8
    print(("liste2 after 8", liste2))
    variableNames.add("liste2")
    objects.add(id(liste2))
    

    print(9)
    liste1.append(7)                    # 9
    print(("liste1 after 9", liste1))
    variableNames.add("liste1")
    objects.add(id(liste1))


    print(("liste2 after 9", liste2))
    variableNames.add("liste2")
    objects.add(id(liste2))
    

    print(10)
    s += "2"                            # 10
    print(("s after 10", s))
    variableNames.add("s")
    objects.add(id(s))
    
    print(("liste1 after 10", liste1))
    variableNames.add("liste1")
    objects.add(id(liste1))
    

    print(11)
    list_internal.append(55)            # 11
    print(("list_internal after 11", list_internal))
    variableNames.add("list_internal")
    objects.add(id(list_internal))
    
    print(("liste1 after 11", liste1))
    variableNames.add("liste1")
    objects.add(id(liste1))
    

    print(12)
    liste2.remove(1)                    # 12 remove() ist eine Listenfunktion, sie entfernt das im Argument angegebene Element von der Liste
    print(("liste1 after 12", liste1))
    variableNames.add("liste1")
    objects.add(id(liste1))
    
    print(("liste2 after 12", liste2))
    variableNames.add("liste2")
    objects.add(id(liste2))
    

    print(13)
    del liste2                          # 13 del löscht das angegebene Objekt aus dem Namensraum
    try:
      print(("liste2 after 13", liste2))
      variableNames.add("liste2")
      objects.add(id(liste2))
    
    except UnboundLocalError:
      print(("liste2 after 13", UnboundLocalError))
    
      print(("liste1 after 13", liste1))
      variableNames.add("liste1")
      objects.add(id(liste1))
    

    
    """FRAGEN:
    
    - Wie viele neue Objekte und wie viele neue Variablennamen wurden in der Funktion insgesamt erzeugt? Anhand welcher Eigenschaft kann man die Anzahl der Objekte nachvollziehen?
        ANTWORT: neue Objekte: """; print(objects) ;""" -> {4523641608, 4523757896, 4523809400, 4523851464}
                 neue Namen: """; print(variableNames) ;""" -> {'liste2', 'liste1', 's', 'list_internal'}
                 Erzeugung neuer Objekte nachvollziehbar durch:
                   Sets, sie sind wie listen, nur dass jedes object nur einmal vorkommen darf.

    - Listen Sie die veränderbaren und unveränderbaren Datentypen auf, die in der Funktion verwendet wurden.
        ANTWORT: VERÄNDERBAR: list
                 UNVERÄNDERBAR: string, integer, set, range

    - Wie viele Elemente hat
     * liste1 nach #7? ANTWORT: len([1, '2', [2, 3, 4], 6]) -> 4
     * liste2 nach #9: ANTWORT: [1, '2', [2, 3, 4], 6, 7] -> 5


    - Wie sieht das angegebene Objekt aus?

     * list_internal nach #5: ANTWORT:
     * ('list_internal after 5', [2, 3, 4])

     * liste1 nach #6:  ANTWORT: [1, '2', [2, 3, 4]]
     * ('liste1 after 6', [1, '2', [2, 3, 4]])

     * liste1 nach #10: ANTWORT:
     * ('liste1 after 10', [1, '2', [2, 3, 4], 6, 7])

     * liste1 nach #11: ANTWORT:
     * ('liste1 after 11', [1, '2', [2, 3, 4, 55], 6, 7])

     * liste1 nach #12: ANTWORT:
     * ('liste1 after 12', ['2', [2, 3, 4, 55], 6, 7])

     * liste2 nach #12: ANTWORT:
     * ('liste2 after 12', ['2', [2, 3, 4, 55], 6, 7])

     * liste1 nach #13: ANTWORT:
     * ('liste1 after 13', ['2', [2, 3, 4, 55], 6, 7])



    - Warum haben #10 und #11 unterschiedliche Auswirkungen auf liste1?

     * Grund des Unterschieds:

     * Auswirkung von #10 auf liste1:
     * int is an immutable primitive literal.
     * list.add(s) adds a reference to '3', not to s.
     * s+= "2" is shorthand for s = s + '3' . Note that s + '3' is an expression, not an operation on the value of s

     * Auswirkung von #11 auf liste1:
     * also here not the reference but the value was passed.
     * list_internal.append(55) mutates the value inside, which is also referenced in liste1



    - Wie verhält sich liste2 ab #8 zu liste1? Was passiert bei Änderungen am liste1 oder am liste2?
    - Warum kann man nach #13 auf liste1 zugreifen?
       Also here both variables reference the same value.
       del deletes the reference between the variable liste2 and it's value.
       del liste1 would cause the the value to be garbage collected because no variables reference to it anymore.
    """
check_mutables()
