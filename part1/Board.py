#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Pieces
from Position import Position

class PlayBoard:
    def __init__(self, state):
        self.state = state
        
    # Alternate representation to correlate with test case verification
    def __repr__(self):
    
        def get_repr(piece):
            if piece == '':
                return '.'
            if piece.__class__.__name__.startswith('Kn'):
                res = 'N'
            else:
                res = piece.__class__.__name__[0]
            return res if piece.color == 'w' else res.lower()

        return '\n'+'\n'.join([''.join(map(lambda piece: get_repr(piece), row)) for row in self.state])

    @staticmethod
    def opponent(player):
        return 'b' if player == 'w' else 'w'

    '''
    A state is terminal, if a king is missing.
    For the current purposes of the algorithm, doesn't matter which king is missing.
    '''
    def is_terminal(self):
        return len([1 for row in self.state for piece in row if type(piece) == Pieces.King]) != 2

    def score(self):
        points = 0
        
        w_king = False
        b_king = False
        
        for i, row in enumerate(self.state):
            for j, piece in enumerate(row):
                if piece != "":
                    points += piece.score(self, Position.get(i, j))
                    
                    if type(piece) == Pieces.King:
                        if piece.color == "w": w_king = True
                        else: b_king = True

        if w_king and not b_king: points = 999
        if b_king and not w_king: points = -999

        return points
    
    def getmoves(self, side):
        moves = []
        
        for i, row in enumerate(self.state):
            for j, piece in enumerate(row):
                if piece != "":
                    if piece.color == side:
                        moves += piece.moves(self.state, Position.get(i, j))
        return moves

    '''
    Given the current location pos, move the piece in pos to its new location specified by new_pos
    create and return a new board to reflect the move and the changed state
    '''
    def move(self, pos, new_pos):
        new_state = [row for row in self.state]
        new_state[pos.row] = new_state[pos.row][:pos.col] + [''] + new_state[pos.row][pos.col+1:]
        new_state[new_pos.row] = new_state[new_pos.row][:new_pos.col] + [self.state[pos.row][pos.col]] + new_state[new_pos.row][new_pos.col + 1:]
        return PlayBoard(new_state)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return all( self.state[i][j] == other.state[i][j] for i in range(0, 8) for j in range(0, 8))
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def PrintOut(self):
        #Commenting temporarily for alternative represenation to make it easier to check manually with test cases
        rep = "  | A| B| C| D| E| F| G| H|\n"
        for i in range(0, 8):
            row = self.state[7 - i]
            
            rep += str(7 - i) + " |"
            for piece in row:
                if piece == "": rep += "  |"
                else: rep += str(piece) + "|"            
            rep += "\n"
        print(rep)

def Parse(raw_input):
    state = []
    
    for r in range(0, 8):
        row = []
        for c in range(0, 8):
            char = raw_input[r*8+c]

            if char == "K": row.append(Pieces.King("w"))
            elif char == "k": row.append(Pieces.King("b"))
            elif char == "P": row.append(Pieces.Pawn("w"))
            elif char == "p": row.append(Pieces.Pawn("b"))
            elif char == "B": row.append(Pieces.Bishop("w"))
            elif char == "b": row.append(Pieces.Bishop("b"))
            elif char == "N": row.append(Pieces.Knight("w"))
            elif char == "n": row.append(Pieces.Knight("b"))
            elif char == "R": row.append(Pieces.Rook("w"))
            elif char == "r": row.append(Pieces.Rook("b"))
            elif char == "Q": row.append(Pieces.Queen("w"))
            elif char == "q": row.append(Pieces.Queen("b"))
            else: row.append("")
        state.append(row)

    return PlayBoard(state)

def Print(board):
    state = ""
    
    for row in board.state:
        for cell in row:
            if cell == "": state += "."
            if type(cell) == Pieces.King: state += "k" if cell.color == "b" else "K"
            if type(cell) == Pieces.Queen: state += "q" if cell.color == "b" else "Q"
            if type(cell) == Pieces.Rook: state += "r" if cell.color == "b" else "R"
            if type(cell) == Pieces.Knight: state += "n" if cell.color == "b" else "N"
            if type(cell) == Pieces.Bishop: state += "b" if cell.color == "b" else "B"
            if type(cell) == Pieces.Pawn: state += "p" if cell.color == "b" else "P"
            
    return state
            
