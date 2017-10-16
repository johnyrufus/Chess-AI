#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Board

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
            
    def MiniMaxSearch(self):
        move = None
        
        if self.initial_player == "w":        
            max_score = -float('inf')
            for pos in self.initial_board.getmoves(self.initial_player):
                score = self.min_value(self.initial_board.move(pos[0], pos[1]), self.initial_board.opponent(self.initial_player), -float('inf'), float('inf'), 0)

                if score > max_score:
                    max_score = score
                    move = pos
        else:
            max_score = float('inf')
            for pos in self.initial_board.getmoves(self.initial_player):
                score = self.max_value(self.initial_board.move(pos[0], pos[1]), self.initial_board.opponent(self.initial_player), -float('inf'), float('inf'), 0)
            
                if score < max_score:
                    max_score = score
                    move = pos
        return move
                
    def max_value(self, board, player, alpha, beta, depth):
        if depth > self.max_depth or board.is_terminal(): return board.score()

        value = -float('inf')
        for pos in board.getmoves(player):
            value = max(value, self.min_value(board.move(pos[0], pos[1]), board.opponent(player), alpha, beta, depth+1))
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value
    
    def min_value(self, board, player, alpha, beta, depth):
        if depth > self.max_depth or board.is_terminal(): return board.score()
        
        value = float('inf')
        for pos in board.getmoves(player):
            value = min(value, self.max_value(board.move(pos[0], pos[1]), board.opponent(player), alpha, beta, depth+1))
            if value <= alpha:
                return value
            beta = min(beta, value)
        return value    
