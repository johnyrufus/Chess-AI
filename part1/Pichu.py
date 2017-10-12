#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
P/p = Parakeet = Pawn
R/r = Robin = Rook
B/b = Bluejay = Bishop
Q/q = Quetzal = Queen
K/k = Kingfisher = King
N/n = Nighthawk = Knight

Rules: no castling, no check, no en passant.
'''
import Board
from datetime import datetime
    
if __name__ == "__main__":
    start_time = datetime.now()
 
    player = 'w'
    state = 'RNBQKBNRPPPPPPPP................................pppppppprnbqkbnr'
    time_limit = 10
    
    root = Board.Parse(state)
    moves = root.getmoves(player)

    print(root)
    print(root.score(player))
    print(moves)
