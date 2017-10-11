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

    def moves(self, board):
        moves = []
        for v1 in [-2, 2]:
            for v2 in [-1, 1]:
                moves.append((self.row+v1, self.col+v2))
                moves.append((self.row+v2, self.col+v1))
        
        possible = []
        
        for move in moves:
            if valid_move(board, self, move[0], move[1]): possible.append(((self.row, self.col), move))
        return possible
   
class Rook(Piece):
    def __repr__(self):
        if self.color == "w": return u'♖'
        else: return u'♜'    
        
    def moves(self, board):
        possible = []
        
        #Up
        for u in range(1, 8 - self.row):
            if valid_move(board, self, self.row + u, self.col):
                possible.append(((self.row, self.col), (self.row + u, self.col)))
            else: break
            if board[self.row + u][self.col] != '': break #Stop if we hit a piece.

        #Down
        for u in range(1, self.row):
            if valid_move(board, self, self.row - u, self.col):
                possible.append(((self.row, self.col), (self.row - u, self.col)))
            else: break
            if board[self.row - u][self.col] != '': break #Stop if we hit a piece.
        
        #Right
        for u in range(1, 8 - self.col):
            if valid_move(board, self, self.row, self.col + u):
                possible.append(((self.row, self.col), (self.row, self.col + u)))
            else: break
            if board[self.row][self.col + u] != '': break #Stop if we hit a piece.

        #Left
        for u in range(1, self.col):
            if valid_move(board, self, self.row, self.col - u):
                possible.append(((self.row, self.col), (self.row, self.col - u)))
            else: break
            if board[self.row][self.col - u] != '': break #Stop if we hit a piece.
        
        return possible   
 
class Bishop(Piece):
    def __repr__(self):
        if self.color == "w": return u'♗'
        else: return u'♝'  
        
    def moves(self, board):
        possible = []
        
        #Up/Right
        for u in range(1, min(8 - self.row, 8 - self.col)):
            if valid_move(board, self, self.row + u, self.col + u):
                possible.append(((self.row, self.col), (self.row + u, self.col + u)))
            else: break
            if board[self.row + u][self.col + u] != '': break #Stop if we hit a piece.

        #Up/Left
        for u in range(1, min(8 - self.row, self.col + 1)):
            if valid_move(board, self, self.row + u, self.col - u):
                possible.append(((self.row, self.col), (self.row + u, self.col - u)))
            else: break
            if board[self.row + u][self.col - u] != '': break #Stop if we hit a piece.
        
        #Down/Right
        for u in range(1, min(self.row + 1, 8 - self.col)):
            if valid_move(board, self, self.row - u, self.col + u):
                possible.append(((self.row, self.col), (self.row - u, self.col + u)))
            else: break
            if board[self.row - u][self.col + u] != '': break #Stop if we hit a piece.

        #Down/Left
        for u in range(1, min(self.row + 1, self.col + 1)):
            if valid_move(board, self, self.row - u, self.col - u):
                possible.append(((self.row, self.col), (self.row - u, self.col - u)))
            else: break
            if board[self.row - u][self.col - u] != '': break #Stop if we hit a piece.

        return possible          
        
        
class Queen(Piece):
    def __repr__(self):
        if self.color == "w": return u'♕'
        else: return u'♛'        

class Pawn(Piece):
    def __repr__(self):
        if self.color == "w": return u'♙'
        else: return u'♟'
   
     
        
def valid_move(board, piece, row, col):
        if row < 0 or row > 7 or col < 0 or col > 7: #Out of Bounds
            return False
        elif board[row][col] == "": #Move into empty space.
            return True
        elif board[row][col].color != piece.color: #Capture
            return True
        else:
            return False
