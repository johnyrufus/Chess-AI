#!/usr/bin/env python3
import Board

def run_tests():
    #Checking king movement when alone
    test = '...........................K....................................'
    test_case = Board.Parse(test)
    assert(test_case.state[3][3].moves(test_case.state) == [((3, 3), (4, 3)), ((3, 3), (2, 3)), ((3, 3), (3, 4)), ((3, 3), (3, 2))])

    #Checking king movement when surrounded
    test = '...................P......PKP......P............................'
    test_case = Board.Parse(test)
    assert(test_case.state[3][3].moves(test_case.state) == [])    

    #Checking king movement when capture
    test = '...................p......pKp......p............................'
    test_case = Board.Parse(test)
    assert(test_case.state[3][3].moves(test_case.state) == [((3, 3), (4, 3)), ((3, 3), (2, 3)), ((3, 3), (3, 4)), ((3, 3), (3, 2))])

    #Checking knight movement when alone
    test = '...........................N....................................'
    test_case = Board.Parse(test)    
    assert(test_case.state[3][3].moves(test_case.state) == [((3, 3), (1, 2)), ((3, 3), (2, 1)), ((3, 3), (1, 4)), ((3, 3), (4, 1)), \
                                                            ((3, 3), (5, 2)), ((3, 3), (2, 5)), ((3, 3), (5, 4)), ((3, 3), (4, 5))])

    #Checking knight when surrounded.
    test = '..........P.P....P...P.....N.....P...P....P.P...................'
    test_case = Board.Parse(test)    
    assert(test_case.state[3][3].moves(test_case.state) == [])

    #Checking knight capture.
    test = '..........P.P....P...P.....n.....P...P....P.P...................'
    test_case = Board.Parse(test)    
    assert(test_case.state[3][3].moves(test_case.state) == [((3, 3), (1, 2)), ((3, 3), (2, 1)), ((3, 3), (1, 4)), ((3, 3), (4, 1)), \
                                                            ((3, 3), (5, 2)), ((3, 3), (2, 5)), ((3, 3), (5, 4)), ((3, 3), (4, 5))])

    #Checking rook capture.
    test = '...................p......pRp..............p....................'
    test_case = Board.Parse(test)    
    assert(test_case.state[3][3].moves(test_case.state) == [((3, 3), (4, 3)), ((3, 3), (5, 3)), ((3, 3), (2, 3)), \
                                                           ((3, 3), (3, 4)), ((3, 3), (3, 2))])

    #Checking rook surrounded.
    test = '...................P......PRP......P............................'
    test_case = Board.Parse(test)    
    assert(test_case.state[3][3].moves(test_case.state) == [])

    #Checking Bishop capture.
    test = '..................p.p......B......p.p...........................'
    test_case = Board.Parse(test)
    assert(test_case.state[3][3].moves(test_case.state) == [((3, 3), (4, 4)), ((3, 3), (4, 2)), ((3, 3), (2, 4)), \
                                                           ((3, 3), (2, 2))])

    #Checking Bishop surrounded.
    test = '..................P.P......B......P.P...........................'
    test_case = Board.Parse(test)
    assert(test_case.state[3][3].moves(test_case.state) == [])
