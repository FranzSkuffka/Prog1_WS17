#!/usr/local/bin/python3

""" Calculate weekly workload for Prog1 course """
__author__      = "Jan Wirth <contact@jan-wirth.de"
__version__      = "0.0.1"

lps = 6
hours_per_lp = 30
workload = lps * hours_per_lp
weeks = 13
workload_per_week = workload / weeks
print(workload_per_week)
