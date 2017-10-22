#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
import Board
import Algorithms
import time
from multiprocessing import Process

'''
The pichu program is what reads in the user's input and then kicks off our
minimax search. The basic_parallel_minimax function is what we use to search
to various depths. The worker class is a simple process we can kick off to 
search to a depth given by i. We have defaulted the depth to 4 is that is 
what testing on burrow could be reached in a reasonable amount of time.

Due to the time constraint, however, we do not have certainty that we can
complete a depth of search 4. To safeguard against that, we do a quick search
at depths 1 and 2 to get an initial move to the user. Then we search 3 and 4
in parallel to maximize the likelihood that we can complete a full search.

The program then finishes by waiting for each process to finish by calling
join().

What we tried and didn't work:
- The biggest obstacle we ran into was how to search and respect the timer.
Our initial thought was to simply remove the depth value so that the function
would search until it ran out of time. However, and retrospecively obviously,
all this accomplished was causing a runaway search on one branch until the
timer began to runout and then heuristic estimation of every other branch. This
is why we ended up with doing iterative deepening search as a safeguard.

- Another attempt to solve the deepening issue was to search to a depth and 
then have each process wait until a signal was given to start searching at a
deeper depth. This process, however, proved too cumbersome to achieve in a
reasonable amount of time.
'''

def basic_parallel_minimax(player, board, timer, start):

    def worker(i):
        game = Algorithms.Minimax(board, player, i, timer, start)
        move = game.MiniMaxSearch()
        new_board = board.move(move[0], move[1])

    max_depth = 3
    procs = list()

    # For depths upto 2,  handle it serially, rest handle them parallely.
    for i in range(3, max_depth+1):
        p = Process(target=worker, args=(i,))
        procs.append(p)
        p.start()

    for p in procs:
        p.join()

    
if __name__ == "__main__":
    start = time.clock()
 
    basic_parallel_minimax(sys.argv[1], Board.Parse(sys.argv[2]), int(sys.argv[3]), start)
