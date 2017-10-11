#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
P/p = Parakeet = Pawn
R/r = Robin = Rook
B/b = Bluejay = Bishop
Q/q = Quetzal = Queen
K/k = Kingfisher = King - no diagonal movements
N/n = Nighthawk = Knight

Rules: no castling, no check, no en passant.
'''
import Board
from datetime import datetime

def print_state(state):
    print(*state, sep="\n")

def unit_tests():
    #Checking king movement when alone
    test = '...........................K....................................'
    test_case = Board.PlayBoard(test)
    assert(test_case.state[3][3].moves(test_case.state) == [((3, 3), (4, 3)), ((3, 3), (2, 3)), ((3, 3), (3, 4)), ((3, 3), (3, 2))])

    #Checking king movement when surrounded
    test = '...................P......PKP......P............................'
    test_case = Board.PlayBoard(test)
    assert(test_case.state[3][3].moves(test_case.state) == [])    

    #Checking king movement when capture
    test = '...................p......pKp......p............................'
    test_case = Board.PlayBoard(test)
    assert(test_case.state[3][3].moves(test_case.state) == [((3, 3), (4, 3)), ((3, 3), (2, 3)), ((3, 3), (3, 4)), ((3, 3), (3, 2))])

    #Checking knight movement when alone
    test = '...........................N....................................'
    test_case = Board.PlayBoard(test)    
    assert(test_case.state[3][3].moves(test_case.state) == [((3, 3), (1, 2)), ((3, 3), (2, 1)), ((3, 3), (1, 4)), ((3, 3), (4, 1)), \
                                                            ((3, 3), (5, 2)), ((3, 3), (2, 5)), ((3, 3), (5, 4)), ((3, 3), (4, 5))])

    #Checking knight when surrounded.
    test = '..........P.P....P...P.....N.....P...P....P.P...................'
    test_case = Board.PlayBoard(test)    
    assert(test_case.state[3][3].moves(test_case.state) == [])

    #Checking knight capture.
    test = '..........P.P....P...P.....n.....P...P....P.P...................'
    test_case = Board.PlayBoard(test)    
    assert(test_case.state[3][3].moves(test_case.state) == [((3, 3), (1, 2)), ((3, 3), (2, 1)), ((3, 3), (1, 4)), ((3, 3), (4, 1)), \
                                                            ((3, 3), (5, 2)), ((3, 3), (2, 5)), ((3, 3), (5, 4)), ((3, 3), (4, 5))])

    #Checking rook capture.
    test = '...................p......pRp..............p....................'
    test_case = Board.PlayBoard(test)    
    assert(test_case.state[3][3].moves(test_case.state) == [((3, 3), (4, 3)), ((3, 3), (5, 3)), ((3, 3), (2, 3)), \
                                                           ((3, 3), (3, 4)), ((3, 3), (3, 2))])

    #Checking rook surrounded.
    test = '...................P......PRP......P............................'
    test_case = Board.PlayBoard(test)    
    assert(test_case.state[3][3].moves(test_case.state) == [])

    #Checking Bishop capture.
    test = '..................p.p......B......p.p...........................'
    test_case = Board.PlayBoard(test)
    assert(test_case.state[3][3].moves(test_case.state) == [((3, 3), (4, 4)), ((3, 3), (4, 2)), ((3, 3), (2, 4)), \
                                                           ((3, 3), (2, 2))])

    #Checking Bishop surrounded.
    test = '..................P.P......B......P.P...........................'
    test_case = Board.PlayBoard(test)
    assert(test_case.state[3][3].moves(test_case.state) == [])

    
if __name__ == "__main__":
    start_time = datetime.now()
 
    player = 'w'
    state = 'RNBQKBNRPPPPPPPP................................pppppppprnbqkbnr'
    time_limit = 10
    
    root = Board.PlayBoard(state)
    
    unit_tests()
