#!/usr/bin/env python3

"""Übung zur Umwandlung von Einzeilern zu Mehrzeilern und umgekehrt.

- zu implementieren: multiliner_1(), multiliner_2(), oneliner_3()
- zu dokumentieren: alle "oneliners" (1, 2, 3)

Author:

"""


import checker


def oneliner_1():
    # TODO: DocString
    return str(int(input("Geben Sie eine Zahl: ")) * int(input("Geben Sie eine zweite Zahl: ")))


def multiliner_1():
    # TODO: implementation
    pass


def oneliner_2(mystring):
    # TODO: DocString
    return "\n".join(mystring.replace("ist", "war").split()).upper()


def multiliner_2(mystring):
    # TODO: implementation
    pass


def multiliner_3(text):
    normalized_text = text.lower()
    char_list = list(normalized_text)
    char_set = set(char_list)
    char_type_list = list(char_set)
    sorted_char_type_list = sorted(char_type_list)
    return sorted_char_type_list


def oneliner_3(text):
    # TODO: DocString and implementation
    pass
    


if __name__ == "__main__":
    mystring_candidate_1 = "Heute ist das Wetter so schön."

    # Gebrüder Grimm: Kinder- und Hausmärchen, große Ausgabe, Band 1, 1850; https://maerchen.com/grimm/jorinde-und-joringel.php
    mystring_candidate_2 = """Jorinde und Joringel

    Es war einmal ein altes Schloß mitten in einem großen dicken Wald, darinnen wohnte eine alte Frau ganz allein, das war eine Erzzauberin. Am Tage machte sie sich zur Katze oder zur Nachteule, des Abends aber wurde sie wieder ordentlich wie ein Mensch gestaltet. Sie konnte das Wild und die Vögel herbei locken, und dann schlachtete sies, kochte und briet es. Wenn jemand auf hundert Schritte dem Schloß nahe kam, so mußte er stille stehen und konnte sich nicht von der Stelle bewegen, bis sie ihn los sprach: wenn aber eine keusche Jungfrau in diesen Kreiß kam, so verwandelte sie dieselbe in einen Vogel, und sperrte sie dann in einen Korb ein, und trug den Korb in eine Kammer des Schlosses. Sie hatte wohl sieben tausend solcher Körbe mit so raren Vögeln im Schlosse.
    Nun war einmal eine Jungfrau, die hieß Jorinde: sie war schöner als alle andere Mädchen. Die, und dann ein gar schöner Jüngling, Namens Joringel, hatten sich zusammen versprochen. Sie waren in den Brauttagen und sie hatten ihr größtes Vergnügen eins am andern. Damit sie nun einsmalen vertraut zusammen reden könnten, giengen sie in den Wald spazieren. 'Hüte dich,' sagte Joringel, 'daß du nicht so nahe ans Schloß kommst.' Es war ein schöner Abend, die Sonne schien zwischen den Stämmen der Bäume hell ins dunkle Grün des Waldes, und die Turteltaube sang kläglich auf den alten Maibuchen.
    Jorinde weinte zuweilen, setzte sich hin im Sonnenschein und klagte; Joringel klagte auch. Sie waren so bestürzt, als wenn sie hätten sterben sollen: sie sahen sich um, waren irre und wußten nicht wohin sie nach Hause gehen sollten. Noch halb stand die Sonne über dem Berg und halb war sie unter. Joringel sah durchs Gebüsch und sah die alte Mauer des Schlosses nah bei sich; er erschrack und wurde todtbang. Jorinde sang

    'mein Vöglein mit dem Ringlein roth
    singt Leide, Leide, Leide:
    es singt dem Täubelein seinen Tod,
    singt Leide, Lei - zucküth, zicküth, zicküth.'

    """  # ... Der Text geht noch weiter.
    
    print("AUFRUF 1")
    print(checker.check_equality(oneliner_1(), multiliner_1()))  # bitte die gleichen Zahlenpaare angeben
    print()
    print("AUFRUF 2")
    print(checker.check_equality(oneliner_2(mystring_candidate_1), multiliner_2(mystring_candidate_1)))
    print()
    print("AUFRUF 3")
    print(checker.check_equality(oneliner_3(mystring_candidate_2), multiliner_3(mystring_candidate_2)))

