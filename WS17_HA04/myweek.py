#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


""" A basic cryptographer. Takes a word at a time."""
__author__      = "Jan Wirth <contact@jan-wirth.de"
__version__     = "0.0.1"

from time import sleep

def _input(msg):
  """
  a wrapper for `input`
  """
  return input(msg)

def _print(msg):
  """
  a wrapper for `print`
  """
  return print(msg)

def user_input(msg = ''):
  """ Ask user for an integer """
  try:
    return int(_input(msg))
  except ValueError:
    return user_input(msg)

def progress_status(size, speed):
  """ A generator that emulates the progress of updates after fixed length time steps. """
  step_size = speed / size * 100
  step = 0
  status = 0

  while status < 100:
    status = step_size * step
    step += 1
    if status <= 100:
      yield status
    elif status > 100:
      yield 100

def print_progress(percent):
  """ Prints a number as percent """
  _print(str(int(percent)) + '%')


def run_update(status_update):
  """
  Simulate an update to the computer given an iterator that returns the statuses from 0 - 100.
  The last status can be greater than but will be maxed to 100.
  """
  status = next(status_update)
  sleep(1)
  if status != 100:
    print_progress(status)
    run_update(status_update)
  elif status == 100:
    print_progress(100)
    _print('DONE')
    return

def main():
  update()

def update():
  """ Simulate an update to the computer """
  size = user_input('Update size: ')
  speed = user_input('Download speed: ')
  _print('Updating. Do not turn off your computer.'),
  progress = progress_status(size, speed)
  run_update(progress)

if __name__ == "__main__":
  main()
