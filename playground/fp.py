from functools import wraps
from inspect import getargspec

def times2 (x): return x * 2
def by3 (x): return x / 3
def square (x): return x * x

def compose2 (fnB, fnA):
  return lambda arg: fnB(fnA(arg))

def compose (fns):
  return reduce(compose2, fns)

composed = compose2(square, by3)

@wraps(filter)
def onlyBy3 (lo, hi): return filter(lambda x: x % 3 == 0, range(lo, hi))

def arg_len (fn): return len(getargspec(compose2)[0])
def curry(fn):
  args = getargspec(fn)[0]
  print(args)
"""print(arg_len(compose2))"""

curry(compose2)
