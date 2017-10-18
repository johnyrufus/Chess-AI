#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
P/p = Parakeet = Pawn
R/r = Robin = Rook
B/b = Bluejay = Bishop
Q/q = Quetzal = Queen
K/k = Kingfisher = King
N/n = Nighthawk = Knight
Rules: no castling, no check, no en passant.
'''
import Board
import Algorithms
from datetime import datetime
from multiprocessing import Process

def basic_parallel_minimax(board, player, time):

    def worker(i):
        game = Algorithms.Minimax(board, player, i, time)
        move = game.MiniMaxSearch()
        new_board = board.move(move[0], move[1])
        print(new_board)

    max_depth = 3
    procs = list()

    # For depths upto 2,  handle it serially, rest handle them parallely.
    for i in range(1, 3):
        worker(i)
    for i in range(3, max_depth+1):
        p = Process(target=worker, args=(i,))
        procs.append(p)
        p.start()

    for p in procs:
        p.join()

    
if __name__ == "__main__":
    start_time = datetime.now()
 
    player = 'w'
    state =   'RNBQKBNR' \
            + 'PPPPPPPP' \
            + '........' \
            + '........' \
            + '........' \
            + '........' \
            + 'pppppppp' \
            + 'rnbqkbnr'
    time_limit = 10

    root = Board.Parse(state)
    print(root.PrintOut())

    basic_parallel_minimax(root, 'w', -1)


