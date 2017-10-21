#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This file contains the logic and scoring functions for each Pichu piece.
Internally, we represented each bird as its equivalent Chess piece, but
for the record, here is how we assigned each bird:

P/p = Parakeet = Pawn
R/r = Robin = Rook
B/b = Bluejay = Bishop
Q/q = Quetzal = Queen
K/k = Kingfisher = King
N/n = Nighthawk = Knight

The first class is Piece which contains some of the basic functions for a
Piece, such as defining its color, testing equivalence, and returning moves.
Each bird then subclasses Piece and overrides some inherited functions, 
specifically moves() and score().

Below the Piece class are the classes for specific kinds of pieces, such as
Kingfisher/King, Nighthawk/Knight, etc. Each piece contains a list of square
values* and overrides __repr__, moves(), and score(). The __repr__ is a 
function to represent each piece as a chess piece from unicode, which makes
viewing board states easier. The moves() function return all possible, legal
moves that the piece can make given its current position. It is assumed that
white parakeets starting on row 2 and black parekeets on row 7 are able to move
two spaces. The score() function returns the piece's point value. For each 
piece, we assumed the following values:
    
Parakeet = Pawn = 100
Robin = Rook = 500
Bluejay = Bishop = 330
Quetzal = Queen = 900
Kingfisher = King = 20000
Nighthawk = Knight = 320

Each piece also contains a square score that varies this score slightly. This
encourage pieces to take more advantageous squares if possible and avoid 
squares that are not as valuable. For example, Quetzals/Queens and 
Nighthawk/Knights are more valuable towards the center of the board. Likewise,
parakeets/pawns become more valuable as they approach the opposite side of the
board and get closer to becoming a promoted Quetzal/Queen.

References:
The values of each piece and square was taken from:
https://chessprogramming.wikispaces.com/Simplified+evaluation+function
'''

import abc
from Position import Position

'''
Parent class Piece. All bird types inherit from this class.
__init__: records the bird's color.
moves(): returns the possible moves for the piece given the board state
         and the bird's color.
score(): returns the value of the piece given a position on a board.
__eq__(): equivalence test when comparing to other pieces.
__ne__(): equivalence test when comparing to other pieces.
'''
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

'''
King/Kingfisher class.
The square values denote the value of each square for the king. The scoring
assumes we're in the midgame rather than early/late game. The encouragement
is to keep the king relatively safe on the back row and out of harms way
towards the corners. Note that the values are considered from the piece's
starting position - so black and white look at the list from the same
perspective (both king's starting square value is 0 rather than 0 and -50).
__repr__(): Returns a unicode string representing a black/white king.
moves(): Returns a list of valid moves where each move represents a tuple of
         the piece's current position and its destination. Kings can move one
         square in any direction that is not occupied by a piece of the same
         color.
score(): Returns the king's value given its position. Kings are assumed to be
         worth 20000. In practice, the king is worth much more as a capture
         is a terminal state resulting in the board state being worth an
         extreme value to encourage capture.
'''
class King(Piece):
    square_values = [[-30,-40,-40,-50,-50,-40,-40,-30], \
                     [-30,-40,-40,-50,-50,-40,-40,-30], \
                     [-30,-40,-40,-50,-50,-40,-40,-30], \
                     [-30,-40,-40,-50,-50,-40,-40,-30], \
                     [-20,-30,-30,-40,-40,-30,-30,-20], \
                     [-10,-20,-20,-20,-20,-20,-20,-10], \
                     [20, 20,  0,  0,  0,  0, 20, 20], \
                     [20, 30, 10,  0,  0, 10, 30, 20]]

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
        if self.color == 'w':
            points = 20000 + self.square_values[7 - pos.row][pos.col]
        else:
            points = -20000 - self.square_values[pos.row][7 - pos.col]

        return points
'''
Knight/Nighthawk class.
The square values denote the value of each square for a knight. The 
encouragement is to keep knights in the relative center of the board where they
are able to attack more freely.
__repr__(): Returns a unicode string representing a black/white knight.
moves(): Returns a list of valid moves where each move represents a tuple of
         the piece's current position and its destination. Knights can move 2
         spaces up/down and then 1 left/right or 2 spaces left/down and then 1
         space up/down. Unlike other pieces, Knights are able to move over
         other pieces. This means we only have to check if the destination
         square is a valid square rather than every intermediate square.
score(): Returns the knights's value given its position. Knights are assumed
         to be worth 320 points.
'''
class Knight(Piece):
    move_r = [-2, -1, -2, 1, 2, -1, 2, 1]
    move_c = [-1, -2, 1, -2, -1, 2, 1, 2]

    square_values = [[-50,-40,-30,-30,-30,-30,-40,-50], \
                     [-40,-20,  0,  0,  0,  0,-20,-40], \
                     [-30,  0, 10, 15, 15, 10,  0,-30], \
                     [-30,  5, 15, 20, 20, 15,  5,-30], \
                     [-30,  0, 15, 20, 20, 15,  0,-30], \
                     [-30,  5, 10, 15, 15, 10,  5,-30], \
                     [-40,-20,  0,  5,  5,  0,-20,-40], \
                     [-50,-40,-30,-30,-30,-30,-40,-50]]
    
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
        if self.color == 'w':
            points = 320 + self.square_values[7 - pos.row][pos.col]
        else:
            points = -320 - self.square_values[pos.row][7 - pos.col]

        return points
'''
Rook/Robin class.
The square values denote the value of each square for a rook. The 
encouragement is to keep rooks centered or towards the enemy's side of the 
board where they can capture unmoved pieces. The encouragement isn't very 
strong as rooks are capable of moving an entire board's width/length.
__repr__(): Returns a unicode string representing a black/white rook.
moves(): Returns a list of valid moves where each move represents a tuple of
         the piece's current position and its destination. Rooks can move 
         up/down/left/right any number of squares until they run into another
         piece. If it's the same color, it must stop the square before. If 
         it's a differnet color, then it can move into that square and capture
         the piece.
score(): Returns the rook's value given its position. Rooks are assumed
         to be worth 500 points.
'''    
class Rook(Piece):
    square_values = [[0,  0,  0,  0,  0,  0,  0,  0], \
                     [5, 10, 10, 10, 10, 10, 10,  5], \
                     [-5,  0,  0,  0,  0,  0,  0, -5], \
                     [-5,  0,  0,  0,  0,  0,  0, -5], \
                     [-5,  0,  0,  0,  0,  0,  0, -5], \
                     [-5,  0,  0,  0,  0,  0,  0, -5], \
                     [-5,  0,  0,  0,  0,  0,  0, -5], \
                     [0,  0,  0,  5,  5,  0,  0,  0]]
    
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
        if self.color == 'w':
            points = 500 + self.square_values[7 - pos.row][pos.col]
        else:
            points = -500 - self.square_values[pos.row][7 - pos.col]
        
        return points
'''
Bishop/Bluejay class.
The square values denote the value of each square for a bishop. The 
encouragement is to keep bishops back and centered.
__repr__(): Returns a unicode string representing a black/white bishop.
moves(): Returns a list of valid moves where each move represents a tuple of
         the piece's current position and its destination. Bishops can move 
         diagonally any number of squares until they run into another
         piece. If it's the same color, it must stop the square before. If 
         it's a differnet color, then it can move into that square and capture
         the piece.
score(): Returns the bishop's value given its position. Rooks are assumed
         to be worth 330 points.
'''        
class Bishop(Piece):
    square_values = [[-20,-10,-10,-10,-10,-10,-10,-20], \
                     [-10,  0,  0,  0,  0,  0,  0,-10], \
                     [-10,  0,  5, 10, 10,  5,  0,-10], \
                     [-10,  5,  5, 10, 10,  5,  5,-10], \
                     [-10,  0, 10, 10, 10, 10,  0,-10], \
                     [-10, 10, 10, 10, 10, 10, 10,-10], \
                     [-10,  5,  0,  0,  0,  0,  5,-10], \
                     [-20,-10,-10,-10,-10,-10,-10,-20]]

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
        if self.color == 'w':
            points = 330 + self.square_values[7 - pos.row][pos.col]
        else:
            points = -330 - self.square_values[pos.row][7 - pos.col]

        return points

'''
Queen/Quetzal class.
The square values denote the value of each square for a queen. The 
encouragement is to keep queens relatively centered on the board and away
from the corners/edges which minimize its movement potential.
__repr__(): Returns a unicode string representing a black/white queen.
moves(): Returns a list of valid moves where each move represents a tuple of
         the piece's current position and its destination. Queen can move 
         in any direction any number of squares until they run into another
         piece. If it's the same color, it must stop the square before. If 
         it's a differnet color, then it can move into that square and capture
         the piece.
score(): Returns the queen's value given its position. Queens are assumed
         to be worth 900 points.
'''        
class Queen(Piece):
    square_values = [[-20,-10,-10, -5, -5,-10,-10,-20], \
                     [-10,  0,  0,  0,  0,  0,  0,-10], \
                     [-10,  0,  5,  5,  5,  5,  0,-10], \
                     [-5,  0,  5,  5,  5,  5,  0, -5], \
                     [0,  0,  5,  5,  5,  5,  0, -5], \
                     [-10,  5,  5,  5,  5,  5,  0,-10], \
                     [-10,  0,  5,  0,  0,  0,  0,-10], \
                     [-20,-10,-10, -5, -5,-10,-10,-20]]    
    
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
        if self.color == 'w':
            points = 900 + self.square_values[7 - pos.row][pos.col]
        else:
            points = -900 - self.square_values[pos.row][7 - pos.col]

        return points

'''
Pawn/parakeet class.
The square values denote the value of each square for a pawn. The scores are
aimed at moving pawns forward towards the opponents side of the board. This
encourages move towards the opposite side where a pawn can be promoted to
a Quetzal/Queen.
__repr__(): Returns a unicode string representing a black/white pawn.
moves(): Returns a list of valid moves where each move represents a tuple of
         the piece's current position and its destination. Pawns are a bit
         tricky when it comes to movement. In the normal case, they can either
         move one square forward into an empty space or one square forward
         and diagonal to capture another piece. If they're in their initial
         starting square, pawns may move two squares forward so long as there
         is no piece in front of it.
score(): Returns the pawn's value given its position. Pawns are assumed
         to be worth 100 points.
''' 
class Pawn(Piece):
    square_values = [[0,  0,  0,  0,  0,  0,  0,  0], \
                     [50, 50, 50, 50, 50, 50, 50, 50], \
                     [10, 10, 20, 30, 30, 20, 10, 10], \
                     [5,  5, 10, 25, 25, 10,  5,  5], \
                     [0,  0,  0, 20, 20,  0,  0,  0], \
                     [5, -5,-10,  0,  0,-10, -5,  5], \
                     [5, 10, 10,-20,-20, 10, 10,  5], \
                     [0,  0,  0,  0,  0,  0,  0,  0]]

    def __repr__(self):
        if self.color == "w": return u'♙'
        else: return u'♟'

    def moves(self, board, pos):
        possible = []
        
        if self.color == "w": step = 1
        else: step = -1
        
        #Forward movement
        valid, cont = ValidMove(board, self, pos.offset(step, 0))
        if valid and cont: # Moving into empty space
            possible.append((pos, pos.offset(step, 0)))
            
            # Opening move, verify if 2 steps can be made, step by step
            # We already know if we can do +2 via continue from the +1 movement...
            if cont and ((pos.row == 1 and self.color == "w") or (pos.row == 6 and self.color == "b")):
                valid, cont = ValidMove(board, self, pos.offset(step * 2, 0))
                if valid and cont : possible.append((pos, pos.offset(step * 2, 0)))
                        
        #Capture
        valid, cont = ValidMove(board, self, pos.offset(step, 1))
        if valid and not cont: possible.append((pos, pos.offset(step, 1)))
            
        valid, cont = ValidMove(board, self, pos.offset(step, -1))
        if valid and not cont: possible.append((pos, pos.offset(step, -1)))

        return possible

    def score(self, board, pos):        
        if self.color == 'w':
            points = 100 + self.square_values[7 - pos.row][pos.col]
        else:
            points = -100 - self.square_values[pos.row][7 - pos.col]
        
        return points

'''
This is a helper function for piece movement. It returns two values:
    Valid: whether or not the piece can move into the proposed square.
    Continue: whether or not the piece has moved into this square by
    capture.
A move can be valid (either the square is empty or the square was captured) and
then continue can be true or false. True if the square was empty and a piece
that can move unlimited squares may continue and false if the square was
captured and a piece that is able to move unlimited squares must stop.
If a move is not valid then continue does not matter and is always false.
'''
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
This is a helper function for pieces that can move an unlimited number of 
squares in a direction (queen, rook, etc.). The function takes in a board,
a piece, its position, and the direction represented by row and column
increments (1 or 0). Starting at the given position, it moves the piece in
the given direction until it cannot move anymore (runs into a border, 
captures a piece, etc.)
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
