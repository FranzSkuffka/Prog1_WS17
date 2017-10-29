#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


""" Calculate weekly workload for Prog1 course """
__author__      = "Jan Wirth <contact@jan-wirth.de"
__version__      = "0.0.1"

lps = 6
hours_per_lp = 30
workload = lps * hours_per_lp
weeks = 13
workload_per_week = workload / weeks
print(workload_per_week)


print("Ein Leistungspunkt entspricht", hours_per_lp, "Stunden Arbeit.")
print("Für den Kurs erhält man", lps, "Leistungspunkte.")
print("Also: man soll für den Kurs insgesamt", workload, "Stunden lernen.")
print("Dies entspricht einer wöchentlichen Lernzeit von", str(workload_per_week) + ".") # concat to remove space before full stop.
