#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import abc
from Position import Position


class Piece():
    def __init__(self, color):
        self.color = color

    @abc.abstractmethod
    def moves(self, board, pos):
        return

    @abc.abstractmethod
    def score(self, board, pos):
        return

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.color == other.color
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


class King(Piece):
    def __repr__(self):
        if self.color == "w": return u'♔'
        else: return u'♚'
        
    def moves(self, board, pos):
        possible = []
        
        for i in [1, -1]:
            #Up/Down
            valid, _ = ValidMove(board, self, pos.offset(i, 0))
            if valid: possible.append((pos, pos.offset(i, 0)))
        
            #Left/Right
            valid, _ = ValidMove(board, self, pos.offset(0, i))
            if valid: possible.append((pos, pos.offset(0, i)))
            
            #Up/Right and Down/Left
            valid, _ = ValidMove(board, self, pos.offset(i, i))
            if valid: possible.append((pos, pos.offset(i, i)))
            
            #Up/Left and Down/Right
            valid, _ = ValidMove(board, self, pos.offset(i, -i))
            if valid: possible.append((pos, pos.offset(i, -i)))

        return possible

    def score(self, board, pos):
        return 0

class Knight(Piece):
    move_r = [-2, -1, -2, 1, 2, -1, 2, 1]
    move_c = [-1, -2, 1, -2, -1, 2, 1, 2]
    
    def __repr__(self):
        if self.color == "w": return u'♘'
        else: return u'♞'   

    def moves(self, board, pos):
        possible = []
        
        for r, c in zip(self.move_r, self.move_c):
            valid, _ = ValidMove(board, self, pos.offset(r, c))
            if valid: possible.append((pos, pos.offset(r, c)))

        return possible

    def score(self, board, pos):
        return 3.2
   
class Rook(Piece):
    def __repr__(self):
        if self.color == "w": return u'♖'
        else: return u'♜'    
        
    def moves(self, board, pos):
        possible = []
        
        for i in [-1, 1]:
            possible += GoInDirection(board, self, pos, i, 0) #Up/Down
            possible += GoInDirection(board, self, pos, 0, i) #Left/Right
        
        return possible   

    def score(self, board, pos):
        return 5.1
 
class Bishop(Piece):
    def __repr__(self):
        if self.color == "w": return u'♗'
        else: return u'♝'  
        
    def moves(self, board, pos):
        possible = []
        
        for i in [-1, 1]:
            possible += GoInDirection(board, self, pos, i, i) #DownLeft/UpRight
            possible += GoInDirection(board, self, pos, i, -i) #DownRight/UpLeft
            
        return possible          
        
    def score(self, board, pos):
        return 3.33

class Queen(Piece):
    def __repr__(self):
        if self.color == "w": return u'♕'
        else: return u'♛'        
        
    def moves(self, board, pos):
        possible = []
        
        for i in [-1, 1]:
            possible += GoInDirection(board, self, pos, i, 0) #Up/Down
            possible += GoInDirection(board, self, pos, 0, i) #Left/Right
            possible += GoInDirection(board, self, pos, i, i) #DownLeft/UpRight
            possible += GoInDirection(board, self, pos, i, -i) #DownRight/UpLeft
        
        return possible

    def score(self, board, pos):
        return 8.8

class Pawn(Piece):
    def __repr__(self):
        if self.color == "w": return u'♙'
        else: return u'♟'
        
    def moves(self, board, pos):
        possible = []
        
        if self.color == "w": step = 1
        else: step = -1
        
        #Forward movement
        valid, cont = ValidMove(board, self, pos.offset(step, 0))
        if valid: possible.append((pos, pos.offset(step, 0)))
        if valid and cont and ((pos.row == 1 and self.color == "w") or (pos.row == 6 and self.color == "b")):
            valid, cont = ValidMove(board, self, pos.offset(step * 2, 0))
            if valid: possible.append((pos, pos.offset(step * 2, 0)))
            
        #Capture
        valid, cont = ValidMove(board, self, pos.offset(step, 1))
        if valid and not cont: possible.append((pos, pos.offset(step, 1)))
            
        valid, cont = ValidMove(board, self, pos.offset(step, -1))
        if valid and not cont: possible.append((pos, pos.offset(step, -1)))

        return possible

    def score(self, board, pos):
        return 1


def ValidMove(board, piece, pos):
    if not pos: #Out of Bounds
        return False, False
    elif board[pos.row][pos.col] == "": #Move into empty space.
        return True, True
    elif board[pos.row][pos.col].color != piece.color: #Capture
        return True, False
    else:
        return False, False


'''
Takes in a direction represented by row_incr, col_incr, and starting from Positon pos,
return all possible valid moves that can be made in that direction.
'''
def GoInDirection(board, piece, pos, row_incr, col_incr):
    moves = []

    r_off = row_incr
    c_off = col_incr

    cont = True
    while cont:
        valid, cont = ValidMove(board, piece, pos.offset(r_off, c_off))
        if valid:
            moves.append((pos, pos.offset(r_off, c_off)))

        r_off += row_incr
        c_off += col_incr

    return moves
