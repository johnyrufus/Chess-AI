#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:09:00 2017

@author: aduer
"""

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
            if valid_move(board, self, move[0], move[1]): possible.append(move)
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
     
class Knight(Piece):
    def __repr__(self):
        if self.color == "w": return u'♘'
        else: return u'♞'   
