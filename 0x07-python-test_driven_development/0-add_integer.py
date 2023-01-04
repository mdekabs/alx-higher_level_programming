#!/usr/bin/python3
"""This module is for testing an add function"""


def add_integer(a, b=98):
    """ adds integer
        Arguments:
        @a: first 
        @b: second integer, set to 98 suppose not given
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
