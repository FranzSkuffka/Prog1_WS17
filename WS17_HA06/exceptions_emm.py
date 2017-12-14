#!/usr/bin/env python3

"""Übung zur Erzeugung und Behandlung von Fehlern

Autor: Jan Wirth
Version: 20171208
"""

import sys

def handle_ModuleNotFoundError():
    """Handling for module not found errors. Tries to import a module that doesn't exist."""
    try:
        import aiujsdaiosjdiajhsd
    except ModuleNotFoundError as mnfe:
        print(f"Sorry! {mnfe} was found!")

def handle_KeyError():
    """Handling for key errors. Tries looking for a key which doesn't exist in given dictionary."""
    test_dict = {}
    try:
        print(test_dict[15])
    except KeyError as ke:
        print(f"Sorry! The key {ke} does not exist in test_dict!")

def handle_NameError():
    """Handling for name errors. Tries to print a variable which hasn't been defined."""
    try:
        print(bliblablub)
    except NameError as ne:
        print(f"Sorry! {ne}")

def handle_ZeroDivisionError():
    """Handling for zero divison errors. Tries to divide 3 by 0."""
    try:
        print(3/0)
    except ZeroDivisionError as zde:
        print(f"Sorry! {zde}")

def handle_SyntaxError():
    """Handling for syntax errors. Tries to call the eval function on a string."""
    try:
        eval("x === x")
    except SyntaxError as se:
        print(f"Sorry! You can't use eval in that way: {se}")

def handle_TypeError():
    """Handling for type errors. Tries to add and int to a string."""
    try:
        print("Hihi" + 3)
    except TypeError as te:
        print(f"Sorry! {te}")

def handle_ImportError():
    """Handling for import errors. Tries to import from a module which doesn't exist."""
    try:
        from plup import plap
    except ImportError as impe:
        print(f"Sorry! {impe}")

def handle_FileNotFoundError():
    """Handling for file not found errors. Tries to open a file which doesn't exist."""
    try:
        with open("aiusdiuahsdiuhasiudh.txt") as f:
            print("well")
    except FileNotFoundError as fnfe:
        print(f"Sorry! {fnfe}")

def handle_OverflowError():
    """Handling for overflow errors. Tries to exponate two massive numbers."""
    try:
        7771237.123**12837981723987
    except OverflowError as oe:
        print(f"Sorry, overflow error occurred! {oe}")

def handle_SystemExitError():
    """Handling for system exit errors. Exits the script and gives a report on such action."""
    try:
        sys.exit()
    except SystemExit:
        print(f"Ok, bye, you exited the script!")



def error_handlings():
    """Aufruf von allen Funktionen im Skript, deren Namen mit 'handle_' anfängt."""

    global_names = globals()
    for name in global_names:
        if name.startswith("handle_"):
            print("\nAUFRUF von '{}':".format(name))
            global_names[name]()


if __name__ == "__main__":
    error_handlings()
