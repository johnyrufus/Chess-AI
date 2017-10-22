#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Board
import time
from multiprocessing import Queue, Process

'''
The Minimax class implements Minimax search with alpha-beta pruning. The 
class variables include the initial board state and player, the maximum depth
we are going to search, a timer which contains the number of seconds that
we have to search, and the start time from when our program is invoked.

For depths < 3, the class does a minimax search in a single threaded manner. 
For depths >=3, the class creates N processes to search down each branch of the
tree originating from the root node. Each process searches down to max_depth
and then returns the estimated board value. If 90% of the time allotted has 
been consumed before reaching max depth then the search begins to roll up in 
order to provide a recommendation in the time given. 
'''
class Minimax:
    '''
    The __init__ function takes in the search's initial state, depth, timer
    and start time
    '''
    def __init__(self, board, player, depth, timer, start):
        self.initial_board = board
        self.initial_player = player
        self.max_depth = depth
        self.timer = timer
        self.start = start

    '''
    Returns a formatted representation of our minimax search. Used primarily
    for debugging purposes.
    '''
    def __repr__(self):
        return 'Current player - {}, bounded by time - {}, depth - {} and the board - \n {}'\
            .format(self.initial_player, self.timer, self.max_depth, self.initial_board.__repr__())
    
    '''
    This function performs Minimax Search.
    
    The worker class is responsible for
    searching down each branch of the tree and putting the resulting score in
    a multiprocess queue.
    
    The search begins by establishing the initial state - if we're playing as
    black then we want to minimize over the moves available at the initial
    state and call max_value to begin looking at white's responses. 
    Conversely, if we're playing white we want to maximize the resulting score
    and begin our search using min_value to evaluate black's responses to each
    move. The balance of the function rolls up the results from the search and
    prints out the suggested move to the user.
    '''
    def MiniMaxSearch(self):

        def worker(q, i, minimax_func, board, player, alpha, beta, depth, timer, start):
            score = minimax_func(board, player, alpha, beta, depth, timer, start)
            q.put((i, score))

        #start = time.clock() # TODO: Comment this before final
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
                p = Process(target=worker, args=(q, i, minimax_func, self.initial_board.move(pos[0], pos[1]), opponent, alpha, beta, depth, self.timer, self.start))
                procs.append(p)
                p.start()
            res = [q.get() for _ in next_moves]
        else:
            res = [(i, minimax_func(self.initial_board.move(pos[0], pos[1]), opponent, alpha, beta, depth, self.timer, self.start)) for i, pos in enumerate(next_moves)]

        i, max_score = comparison_func(res, key=lambda x: x[1])
        suggested_board = self.initial_board.move(next_moves[i][0], next_moves[i][1])
        print(Board.Print(suggested_board))
        #print('Time taken for depth = {} is {}'.format(self.max_depth, time.clock() - start)) # TODO: Comment this before final

        # Not sure of time delay of this, even though I believe this should be quick,
        # so first print/get the results out as in the statements above and then wait for processes to join.
        if self.max_depth > 2:
            for p in procs:
                p.join()

        return next_moves[i]
                
    '''
    The max_value function is used for MAX moves where the player is trying
    to maximize the board's state score. The first line contains our watchdogs
    that look for whether or not we've hit max depth, if the board is in a 
    terminal state or if we're running out of time. If any of those conditions
    are true, then the function returns and we begin to roll up the tree.
    
    The rest of the function initializes the value so far to negative infinity
    and then generates the potential moves for the board state. For each move,
    it recursively calls min_value and tests to see whether that returns a value
    better than we've seen so far. If so, we record that value as the new MAX
    and continue searching. If we result in a value greater than beta, we can
    return our seen value because we know the other player will never select
    this move as there's another move we've already seen that results in a lower
    score.
    
    Finally, if value is < beta, then we calculate our new alpha as the max
    of alpha and value which is used in min_value.
    '''
    def max_value(self, board, player, alpha, beta, depth, timer, start):
        if depth > self.max_depth or board.is_terminal() or (time.clock() - start)/timer > 0.9: return board.score()

        value = -float('inf')
        for pos in board.getmoves(player):
            value = max(value, self.min_value(board.move(pos[0], pos[1]), board.opponent(player), alpha, beta, depth+1, timer, start))
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value
    
    '''
    The min_value function operates in the opposite manner of max_value. Here,
    we are trying to MIN the value of the moves the player has available to 
    them. Like max_value, we have our watchdogs for depth, terminal states,
    and the timer.
    
    If we're not rolling up the search due to one of the watchdogs, then we
    generate the moves available to the player. For each move, we call 
    max_value using the board state that results from taking the move. If the
    resulting value is less than the value we've seen so far, we record it.
    Then, if the value is less than alpha, we can return immediately as we know
    that the MAX player has a better move available to them from what we've
    seen in the tree so far. Finally, we take the minimum of beta and value
    in order to update the searching in max_value.
    '''
    def min_value(self, board, player, alpha, beta, depth, timer, start):
        if depth > self.max_depth or board.is_terminal() or (time.clock() - start)/timer > 0.9: return board.score()
        
        value = float('inf')
        for pos in board.getmoves(player):
            value = min(value, self.max_value(board.move(pos[0], pos[1]), board.opponent(player), alpha, beta, depth+1, timer, start))
            if value <= alpha:
                return value
            beta = min(beta, value)
        return value    
