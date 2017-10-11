#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Piece():
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col

class King(Piece):
    def __repr__(self):
        if self.color == "w": return u'♔'
        else: return u'♚'
        
    def moves(self, board):
        moves = [(self.row+1, self.col), (self.row-1, self.col), (self.row, self.col+1), (self.row, self.col-1)]
        possible = []
        
        for move in moves:
            if valid_move(board, self, move[0], move[1]): possible.append(((self.row, self.col), move))
        return possible

class Knight(Piece):
    def __repr__(self):
        if self.color == "w": return u'♘'
        else: return u'♞'   

    def moves(self, board): #L1/U2, L1/D2, R1/U2, R1/D2, U1/L2, U1/R2, D1/L2, D1/R2
        moves = []
        for v1 in [-2, 2]:
            for v2 in [-1, 1]:
                moves.append((self.row+v1, self.col+v2))
                moves.append((self.row+v2, self.col+v1))
        
        possible = []
        
        for move in moves:
            if valid_move(board, self, move[0], move[1]): possible.append(((self.row, self.col), move))
        return possible
        
class Queen(Piece):
    def __repr__(self):
        if self.color == "w": return u'♕'
        else: return u'♛'        

class Pawn(Piece):
    def __repr__(self):
        if self.color == "w": return u'♙'
        else: return u'♟'
   
class Rook(Piece):
    def __repr__(self):
        if self.color == "w": return u'♖'
        else: return u'♜'     
   
class Bishop(Piece):
    def __repr__(self):
        if self.color == "w": return u'♗'
        else: return u'♝'     
     
        
def valid_move(board, piece, row, col):
        if row < 0 or row > 7 or col < 0 or col > 7: #Out of Bounds
            return False
        elif board[row][col] == "": #Move into empty space.
            return True
        elif board[row][col].color != piece.color: #Capture
            return True
        else:
            return False
