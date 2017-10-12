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
            #Up/Down
            valid, _ = ValidMove(board, self, self.row + i, self.col)
            if valid: possible.append((self.pos, self.offset(i, 0)))
        
            #Left/Right
            valid, _ = ValidMove(board, self, self.row, self.col + i)
            if valid: possible.append((self.pos, self.offset(0, i)))
            
            #Up/Right and Down/Left
            valid, _ = ValidMove(board, self, self.row + i, self.col + i)
            if valid: possible.append((self.pos, self.offset(i, i)))
            
            #Up/Left and Down/Right
            valid, _ = ValidMove(board, self, self.row + i, self.col - i)
            if valid: possible.append((self.pos, self.offset(i, -i)))

        return possible

    def score(self, board):
        return 0

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

    def score(self, board):
        return 3.2
   
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

    def score(self, board):
        return 5.1
 
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
        
    def score(self, board):
        return 3.33

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

    def score(self, board):
        return 8.8

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

    def score(self, board):
        return 1
        
def ValidMove(board, piece, row, col):
    if row < 0 or row > 7 or col < 0 or col > 7: #Out of Bounds
        return False, False
    elif board[row][col] == "": #Move into empty space.
        return True, True
    elif board[row][col].color != piece.color: #Capture
        return True, False
    else:
        return False, False


'''
Takes in a direction represented by row_incr, col_incr, and 
return all possible valid moves that can be made in that direction.
'''
def GoInDirection(board, piece, row_incr, col_incr):
    moves = []

    r_off = row_incr
    c_off = col_incr

    cont = True
    while cont:
        valid, cont = ValidMove(board, piece, piece.row + r_off, piece.col + c_off)
        if valid:
            moves.append((piece.pos, piece.offset(r_off, c_off)))

        r_off += row_incr
        c_off += col_incr

    return moves
