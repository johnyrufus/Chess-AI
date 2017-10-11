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
        moves = []
        for i in [1, -1]:
            moves.append((self.row+i, self.col))
            moves.append((self.row, self.col+i))

        possible = []
        
        for move in moves:
            valid, _ = valid_move(board, self, move[0], move[1])
            if valid: possible.append(((self.row, self.col), move))
        return possible

class Knight(Piece):
    def __repr__(self):
        if self.color == "w": return u'♘'
        else: return u'♞'   

    def moves(self, board):
        moves = []
        for v1 in [-2, 2]:
            for v2 in [-1, 1]:
                moves.append((self.row+v1, self.col+v2))
                moves.append((self.row+v2, self.col+v1))
        
        possible = []
        
        for move in moves:
            valid, _ = valid_move(board, self, move[0], move[1])
            if valid: possible.append(((self.row, self.col), move))
        return possible
   
class Rook(Piece):
    def __repr__(self):
        if self.color == "w": return u'♖'
        else: return u'♜'    
        
    def moves(self, board):
        possible = []
        
        #Up
        for u in range(1, 8 - self.row):
            valid, cont = valid_move(board, self, self.row + u, self.col)
            if valid: possible.append(((self.row, self.col), (self.row + u, self.col)))
            if (not valid) or (not cont): break

        #Down
        for u in range(1, self.row):
            valid, cont = valid_move(board, self, self.row - u, self.col)
            if valid: possible.append(((self.row, self.col), (self.row - u, self.col)))
            if (not valid) or (not cont): break
        
        #Right
        for u in range(1, 8 - self.col):
            valid, cont = valid_move(board, self, self.row, self.col + u)
            if valid: possible.append(((self.row, self.col), (self.row, self.col + u)))
            if (not valid) or (not cont): break

        #Left
        for u in range(1, self.col):
            valid, cont = valid_move(board, self, self.row, self.col - u)
            if valid: possible.append(((self.row, self.col), (self.row, self.col - u)))
            if (not valid) or (not cont): break
        
        return possible   
 
class Bishop(Piece):
    def __repr__(self):
        if self.color == "w": return u'♗'
        else: return u'♝'  
        
    def moves(self, board):
        possible = []
        
        #Up/Right
        for u in range(1, min(8 - self.row, 8 - self.col)):
            valid, cont = valid_move(board, self, self.row + u, self.col + u)
            if valid: possible.append(((self.row, self.col), (self.row + u, self.col + u)))
            if (not valid) or (not cont): break

        #Up/Left
        for u in range(1, min(8 - self.row, self.col + 1)):
            valid, cont = valid_move(board, self, self.row + u, self.col - u)
            if valid: possible.append(((self.row, self.col), (self.row + u, self.col - u)))
            if (not valid) or (not cont): break
        
        #Down/Right
        for u in range(1, min(self.row + 1, 8 - self.col)):
            valid, cont = valid_move(board, self, self.row - u, self.col + u)
            if valid: possible.append(((self.row, self.col), (self.row - u, self.col + u)))
            if (not valid) or (not cont): break

        #Down/Left
        for u in range(1, min(self.row + 1, self.col + 1)):
            valid, cont = valid_move(board, self, self.row - u, self.col - u)
            if valid: possible.append(((self.row, self.col), (self.row - u, self.col - u)))
            if (not valid) or (not cont): break

        return possible          
        
class Queen(Piece):
    def __repr__(self):
        if self.color == "w": return u'♕'
        else: return u'♛'        
        
    def moves(self, board):
        possible = []
        
        #Up/Right
        for u in range(1, min(8 - self.row, 8 - self.col)):
            valid, cont = valid_move(board, self, self.row + u, self.col + u)
            if valid: possible.append(((self.row, self.col), (self.row + u, self.col + u)))
            if (not valid) or (not cont): break

        #Up/Left
        for u in range(1, min(8 - self.row, self.col + 1)):
            valid, cont = valid_move(board, self, self.row + u, self.col - u)
            if valid: possible.append(((self.row, self.col), (self.row + u, self.col - u)))
            if (not valid) or (not cont): break
        
        #Down/Right
        for u in range(1, min(self.row + 1, 8 - self.col)):
            valid, cont = valid_move(board, self, self.row - u, self.col + u)
            if valid: possible.append(((self.row, self.col), (self.row - u, self.col + u)))
            if (not valid) or (not cont): break

        #Down/Left
        for u in range(1, min(self.row + 1, self.col + 1)):
            valid, cont = valid_move(board, self, self.row - u, self.col - u)
            if valid: possible.append(((self.row, self.col), (self.row - u, self.col - u)))
            if (not valid) or (not cont): break

        #Up
        for u in range(1, 8 - self.row):
            valid, cont = valid_move(board, self, self.row + u, self.col)
            if valid: possible.append(((self.row, self.col), (self.row + u, self.col)))
            if (not valid) or (not cont): break

        #Down
        for u in range(1, self.row):
            valid, cont = valid_move(board, self, self.row - u, self.col)
            if valid: possible.append(((self.row, self.col), (self.row - u, self.col)))
            if (not valid) or (not cont): break
        
        #Right
        for u in range(1, 8 - self.col):
            valid, cont = valid_move(board, self, self.row, self.col + u)
            if valid: possible.append(((self.row, self.col), (self.row, self.col + u)))
            if (not valid) or (not cont): break

        #Left
        for u in range(1, self.col):
            valid, cont = valid_move(board, self, self.row, self.col - u)
            if valid: possible.append(((self.row, self.col), (self.row, self.col - u)))
            if (not valid) or (not cont): break        
        
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
        valid, cont = valid_move(board, self, self.row + step, self.col)
        if valid: possible.append(((self.row, self.col), (self.row + step, self.col)))
        if valid and cont and ((self.row == 1 and self.color == "w") or (self.row == 6 and self.color == "b")): 
            valid, cont = valid_move(board, self, self.row + step * 2, self.col)
            if valid: possible.append(((self.row, self.col), (self.row + step * 2, self.col)))
            
        #Capture
        valid, cont = valid_move(board, self, self.row + step, self.col + 1)
        if valid and not cont: possible.append(((self.row, self.col), (self.row + step, self.col + 1)))        
            
        valid, cont = valid_move(board, self, self.row + step, self.col - 1)
        if valid and not cont: possible.append(((self.row, self.col), (self.row + step, self.col - 1)))        

        return possible
        
def valid_move(board, piece, row, col):
    if row < 0 or row > 7 or col < 0 or col > 7: #Out of Bounds
        return False, False
    elif board[row][col] == "": #Move into empty space.
        return True, True
    elif board[row][col].color != piece.color: #Capture
        return True, False
    else:
        return False, False
