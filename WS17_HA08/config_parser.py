#! /usr/bin/env python3

# -----------------------------------
# Version: 0.0.1
# Author: Jan Wirth
# Description: Interactive Config parser
# -----------------------------------
"""This script reads and parses .ini files by standard format, then gives the user an option to explore sections, followed by their comments and key: value pairs. The argument after the module name should be the file name of the .ini file you would like to read."""

from sys import argv

global allsections
allsections = []

class Section():

  def __init__(self, name, comment, content):
    self.name = name
    self.comment = comment
    self.content = content

  def get_name(self):
    return (self.name)

  def get_comment(self):
    return (self.comment)

  def get_args(self):
    for i in self.content.keys():
      print(f"{i} : {self.content[i]}")

def read_config(filename):
  """Reads config file and divides sections by section names."""
  with open(filename) as open_file:
    sections = open_file.read().split("\n\n")

  for section_data in sections:
    if section_data[0].startswith("["):
      allsections.append(sectionize(section_data))
  return

def wert(wert):
  """Checks and converts data from string to int or string to float if necessary."""
  try:
    return int(wert)
  except ValueError:
    try:
      return float(wert)
    except ValueError:
      return wert

def sectionize(section_data):
  """Takes information from read_config() and creates an instance of Sections() for each block, then adds the relevant information to that instance."""
  section_lines = [i for i in section_data.split("\n") if i]
  section_name = ""
  section_comment = ""
  content_dictionary = {}

  for item in section_lines:
    if item.startswith("["):
      section_name = item
    elif item.startswith("#") or item.startswith(";"):
      section_comment = item
    else:
      if len(item.split("=")) == 2:
        content_dictionary[item.split("=")[0].strip()] = wert(item.split("=")[1].strip())
      elif len(item.split(":")) == 2:
        content_dictionary[item.split(":")[0].strip()] = wert(item.split(":")[1].strip())
      else:
        content_dictionary[item] = ""

  return Section(section_name, section_comment, content_dictionary)

if __name__ == "__main__":
  read_config(argv[1])
  for i in range(len(allsections)):
    print(f"Press {i} to see contents of {allsections[i].get_name()}.")
  ask_section = int(input(""))
  print(f"You have chosen {allsections[ask_section].get_name()}")
  option = input("Press 1 for comment and 2 for content.")
  if option =="1":
    print(allsections[ask_section].get_comment())
  else:
    allsections[ask_section].get_args()
