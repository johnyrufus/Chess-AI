#!/usr/bin/env python3
import Board
import Pieces
from Position import Position
from Algorithms import Minimax

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

    # test for move function, move on the same row
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

    # test for move function, move to a different row
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

    # test for move function, when multiple pieces and moves involved
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

    new_board = new_board.move(Position.get(6, 3), Position.get(5, 3))
    new_board = new_board.move(Position.get(4, 3), Position.get(6, 3))
    assert test_case == new_board

    # Testing Minimax at depth 1
    test = '...K....' \
           '.n....Q.' \
           '........' \
           '..PP....' \
           '...k....' \
           '........' \
           '........' \
           '........'
    test_case = Board.Parse(test)
    game = Minimax(test_case, 'w', 1, -1)
    res = game.get_next_move()
    assert res[0] == (Position.get(1,6), Position.get(4,3))

    game = Minimax(test_case, 'b', 1, -1)
    res = game.get_next_move()
    assert res[0] == (Position.get(1, 1), Position.get(0, 3))

    # Testing Minimax at depth 2
    test = 'K.P.Q...' \
           '........' \
           '........' \
           '....p...' \
           '..p.p...' \
           '..pkp...' \
           '..ppp...' \
           '........'
    test_case = Board.Parse(test)
    game = Minimax(test_case, 'w', 2, -1)
    res = game.get_next_move()
    assert res[0] == (Position.get(0, 4), Position.get(0, 3))

    game = Minimax(test_case, 'b', 2, -1)
    res = game.get_next_move()
    print(res)
    assert res[0] == (Position.get(4, 2), Position.get(3, 2)) or res [0] == (Position.get(5, 3), Position.get(4, 3))

    # Testing Minimax at depth 2
    test = 'K.P...B.' \
           '........' \
           '........' \
           '..ppp...' \
           '..pp.P..' \
           '..pkpp..' \
           '..ppp...' \
           '........'
    test_case = Board.Parse(test)
    game = Minimax(test_case, 'w', 2, -1)
    res = game.get_next_move()
    assert res[0] == (Position.get(0, 6), Position.get(1, 7))

    game = Minimax(test_case, 'b', 2, -1)
    res = game.get_next_move()
    assert res[0] == (Position.get(5, 4), Position.get(4, 5))

    #Test currently failing for pawn move
    test = '........' \
           '........' \
           '........' \
           '........' \
           '...P....' \
           '...p....' \
           '........' \
           '........'
    test_case = Board.Parse(test)
    assert (test_case.state[5][3].moves(test_case.state, Position.get(5, 3)) == [])

if __name__ == "__main__": run_tests()
