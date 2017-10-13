#!/usr/bin/env python3
import Board
import Pieces
from Position import Position

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
    assert(test_case.state[3][3].moves(test_case.state, Position.get(3, 3)) == [(Position.get(3, 3), Position.get(4, 3)),
                    (Position.get(3, 3), Position.get(3, 4)), (Position.get(3, 3), Position.get(4, 4)),
                    (Position.get(3, 3), Position.get(4, 2)), (Position.get(3, 3), Position.get(2, 3)),
                    (Position.get(3, 3), Position.get(3, 2)), (Position.get(3, 3), Position.get(2, 2)),
                    (Position.get(3, 3), Position.get(2, 4))])

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
    assert(test_case.state[3][3].moves(test_case.state, Position.get(3, 3)) == [])

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
    assert (test_case.state[3][3].moves(test_case.state, Position.get(3, 3)) == [(Position.get(3, 3), Position.get(4, 3)),
            (Position.get(3, 3), Position.get(3, 4)), (Position.get(3, 3), Position.get(4, 4)),
            (Position.get(3, 3), Position.get(4, 2)), (Position.get(3, 3), Position.get(2, 3)),
            (Position.get(3, 3), Position.get(3, 2)), (Position.get(3, 3), Position.get(2, 2)),
            (Position.get(3, 3), Position.get(2, 4))])
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
    assert (test_case.state[3][3].moves(test_case.state, Position.get(3, 3)) == [(Position.get(3, 3), Position.get(4, 3)),
            (Position.get(3, 3), Position.get(3, 4)), (Position.get(3, 3), Position.get(4, 4)),
            (Position.get(3, 3), Position.get(4, 2)), (Position.get(3, 3), Position.get(2, 3)),
            (Position.get(3, 3), Position.get(3, 2)), (Position.get(3, 3), Position.get(2, 2)),
            (Position.get(3, 3), Position.get(2, 4))])

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
    assert(test_case.state[3][3].moves(test_case.state, Position.get(3, 3)) == [(Position.get(3, 3), Position.get(1, 2)),
            (Position.get(3, 3), Position.get(2, 1)), (Position.get(3, 3), Position.get(1, 4)),
            (Position.get(3, 3), Position.get(4, 1)), (Position.get(3, 3), Position.get(5, 2)),
            (Position.get(3, 3), Position.get(2, 5)), (Position.get(3, 3), Position.get(5, 4)),
            (Position.get(3, 3), Position.get(4, 5))])

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
    assert(test_case.state[3][3].moves(test_case.state, Position.get(3, 3)) == [])

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
    assert(test_case.state[3][3].moves(test_case.state, Position.get(3, 3)) == [(Position.get(3, 3), Position.get(1, 2)),
            (Position.get(3, 3), Position.get(2, 1)), (Position.get(3, 3), Position.get(1, 4)),
            (Position.get(3, 3), Position.get(4, 1)), (Position.get(3, 3), Position.get(5, 2)),
            (Position.get(3, 3), Position.get(2, 5)), (Position.get(3, 3), Position.get(5, 4)),
            (Position.get(3, 3), Position.get(4, 5))])

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
    assert(test_case.state[3][3].moves(test_case.state, Position.get(3, 3)) == [(Position.get(3, 3), Position.get(2, 3)),
            (Position.get(3, 3), Position.get(3, 2)), (Position.get(3, 3), Position.get(4, 3)),
            (Position.get(3, 3), Position.get(5, 3)), (Position.get(3, 3), Position.get(3, 4))])

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
    assert(test_case.state[3][3].moves(test_case.state, Position.get(3, 3)) == [])

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
    assert(test_case.state[3][3].moves(test_case.state, Position.get(3, 3)) == [(Position.get(3, 3), Position.get(2, 2)),
            (Position.get(3, 3), Position.get(2, 4)), (Position.get(3, 3), Position.get(4, 4)), (Position.get(3, 3), Position.get(4, 2))])

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
    assert(test_case.state[3][3].moves(test_case.state, Position.get(3, 3)) == [])

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
    assert(test_case.state[3][3].moves(test_case.state, Position.get(3, 3)) == [(Position.get(3, 3), Position.get(4, 3))])

    test = '........' \
           '........' \
           '........' \
           '...p....' \
           '........' \
           '........' \
           '........' \
           '........'
    test_case = Board.Parse(test)
    assert(test_case.state[3][3].moves(test_case.state, Position.get(3, 3)) == [(Position.get(3, 3), Position.get(2, 3))])

    test = '........' \
           '...P....' \
           '........' \
           '........' \
           '........' \
           '........' \
           '........' \
           '........'
    test_case = Board.Parse(test)
    assert(test_case.state[1][3].moves(test_case.state, Position.get(1, 3)) == [(Position.get(1, 3), Position.get(2, 3)),
                                                                                (Position.get(1, 3), Position.get(3, 3))])

    test = '........' \
           '........' \
           '........' \
           '........' \
           '........' \
           '........' \
           '...p....' \
           '........'
    test_case = Board.Parse(test)
    assert(test_case.state[6][3].moves(test_case.state, Position.get(6, 3)) == [(Position.get(6, 3), Position.get(5, 3)),
                                                                                (Position.get(6, 3), Position.get(4, 3))])

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
    assert(test_case.state[6][3].moves(test_case.state, Position.get(6, 3)) == [(Position.get(6, 3), Position.get(5, 4)),
                                                                                (Position.get(6, 3), Position.get(5, 2))])
    
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
    assert(len(test_case.state[3][3].moves(test_case.state, Position.get(3, 3))) == 27)

    # test for move function
    test = '........' \
           '........' \
           '........' \
           '...Q....' \
           '........' \
           '........' \
           '........' \
           '........'
    test_case = Board.Parse(test)
    new_board = test_case.move(Position.get(3, 3), Position.get(3, 7))
    assert new_board.state[3][3] == '' and type(new_board.state[3][7]) == Pieces.Queen and  new_board.state[3][7].color == 'w'
    assert test_case.state[3][7] == '' and type(test_case.state[3][3]) == Pieces.Queen and test_case.state[3][3].color == 'w'

    # test for move function
    test = '........' \
           '........' \
           '........' \
           '...Q....' \
           '........' \
           '........' \
           '........' \
           '........'
    test_case = Board.Parse(test)
    new_board = test_case.move(Position.get(3, 3), Position.get(4, 7))
    assert new_board.state[3][3] == '' and type(new_board.state[4][7]) == Pieces.Queen and new_board.state[4][
                                                                                               7].color == 'w'
    assert test_case.state[4][7] == '' and type(test_case.state[3][3]) == Pieces.Queen and test_case.state[3][
                                                                                               3].color == 'w'

    # test for move function
    test = '........' \
           '........' \
           '........' \
           '........' \
           '........' \
           '..PpP...' \
           '...p....' \
           '........'
    test_case = Board.Parse(test)
    new_board = test_case.move(Position.get(5, 3), Position.get(4, 3))
    assert new_board.state[5][3] == '' and type(new_board.state[4][3]) == Pieces.Pawn and new_board.state[4][3].color == 'b'
    assert test_case.state[4][3] == '' and type(test_case.state[5][3]) == Pieces.Pawn and test_case.state[5][3].color == 'b'
    #print(new_board)
    #print(test_case)

    # Testing get_next_state
    test = '........' \
           '........' \
           '........' \
           '........' \
           '........' \
           '..PpP...' \
           '...p....' \
           '........'
    test_case = Board.Parse(test)
    print(test_case)
    next_states = test_case.get_next_states('b')
    print(next_states)

    next_states = test_case.get_next_states('w')
    print(next_states)

    

if __name__ == "__main__": run_tests()
