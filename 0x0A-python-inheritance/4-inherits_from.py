#!/usr/bin/python3

"""method module"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class inherited from a_class,
    otherwise False."""
    return issubclass(type(obj), a_class) and type(obj) != a_class
