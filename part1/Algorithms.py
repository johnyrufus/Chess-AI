#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Board
from multiprocessing import Queue, Process

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

        def worker(q, i, minimax_func, board, player, alpha, beta, depth):
            score = minimax_func(board, player, alpha, beta, depth)
            q.put((i, score))

        next_moves = self.initial_board.getmoves(self.initial_player)

        if self.initial_player == "w":
            minimax_func = self.min_value
            comparison_func = max
        else:
            minimax_func = self.max_value
            comparison_func = min

        opponent, alpha, beta, depth = self.initial_board.opponent(self.initial_player), -float('inf'), float('inf'), 0

        # parallelize only for depths 3 and above
        if self.max_depth > 2:
            procs = list()
            q = Queue()
            for i, pos in enumerate(next_moves):
                p = Process(target=worker, args=(q, i, minimax_func, self.initial_board.move(pos[0], pos[1]), opponent, alpha, beta, depth))
                procs.append(p)
                p.start()
            res = [q.get() for _ in next_moves]
        else:
            res = [(i, minimax_func(self.initial_board.move(pos[0], pos[1]), opponent, alpha, beta, depth)) for i, pos in enumerate(next_moves)]

        i, max_score = comparison_func(res, key=lambda x: x[1])
        suggested_board = self.initial_board.move(next_moves[i][0], next_moves[i][1])
        print(Board.Print(suggested_board))

        # Not sure of time delay of this, so first print/get the results out and then wait for processes to join.
        if self.max_depth > 2:
            for p in procs:
                p.join()

        return next_moves[i]
                
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
