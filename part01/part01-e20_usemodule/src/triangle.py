""" This is the triangle module.

This module has two functions: hypotenuse and area.
This module has two attributes: version and author.
"""

from math import sqrt


__version__ = "1.0"
__author__ = "orghmoitr"


def hypotenuse(base, height):
    """Return the hypotenuse of a right-angled triangle."""
    return sqrt(base**2 + height**2)


def area(base, height):
    """Return the area of a right-angled triangle."""
    return (base*height) / 2
