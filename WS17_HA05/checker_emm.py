#!/usr/bin/env python3

"""Functions for checking results, e.g. whether two values are the same.

Author: emm
Version: 20171123
"""

def check_equality(value1, value2):
    """Compares two values, and returns a message about their equality.
    
    :param value1: input value for comparison
    :param value2: another input value for comparison
    :return: message containing information about the equality of the input values; additionally content: if the values differ, both of them are collected for introspection purposes; if they are the same, one of them will be collected.
    """
    
    if value1 == value2:
        return "SAME VALUES: {}".format(value1)
    
    return "DIFFERENT VALUES:\n- FIRST: {}\n- SECOND: {}".format(value1, value2)
    