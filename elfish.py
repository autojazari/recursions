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
"""
def elfish(word):
    """
    >>> elfish('')
    False

    >>> elfish('whiteleaf')
    True

    >>> elfish('whiteleaf')
    True

    >>> elfish('unfriendly')
    True

    >>> elfish('waffles')
    True

    >>> elfish('waffles')
    True

    >>> elfish('sameh')
    False

    >>> elfish('wolf')
    False

    """
    if len(word) == 1:
        return word == 'e' or word == 'l' or word == 'f'
