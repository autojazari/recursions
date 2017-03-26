#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Sam Mohamed
Binary search implementation

Usage:
    $ python3 -m doctest binary_search.py

Complexity: O(log(n))
"""
def search(array, item):
    """
    >>> search([], 1)
    False

    >>> search([1,2,3,4], 8)
    False

    >>> search([1,2,3,4], 0)
    False

    >>> search([1,2,3,5], 4)
    False

    >>> search([1,2,3,5], 3)
    True

    >>> search([1,2,3,5], 5)
    True

    >>> search([1,2,3,5], 1)
    True

    """

    if not array:
        return False

    if len(array) == 1:
        return array[0] == item

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    return search(left, item) or search(right, item)
