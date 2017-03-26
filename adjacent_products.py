#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Sam Mohamed
Find the largest product of two consecutive elemnts
in a sequence.

Usage:
    $ python3 -m doctest adjacent_products.

Arguments:
    filepath: path to file containing array elements

Attributes:
"""
def multiply(inputArray):
    m = inputArray[0] * inputArray[1]
    return m

def adjacent_product(inputArray):
    """
    >>> adjacent_product([1,0,1,0,1000])
    0

    >>> adjacent_product([-1, 1, -1])
    -1
    """
    # [3, 6, -2, -5, 7, 3]
    if len(inputArray) <= 1:
        return []

    left = inputArray[:2]
    right = inputArray[1:]

    m = multiply(left)

    result = adjacent_product(right)

    # combine solutions
    result.insert(0, m)

    return result