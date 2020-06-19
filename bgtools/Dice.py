#!/usr/bin/env python3
'''
Functions and classes for representing dice

Niema Moshiri 2020
'''
from random import choice

class Die:
    '''Class to represent a single die'''
    def __init__(self, sides):
        '''``Die`` constructor

        Args:
            ``sides`` (``list`` or ``int``): The list of sides, or an ``int`` such that the die will have sides 1, 2, ..., ``sides``
        '''
        if isinstance(sides, int):
            self.sides = tuple(range(1,sides+1))
        elif isinstance(sides, list) or isinstance(sides, set):
            self.sides = tuple(sides)
        else:
            raise TypeError("'sides' must be 'list' or 'int'")

    def roll(self):
        '''Roll this ``Die``

        Returns:
            ``int``: The value of one of the sides of this ``Die`` with uniform probability
        '''
        return choice(self.sides)
