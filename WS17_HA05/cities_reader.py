""" A tool for querying city data """
__author__      = "Jan Wirth <contact@jan-wirth.de"
__version__     = "0.0.1"

id = lambda x: x

def checkType(cons, val):
  try:
    return type(cons(val)) == type(cons())
  except ValueError:
    return False

def isValid(entry):
  try:
    return (checkType(str, entry[0])
    and checkType(int, entry[1])
    and checkType(float, entry[2])
    and checkType(str, entry[3]))
  except IndexError:
    return False

def makeOperable(entry):
  return [entry[0], int(entry[1]), float(entry[2]), entry[3]]

def compare(cities, aName, bName):
  try:
    a = next(c for c in cities if c[0].lower() == aName.lower())
  except StopIteration:
    return print('Can not compare because ' + aName + ' was not found')
  try:
    b = next(c for c in cities if c[0].lower() == bName.lower())
  except StopIteration:
    return print('Can not compare because ' + bName + ' was not found')

  print('Comparing ' + a[0] + ' to ' + b[0])
  if (a[3] == b[3]):
    print('Both cities are in the same state')

  if (a[1] > b[1]):
    print(a[0] + ' has a higher population')
  else:
    print(b[0] + ' has a higher population')

  if (a[2] > b[2]):
    print(a[0] + ' is bigger')
  else:
    print(b[0] + ' is bigger')
  print()

def read():
  lines = open('cities_corrupted.tsv', 'r').read().splitlines()
  raw_entries = map(lambda line: line.split('\t'), filter(lambda line: not line.startswith('#'), lines))
  return list(map(makeOperable, filter(isValid, raw_entries)))

def main():
  cities = read()
  aName = input('First city to compare: ')
  bName = input('First city to compare: ')
  print()
  compare(cities, aName, bName)
  #compare(cities, 'Ulm', 'Bonn')
  #compare(cities, 'Moers', 'Bonn')
  #compare(cities, 'Moers', 'Gibtsnich')

if __name__ == "__main__":
  main()
