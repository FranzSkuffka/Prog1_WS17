#!/usr/bin/env python3

"""Übung zur Umwandlung von Einzeilern zu Mehrzeilern und umgekehrt.

- zu implementieren: multiliner_1(), oneliner_2(), oneliner_3()
- zu dokumentieren: alle "oneliners" (1, 2, 3)

Author:

"""

import sys
import checker_emm as checker

def oneliner_1(mystring, given_char="e"):
    return [char for char in mystring].count(given_char)


def multiliner_1(mystring, given_char="e"):
    pass
    #TODO


def multiliner_2(text):
    filtered_lines = []
    line_list = text.splitlines()
    for line in line_list:
        cleared_line = line.strip()
        if cleared_line:
            filtered_lines.append(cleared_line)
    return filtered_lines


def oneliner_2(text):
    pass
    # TODO


def multiliner_3(text, query="Jorinde"):
    found_words = []
    word_list = text.split()
    for word in word_list:
        if word == query:
            found_words.append("+")
    count = len(found_words)
    return count


def oneliner_3(text, query="Jorinde"):
    pass
    # TODO


if __name__ == "__main__":
    # Gebrüder Grimm: Kinder- und Hausmärchen, große Ausgabe, Band 1, 1850; https://maerchen.com/grimm/jorinde-und-joringel.php
    mystring_candidate = """Jorinde und Joringel

Es war einmal ein altes Schloß mitten in einem großen dicken Wald, darinnen wohnte eine alte Frau ganz allein, das war eine Erzzauberin. Am Tage machte sie sich zur Katze oder zur Nachteule, des Abends aber wurde sie wieder ordentlich wie ein Mensch gestaltet. Sie konnte das Wild und die Vögel herbei locken, und dann schlachtete sies, kochte und briet es. Wenn jemand auf hundert Schritte dem Schloß nahe kam, so mußte er stille stehen und konnte sich nicht von der Stelle bewegen, bis sie ihn los sprach: wenn aber eine keusche Jungfrau in diesen Kreiß kam, so verwandelte sie dieselbe in einen Vogel, und sperrte sie dann in einen Korb ein, und trug den Korb in eine Kammer des Schlosses. Sie hatte wohl sieben tausend solcher Körbe mit so raren Vögeln im Schlosse.
Nun war einmal eine Jungfrau, die hieß Jorinde: sie war schöner als alle andere Mädchen. Die, und dann ein gar schöner Jüngling, Namens Joringel, hatten sich zusammen versprochen. Sie waren in den Brauttagen und sie hatten ihr größtes Vergnügen eins am andern. Damit sie nun einsmalen vertraut zusammen reden könnten, giengen sie in den Wald spazieren. 'Hüte dich,' sagte Joringel, 'daß du nicht so nahe ans Schloß kommst.' Es war ein schöner Abend, die Sonne schien zwischen den Stämmen der Bäume hell ins dunkle Grün des Waldes, und die Turteltaube sang kläglich auf den alten Maibuchen.
Jorinde weinte zuweilen, setzte sich hin im Sonnenschein und klagte; Joringel klagte auch. Sie waren so bestürzt, als wenn sie hätten sterben sollen: sie sahen sich um, waren irre und wußten nicht wohin sie nach Hause gehen sollten. Noch halb stand die Sonne über dem Berg und halb war sie unter. Joringel sah durchs Gebüsch und sah die alte Mauer des Schlosses nah bei sich; er erschrack und wurde todtbang. Jorinde sang

'mein Vöglein mit dem Ringlein roth
singt Leide, Leide, Leide:
es singt dem Täubelein seinen Tod,
singt Leide, Lei - zucküth, zicküth, zicküth.'

"""  # ... Der Text geht noch weiter.
    
    #Man kann auch eine andere Datei ins Programm laden, wenn man einen Dateinamen als Kommandozeilenargument angibt.
    args = sys.argv
    if len(args) > 1:
        input_filename = args[1]
        with open(input_filename) as f:
            mystring_candidate = f.read()
        print("Eingabedatei: {}\n".format(input_filename))
    
    print("AUFRUF 1")
    print(checker.check_equality(oneliner_1(mystring_candidate), multiliner_1(mystring_candidate)))
    print()
    print("AUFRUF 2")
    print(checker.check_equality(oneliner_2(mystring_candidate), multiliner_2(mystring_candidate)))
    print()
    print("AUFRUF 3")
    print(checker.check_equality(oneliner_3(mystring_candidate), multiliner_3(mystring_candidate)))