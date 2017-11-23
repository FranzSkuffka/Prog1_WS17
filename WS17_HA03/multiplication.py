#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


"""
Prompt for two numbers and print their products as calculated using different algorithms.
The algorithms have been adjusted and tested to work with arbitrary combinations of positive and negative integers.
Note: The algorithms are very slow for large numbers.
"""
__author__      = "Jan Wirth <contact@jan-wirth.de"
__version__     = "0.0.1"

def user_input(msg):
  """ Asks the user for input and only accepts integers """
  try:
    return int(input(msg))
  except ValueError:
    print('Please type a single number')
    print('')
    return user_input(msg)
  except SyntaxError:
    print('Please type a single number')
    print('')
    return user_input(msg)

def multiply_builtin(a, b):
  """ Multiplies two numbers using the built-in multiplication function """
  return a * b

def multiply_while(a, b):
  """ Multiplies two numbers using a while loop """
  i = 0
  sum = 0
  while i < abs(b):
    sum += a
    i += 1
  if (b > 0):
    return sum
  else:
    return -sum

def multiply_for(a, b):
  """ Multiplies two numbers using a for loop. """
  sum = 0
  for i in range(0, abs(b)):
    sum += a
  if (b > 0):
    return sum
  else:
    return -sum

def main():
  """ run the entire program """

  a = user_input('Type the first numba\n')
  print('')

  b = user_input('Type the second numbaaa\n')
  print('')

  # Reverse argument order to prevent
  print_res(a, b)

def print_res(a, b):
    print('RESULT')
    print()
    print('result using builtin')
    print(multiply_builtin(a, b))
    print()
    print('result using for')
    print(multiply_for(a, b))
    print()
    print('result using while')
    print(multiply_while(a, b))

if __name__ == "__main__":
  main()
