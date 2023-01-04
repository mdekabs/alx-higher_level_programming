#!/usr/bin/python3
"""function to print first and last name"""


def say_my_name(first_name, last_name=""):
    """ prints first and last name
        Arguments:
            @first_name: first name
            @second_name: last_name 
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    fprint("My name is {first_name} {last_name}")
