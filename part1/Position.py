#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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
