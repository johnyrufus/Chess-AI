#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Pieces

class PlayBoard:
    def __init__(self, state):
        self.state = state
        
    def __repr__(self):
        rep = "  | A| B| C| D| E| F| G| H|\n"
        for i in range(0, 8):
            row = self.state[7 - i]
            
            rep += str(7 - i) + " |"
            for piece in row:
                if piece == "": rep += "  |"
                else: rep += str(piece) + "|"            
            rep += "\n"
        return rep
    
    def score(self, side):
        points = 0
        
        my_king = False
        opp_king = False
        
        for row in self.state:
            for piece in row:
                if piece != "":
                    if piece.color == side: points += piece.score(self)
                    else: points -= piece.score(self)
                    
                    if type(piece) == Pieces.King:
                        if piece.color == side: my_king = True
                        else: opp_king = True
        
        if my_king and not opp_king: points = 999
        if not my_king and opp_king: points = -999
        
        return round(points, 5)
    
    def getmoves(self, side):
        moves = []
        
        for row in self.state:
            for piece in row:
                if piece != "":
                    if piece.color == side:
                        moves += piece.moves(self.state)
        return moves
    
def Parse(raw_input):
    state = []
    
    for r in range(0, 8):
        row = []
        for c in range(0, 8):
            char = raw_input[r*8+c]
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
            elif char == "Q": row.append(Pieces.Queen("w", r, c))
            elif char == "q": row.append(Pieces.Queen("b", r, c))
            else: row.append("")
        state.append(row)

    return PlayBoard(state)    
