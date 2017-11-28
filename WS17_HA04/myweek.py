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

def query_calendar():
  registry = read_calendar()
  query = input('Which day? ').strip('')
  try:
    print(registry[query])
    query_calendar()
  except KeyError:
    return


def main():
  query_calendar()

if __name__ == "__main__":
  main()
