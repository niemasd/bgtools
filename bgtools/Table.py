#!/usr/bin/env python3
'''
Functions and classes for representing a game table (e.g. dice, players, etc.)

Niema Moshiri 2020
'''
from bgtools.Dice import Die

class Table:
    '''Class to represent a game table (e.g. dice, players, etc.)'''
    def __init__(self):
        '''``Table`` constructor'''
        self.dice = list()

    def add_die(self, sides):
        '''Add a new ``Die`` to this ``Table``

        Args:
            ``sides``: See the ``sides`` parameter of the ``Die`` constructor
        '''
        self.dice.append(Die(sides))
