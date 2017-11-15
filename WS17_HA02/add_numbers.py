#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


""" Prompt for two numbers and print the sum of the range that spans between them """
__author__      = "Jan Wirth <contact@jan-wirth.de"
__version__     = "0.0.1"

from functools import reduce


def sum_from_to(a, b):
  """ recursively sums the inclusive range between two numbers """
  return reduce(lambda a, b: a + b, list(range(a, b + 1))) # range top is not inclusive

def user_input(msg):
  try:
    return int(input(msg))
  except ValueError:
    print('')
    return user_input(msg)

def main():

  a = user_input('Type the first numba\n')
  print('')

  b = user_input('Type the second numbaaa\n')
  print('')

  if (a > b):
    print('ERROR: The second number should be equal or greater to the first one.\n')
    main()
  else:
    print('RESULT')
    print(sum_from_to(a, b))

if __name__ == "__main__":
  main()

"""
– Funktion user_input(str promt) -> int2 soll mit der im Argument ange- gebenen Prompt-Anfrage nach einer ganzen Zahl fragen und diese als Integer zurückgeben.3
– Funktion sum_from_to(int from_int, int to_int) -> int soll zwei Inte- gers als Argumente nehmen, und einen Integer zurückgeben, wobei der Rückga- bewert das aufsummierte Ergebnis der Zahlfolge zwischen den beiden Eingabe- zahlen sein soll (beide Zahlen inklusive).
– Beide Funktionen sollten mit je einem DocString versehen werden, der über die Funktionalität und Eingabe bzw. Rückgabe der Funktion berichtet.
– Der Main-Teil – eingerückger Block nach einer Zeile if __name__ == "__main__":
– soll mithilfe der beiden geschriebenen Funktionen sowie weiteren Anweisungen und Kontrollstrukturen so gestaltet werden, dass zwei Ganzzahlen eingelesen werden, welche für die Berechnung der Aufsummierung mit sum_from_to() dienen. Das Ergebnis soll ausgegeben werden.
– Wird als zweite Zahl eine kleinere Zahl als die erste vom Benutzer (Sie) ein- gegeben, soll keine Berechnung erfolgen, sondern der Benutzer soll von den erwarteten Eingaben informiert werden.
– Testen Sie Ihr Programm mit unterschiedlichen Zahlen.
"""
