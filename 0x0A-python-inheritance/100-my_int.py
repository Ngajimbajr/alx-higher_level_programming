#!/usr/bin/python3
"""
class module
"""


class MyInt(int):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        """Inverts the == operator."""
        return self.value != other

    def __ne__(self, other):
        """Inverts the != operator."""
        return self.value == other
