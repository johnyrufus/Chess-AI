#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Pieces
import PlayBoard

#TODO: Totally incomplete. WIP
class Minimax:
    def __init__(self, board, player, time):
        self.board = board
        self.player = player
        self.time = time

    def __repr__(self):
        return 'Current player - {}, bounded by - {} and the board - \n {}'\
            .format (self.player, self.time, self.board.__repr__())

    def minimax(self):
        self.board.moves(self.player)
        return max()

    def min_value(self, board, player):
        if board.is_terminal():
            return 999
        return max(board.getmoves(player), )

    def max_value(self, board):
        if board.is_terminal():
            return -999