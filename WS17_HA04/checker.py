#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

""" A basic week planner. Takes a day at a time."""
__author__      = "Jan Wirth <contact@jan-wirth.de"
__version__     = "0.0.1"

from time import sleep

def read_calendar():
  """ Reads a calendar from a string """
  register = dict()
  calendar = """Mo; Logik
Di; ECL-Tutorium; Prog1
Mi; ECL
Do; Prog1-Tutorium; ECL; Prog1 Fr
Sa; Englisch
So """
  days = calendar.split('\n')
  for day in days:
    dayName, *dayContents = day.split("; ")
    register[dayName] = dayContents
  return register

def check_equality(a, b):
  if a == b :
    print("SAME VALUE: " + a)
  else:
    print("DIFFERENT VALUES")
    print("FIRST: " + a)
    print("SECOND: " + b)


def main():
  first = input('First value: ').strip('')
  second = input('Second value: ').strip('')
  check_equality(first, second)

if __name__ == "__main__":
  main()
