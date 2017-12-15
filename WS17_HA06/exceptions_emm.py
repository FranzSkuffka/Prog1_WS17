#!/usr/bin/env python3

"""Übung zur Erzeugung und Behandlung von Fehlern
Autor: Jan Wirth
"""

import sys

def provoke_and_handle_ModuleNotFoundError():
    """Handling for module not found errors. Tries to import a module that doesn't exist."""
    try:
        import arsiton324
    except ModuleNotFoundError as mnfe:
        print(f"Sorry! {mnfe} was found!")

def provoke_and_handle_KeyError():
    """Handling for key errors. Tries looking for a key which doesn't exist in given dictionary."""
    test_dict = {}
    try:
        print(test_dict['to life'])
    except KeyError as ke:
        print(f"Sorry! The key '{ke}' does not exist in test_dict!")

def provoke_and_handle_NameError():
    """Handling for name errors. Tries to print a variable which hasn't been defined."""
    try:
        print(bliblablub)
    except NameError as ne:
        print(f"Sorry! {ne}")

def provoke_and_handle_ZeroDivisionError():
    """Handling for zero divison errors. Tries to divide 3 by 0."""
    try:
        print(324/0)
    except ZeroDivisionError as zde:
        print(f"Sorry! {zde}")

def provoke_and_handle_SyntaxError():
    """Handling for syntax errors. Tries to call the eval function on a string."""
    try:
        eval("x === x")
    except SyntaxError as se:
        print(f"Sorry! You can't use eval in that way: {se}")

def provoke_and_handle_TypeError():
    """Handling for type errors. Tries to add and int to a string."""
    try:
        print("loetungdusohn" + 3)
    except TypeError as te:
        print(f"Sorry! {te}")

def provoke_and_handle_ImportError():
    """Handling for import errors. Tries to import from a module which doesn't exist."""
    try:
        from you import me
    except ImportError as impe:
        print(f"Sorry! {impe}")

def provoke_and_handle_FileNotFoundError():
    """Handling for file not found errors. Tries to open a file which doesn't exist."""
    try:
        with open("NEIN.mp3") as f:
            print("well")
    except FileNotFoundError as fnfe:
        print(f"Sorry! {fnfe}")

def provoke_and_handle_OverflowError():
    """Handling for overflow errors. Tries to exponate two massive numbers."""
    try:
        7771237.123**12837981723987
    except OverflowError as oe:
        print(f"Oopsie, overflow error occurred! {oe}")

def provoke_and_handle_SystemExitError():
    """Handling for system exit errors. Exits the script and gives a report on such action."""
    try:
        sys.exit()
    except SystemExit:
        print(f"I don't want to see you anymore!!")



def error_handlings():
    """Call all functions that start with 'provoke_and_handle_'."""

    global_names = globals()
    for name in global_names:
        if name.startswith("provoke_and_handle_"):
            print("\nAUFRUF von '{}':".format(name))
            global_names[name]()


if __name__ == "__main__":
    error_handlings()
