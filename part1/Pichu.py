#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
P/p = Parakeet = Pawn
R/r = Robin = Rook
B/b = Bluejay = Bishop
Q/q = Quetzal = Queen
K/k = Kingfisher = King - no diagonal movements
N/n = Nighthawk = Knight

Rules: no castling, no check, no en passant.
'''
import Board
import UnitTests
from datetime import datetime
    
if __name__ == "__main__":
    start_time = datetime.now()
 
    player = 'w'
    state = 'RNBQKBNRPPPPPPPP................................pppppppprnbqkbnr'
    time_limit = 10
    
    root = Board.Parse(state)
    print(root)
    
    UnitTests.run_tests()
