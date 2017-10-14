#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Pieces
from Board import PlayBoard
import operator


'''
Implements the mini max algorithm
'''
class Minimax:
    def __init__(self, board, player, depth, time):
        self.initial_board = board
        self.initial_player = player
        self.time = time
        self.max_depth = depth

    def __repr__(self):
        return 'Current player - {}, bounded by time - {}, depth - {} and the board - \n {}'\
            .format(self.initial_player, self.time, self.max_depth, self.initial_board.__repr__())

    def get_next_move(self):
        moves = self.initial_board.getmoves(self.initial_player)
        scores = [self.mini_max(self.initial_board.move(pos[0], pos[1]), PlayBoard.opponent(self.initial_player), 1) for pos in moves]
        max_index, max_value = max(enumerate(scores), key=operator.itemgetter(1))
        return moves[max_index], self.initial_board.move(moves[max_index][0], moves[max_index][1])

    def mini_max(self, board, player, depth):
        if board.is_terminal():
            return -999 if player == self.initial_player else 999
        if depth > self.max_depth:
            return board.score(self.initial_player)
        func = max if player == self.initial_player else min
        return func([self.mini_max(board.move(pos[0], pos[1]), PlayBoard.opponent(player), depth + 1) for pos in board.getmoves(player)])

