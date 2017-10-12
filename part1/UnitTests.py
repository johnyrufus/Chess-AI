#!/usr/bin/env python3
import Board

def run_tests():
    #Checking king movement when alone
    test = '........' \
           '........' \
           '........' \
           '...K....' \
           '........' \
           '........' \
           '........' \
           '........'
    test_case = Board.Parse(test)
    assert(test_case.state[3][3].moves(test_case.state) == [((3, 3), (4, 3)), ((3, 3), (3, 4)), ((3, 3), (4, 4)), ((3, 3), (4, 2)),
                                                            ((3, 3), (2, 3)), ((3, 3), (3, 2)), ((3, 3), (2, 2)),  ((3, 3), (2, 4))])

    #Checking king movement when surrounded
    test = '........' \
           '........' \
           '..PPP...' \
           '..PKP...' \
           '..PPP...' \
           '........' \
           '........' \
           '........'
    test_case = Board.Parse(test)
    assert(test_case.state[3][3].moves(test_case.state) == [])    

    #Checking king movement when capture
    test = '........' \
           '........' \
           '...p....' \
           '..pKp...' \
           '...p....' \
           '........' \
           '........' \
           '........'
    test_case = Board.Parse(test)
    assert (test_case.state[3][3].moves(test_case.state) == [((3, 3), (4, 3)), ((3, 3), (3, 4)), ((3, 3), (4, 4)), ((3, 3), (4, 2)),
                                                             ((3, 3), (2, 3)), ((3, 3), (3, 2)), ((3, 3), (2, 2)), ((3, 3), (2, 4))])
    # Checking king movement when capture
    test = '........' \
           '........' \
           '..ppp...' \
           '..pKp...' \
           '..ppp...' \
           '........' \
           '........' \
           '........'
    test_case = Board.Parse(test)
    assert (test_case.state[3][3].moves(test_case.state) == [((3, 3), (4, 3)), ((3, 3), (3, 4)), ((3, 3), (4, 4)), ((3, 3), (4, 2)),
                                                             ((3, 3), (2, 3)), ((3, 3), (3, 2)), ((3, 3), (2, 2)), ((3, 3), (2, 4))])

    #Checking knight movement when alone
    test = '........' \
           '........' \
           '........' \
           '...N....' \
           '........' \
           '........' \
           '........' \
           '........'
    test_case = Board.Parse(test)    
    assert(test_case.state[3][3].moves(test_case.state) == [((3, 3), (1, 2)), ((3, 3), (2, 1)), ((3, 3), (1, 4)), ((3, 3), (4, 1)), \
                                                            ((3, 3), (5, 2)), ((3, 3), (2, 5)), ((3, 3), (5, 4)), ((3, 3), (4, 5))])

    #Checking knight when surrounded.
    test = '........' \
           '..P.P...' \
           '.P...P..' \
           '...N....' \
           '.P...P..' \
           '..P.P...' \
           '........' \
           '........'
    test_case = Board.Parse(test)    
    assert(test_case.state[3][3].moves(test_case.state) == [])

    #Checking knight capture.
    test = '........' \
           '..P.P...' \
           '.P...P..' \
           '...n....' \
           '.P...P..' \
           '..P.P...' \
           '........' \
           '........'
    test_case = Board.Parse(test)    
    assert(test_case.state[3][3].moves(test_case.state) == [((3, 3), (1, 2)), ((3, 3), (2, 1)), ((3, 3), (1, 4)), ((3, 3), (4, 1)), \
                                                            ((3, 3), (5, 2)), ((3, 3), (2, 5)), ((3, 3), (5, 4)), ((3, 3), (4, 5))])

    #Checking rook capture.
    test = '........' \
           '........' \
           '...p....' \
           '..pRp...' \
           '........' \
           '...p....' \
           '........' \
           '........'
    test_case = Board.Parse(test)  
    assert(test_case.state[3][3].moves(test_case.state) == [((3, 3), (2, 3)), ((3, 3), (3, 2)), ((3, 3), (4, 3)), \
                                                           ((3, 3), (5, 3)), ((3, 3), (3, 4))])

    #Checking rook surrounded.
    test = '........' \
           '........' \
           '...P....' \
           '..PRP...' \
           '...P....' \
           '........' \
           '........' \
           '........'
    test_case = Board.Parse(test)    
    assert(test_case.state[3][3].moves(test_case.state) == [])

    #Checking Bishop capture.
    test = '........' \
           '........' \
           '..p.p...' \
           '...B....' \
           '..p.p...' \
           '........' \
           '........' \
           '........'
    test_case = Board.Parse(test)
    assert(test_case.state[3][3].moves(test_case.state) == [((3, 3), (2, 2)), ((3, 3), (2, 4)), ((3, 3), \
                                                           (4, 4)), ((3, 3), (4, 2))])

    #Checking Bishop surrounded.
    test = '........' \
           '........' \
           '..P.P...' \
           '...B....' \
           '..P.P...' \
           '........' \
           '........' \
           '........'
    test_case = Board.Parse(test)
    assert(test_case.state[3][3].moves(test_case.state) == [])

    #Checking pawn movement
    test = '........' \
           '........' \
           '........' \
           '...P....' \
           '........' \
           '........' \
           '........' \
           '........'
    test_case = Board.Parse(test)
    assert(test_case.state[3][3].moves(test_case.state) == [((3, 3), (4, 3))])

    test = '........' \
           '........' \
           '........' \
           '...p....' \
           '........' \
           '........' \
           '........' \
           '........'
    test_case = Board.Parse(test)
    assert(test_case.state[3][3].moves(test_case.state) == [((3, 3), (2, 3))])

    test = '........' \
           '...P....' \
           '........' \
           '........' \
           '........' \
           '........' \
           '........' \
           '........'
    test_case = Board.Parse(test)
    assert(test_case.state[1][3].moves(test_case.state) == [((1, 3), (2, 3)), ((1, 3), (3, 3))])

    test = '........' \
           '........' \
           '........' \
           '........' \
           '........' \
           '........' \
           '...p....' \
           '........'
    test_case = Board.Parse(test)
    assert(test_case.state[6][3].moves(test_case.state) == [((6, 3), (5, 3)), ((6, 3), (4, 3))])

    #Testing capture
    test = '........' \
           '........' \
           '........' \
           '........' \
           '........' \
           '..PpP...' \
           '...p....' \
           '........'
    test_case = Board.Parse(test)
    assert(test_case.state[6][3].moves(test_case.state) == [((6, 3), (5, 4)), ((6, 3), (5, 2))])
    
    #Queen movement
    test = '........' \
           '........' \
           '........' \
           '...Q....' \
           '........' \
           '........' \
           '........' \
           '........'
    test_case = Board.Parse(test)
    assert(len(test_case.state[3][3].moves(test_case.state)) == 27)
    

if __name__ == "__main__": run_tests()
