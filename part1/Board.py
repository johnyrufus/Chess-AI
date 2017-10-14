#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Pieces
from Position import Position
import copy

class PlayBoard:
    def __init__(self, state):
        self.state = state
        
    def __repr__(self):
        #Commenting temporarily for alternative represenation to make it easier to check manually with test cases
        '''rep = "  | A| B| C| D| E| F| G| H|\n"
        for i in range(0, 8):
            row = self.state[7 - i]
            
            rep += str(7 - i) + " |"
            for piece in row:
                if piece == "": rep += "  |"
                else: rep += str(piece) + "|"            
            rep += "\n"
            #return rep '''
        # Alternate representation to correlate with test case verification
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

    def score(self, side):
        points = 0
        
        my_king = False
        opp_king = False
        
        for i, row in enumerate(self.state):
            for j, piece in enumerate(row):
                if piece != "":
                    if piece.color == side: points += piece.score(self, Position.get(i, j))
                    else: points -= piece.score(self, Position.get(i, j))
                    
                    if type(piece) == Pieces.King:
                        if piece.color == side: my_king = True
                        else: opp_king = True
        
        if my_king and not opp_king: points = 999
        if not my_king and opp_king: points = -999

        return round(points, 5)
    
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


def Parse(raw_input):
    state = []
    
    for r in range(0, 8):
        row = []
        for c in range(0, 8):
            char = raw_input[r*8+c]
            pos = Position.get(r, c)
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
