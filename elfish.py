#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Sam Mohamed
A word is considered elfish if it contains the
letters: e, l, and f in it, in any order. For example, we would say
that the following words are elfish: whiteleaf, tasteful, unfriendly,
and waffles, because they each contain those letters

Usage:
    $ python3 -m doctest elfish.py

Complexity: O(n log(n))
"""
from binary_search import search

def elfish(word, letters):
    """
    >>> elfish('', 'efl')
    False

    >>> elfish('whiteleaf', 'elf')
    True

    >>> elfish('whiteleaf', 'elf')
    True

    >>> elfish('unfriendly', 'elf')
    True

    >>> elfish('waffles', 'elf')
    True

    >>> elfish('waffles', 'elf')
    True

    >>> elfish('sameh', 'elf')
    False

    >>> elfish('wolf', 'elf')
    False

    """
    result = True
    for letter in letters:
        result = result and search(word, letter)
    return result


elfish('waffles', 'elf')