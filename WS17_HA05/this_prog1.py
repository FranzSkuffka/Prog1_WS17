#!/usr/bin/env python3
#
from checker_emm import check_equality

"""Hausaufgabe für Prog1_WS17 HA05

AUFGABEN:

- Erklären Sie die Funktion this_v1() mit Ihren eigenen Worten in einem DocString zu this_v1(): Was sind Ein- und Rückgaben, was und wie passiert mit der Eingabe?
 * Erklären Sie dabei jede Zeile in this_v1() mit mind. einem Satz. Zusätzlich zum DocString kann man gerne zu jedem Zeile einen Kommentar verfassen.
 * Zusätzlich sollte eine Ausgabe jeder Laufvariablen c und i mit dem aktuellen Schlüssel und Wert in der inneren Schleife erfolgen.

- Schreiben Sie die funktion this_v1() in Funktion this_maximallong() neu, wobei Sie möglichst viele komplexen Ausdrücke in einzelne einfache auftrennen.
 * Diese Teilaufgabe kann auch bei der Beantwortung der obigen Teilaufgabe helfen.
 * Wenn Sie eine Variable definieren, wählen Sie dafür einen sinnvollen Namen.
 * z.B. statt einer Zeile
        int("4") + 1
   könnte man drei schreiben:
        mystringint = "4"           #Zuweisung -> Variable statt Literal
        myint = int(mystringint)    #Umwandlung str->int
        result = myint + 1          #Wert erhöhen, Ergebnis in einer (neuen) Variable speichern


- Gestalten Sie einen Main-Block, in dem Sie einen Aufruf beider Funktionen gestalten, und die Rückgabewerte verglichen werden.
 * Importieren und verwenden Sie dazu Ihre Implementation des checker-Moduls aus HA04. Alternativ können Sie auch die beigefügte Version checker_emm.py einsetzen.


Autor: ...
"""


s = """Gur Mra bs Clguba, ol Gvz Crgref

Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyrk.
Pbzcyrk vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcnefr vf orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orngf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""


def this_v1(mystring):
    """Decrypt a multiline ALbAM encrypted string"""
    d = {} # create a dict that maps the encrypted char onto the decrypted equivalent
    for c in (65, 97): # uppercase & lowercase chars
        print('c ' + str(c))
        for i in range(26):
            print('i ' + str(i))
            d[chr(i + c)] = chr((i + 13) % 26 + c) # module to check if index exceeds alphabet boundaries
    
    return "".join([d.get(c, c) for c in mystring])


def this_maximallong(mystring):
    d = {}
    for c in (65, 97):
        for i in range(26):
            shifted = i + 13
            rest = shifted % 26
            shifted_case = rest + c
            decrypted = chr(shifted_case)
            key = chr(i + c)
            d[key] = decrypted

    res_chars = []
    for c in s:
        source_from_dict = d.get(c, c)  # fallback to c if key is not found in dict
        res_chars.append(source_from_dict)
    output = "".join(res_chars)
    return output


if __name__ == "__main__":
    print(check_equality(this_v1(s), this_maximallong(s)))
