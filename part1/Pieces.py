#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Piece():
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
        self.pos = (row, col)
        
    def offset(self, r, c):
        return (self.row + r, self.col + c)
    
class King(Piece):
    def __repr__(self):
        if self.color == "w": return u'♔'
        else: return u'♚'
        
    def moves(self, board):
        possible = []
        
        for i in [1, -1]:
            valid, _ = ValidMove(board, self, self.row + i, self.col)
            if valid: possible.append((self.pos, self.offset(i, 0)))
        
            valid, _ = ValidMove(board, self, self.row, self.col + i)
            if valid: possible.append((self.pos, self.offset(0, i)))

        return possible

class Knight(Piece):
    move_r = [-2, -1, -2, 1, 2, -1, 2, 1]
    move_c = [-1, -2, 1, -2, -1, 2, 1, 2]
    
    def __repr__(self):
        if self.color == "w": return u'♘'
        else: return u'♞'   

    def moves(self, board):        
        possible = []
        
        for r, c in zip(self.move_r, self.move_c):
            valid, _ = ValidMove(board, self, self.row + r, self.col + c)
            if valid: possible.append((self.pos, self.offset(r, c)))

        return possible
   
class Rook(Piece):
    def __repr__(self):
        if self.color == "w": return u'♖'
        else: return u'♜'    
        
    def moves(self, board):
        possible = []
        
        for i in [-1, 1]:
            possible += GoInDirection(board, self, i, 0) #Up/Down
            possible += GoInDirection(board, self, 0, i) #Left/Right
        
        return possible   
 
class Bishop(Piece):
    def __repr__(self):
        if self.color == "w": return u'♗'
        else: return u'♝'  
        
    def moves(self, board):
        possible = []
        
        for i in [-1, 1]:
            possible += GoInDirection(board, self, i, i) #DownLeft/UpRight
            possible += GoInDirection(board, self, i, -i) #DownRight/UpLeft
            
        return possible          
        
class Queen(Piece):
    def __repr__(self):
        if self.color == "w": return u'♕'
        else: return u'♛'        
        
    def moves(self, board):
        possible = []
        
        for i in [-1, 1]:
            possible += GoInDirection(board, self, i, 0) #Up/Down
            possible += GoInDirection(board, self, 0, i) #Left/Right
            possible += GoInDirection(board, self, i, i) #DownLeft/UpRight
            possible += GoInDirection(board, self, i, -i) #DownRight/UpLeft
        
        return possible

class Pawn(Piece):
    def __repr__(self):
        if self.color == "w": return u'♙'
        else: return u'♟'
        
    def moves(self, board):
        possible = []
        
        if self.color == "w": step = 1
        else: step = -1
        
        #Forward movement
        valid, cont = ValidMove(board, self, self.row + step, self.col)
        if valid: possible.append((self.pos, (self.row + step, self.col)))
        if valid and cont and ((self.row == 1 and self.color == "w") or (self.row == 6 and self.color == "b")): 
            valid, cont = ValidMove(board, self, self.row + step * 2, self.col)
            if valid: possible.append((self.pos, (self.row + step * 2, self.col)))
            
        #Capture
        valid, cont = ValidMove(board, self, self.row + step, self.col + 1)
        if valid and not cont: possible.append((self.pos, (self.row + step, self.col + 1)))        
            
        valid, cont = ValidMove(board, self, self.row + step, self.col - 1)
        if valid and not cont: possible.append((self.pos, (self.row + step, self.col - 1)))        

        return possible
        
def ValidMove(board, piece, row, col):
    if row < 0 or row > 7 or col < 0 or col > 7: #Out of Bounds
        return False, False
    elif board[row][col] == "": #Move into empty space.
        return True, True
    elif board[row][col].color != piece.color: #Capture
        return True, False
    else:
        return False, False
    
def GoInDirection(board, piece, row, col):
    moves = []
    
    r = row
    c = col
    
    valid, cont = ValidMove(board, piece, piece.row + r, piece.col + c)
    while valid:
        moves.append((piece.pos, piece.offset(r, c)))
        
        if not cont: return moves
        
        r += row
        c += col
        valid, cont = ValidMove(board, piece, piece.row + r, piece.col + c)
    
    return moves
