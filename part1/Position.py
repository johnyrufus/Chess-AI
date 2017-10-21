#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
The Position class is a singleton class that allows easy/fast access to 
various positions which represent locations on the Chess/Pichu board. The
class has various functions:
    
__init__(): A simple constructor for the class given a row/column.
__repr__(): Returns a formatting string representation of the class.
get(): Returns a position with a given row/column. If the singleton collection
       for the class is None, it constructs all possible positions first.
offset(): Returns a new position with a given offset from the current position
'''    
class Position:

    positions = None

    # Constructor should not be used outside this class, please use get
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __repr__(self):
        return 'Position: {},{}'.format(self.row, self.col)

    @classmethod
    def get(cls, row, col):
        if cls.positions is None:
            # Cache all the positions, so that they can be reused, and not created every time.
            cls.positions = [[Position(i, j) for j in range(8)] for i in range(8)]
        return cls.positions[row][col] if 0 <= row <= 7 and 0 <= col <= 7 else None

    def offset(self, r, c):
        return Position.get(self.row + r, self.col + c)
