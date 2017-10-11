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
import Pieces
from datetime import datetime

def valid_move(board, piece, row, col):
        if row < 0 or row > 7 or col < 0 or col > 7: #Out of Bounds
            return False
        elif board[row][col] == "": #Move into empty space.
            return True
        elif board[row][col].color != piece.color: #Capture
            return True
        else:
            return False

def create_board(board):
    state = []
    
    for r in range(0, 8):
        row = []
        for c in range(0, 8):
            char = board[r*8+c]
            if char == "K": row.append(Pieces.King("w", r, c))
            elif char == "k": row.append(Pieces.King("b", r, c))
            elif char == "P": row.append(Pieces.Pawn("w", r, c))
            elif char == "p": row.append(Pieces.Pawn("b", r, c))
            elif char == "B": row.append(Pieces.Bishop("w", r, c))
            elif char == "b": row.append(Pieces.Bishop("b", r, c))
            elif char == "N": row.append(Pieces.Knight("w", r, c))
            elif char == "n": row.append(Pieces.Knight("b", r, c))
            elif char == "R": row.append(Pieces.Rook("w", r, c))
            elif char == "r": row.append(Pieces.Rook("b", r, c))
            elif char == "Q": row.append(Pieces.Rook("w", r, c))
            elif char == "q": row.append(Pieces.Rook("b", r, c))
            else: row.append("")
        state.append(row)
    return state

def print_state(state):
    print(*state, sep="\n")

def unit_tests():
    #Checking king movement when surrounded
    board = '...................P......PKP......P............................'
    state = create_board(board)
    assert(state[3][3].moves(state) == [])
    
    #Checking king movement when alone
    board = '...........................K....................................'
    state = create_board(board)
    assert(state[3][3].moves(state) == [(4, 3), (2, 3), (3, 4), (3, 2)])

    #Checking king movement when capture
    board = '...................p......pKp......p............................'
    state = create_board(board)
    assert(state[3][3].moves(state) == [(4, 3), (2, 3), (3, 4), (3, 2)])


if __name__ == "__main__":
    start_time = datetime.now()
 
    player = 'w'
    board = 'RNBQKBNRPPPPPPPP................................pppppppprnbqkbnr'
    time_limit = 10
    
    state = create_board(board)
    
    unit_tests()
