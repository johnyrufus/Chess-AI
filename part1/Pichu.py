
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
import Algorithms
from datetime import datetime
    
if __name__ == "__main__":
    start_time = datetime.now()
 
    player = 'w'
    state =   'RNBQKBNR' \
            + 'PPPPPPPP' \
            + '........' \
            + '........' \
            + '........' \
            + '........' \
            + 'pppppppp' \
            + 'rnbqkbnr'
    time_limit = 10

    root = Board.Parse(state)
    print(root.PrintOut())
    
    
    game = Algorithms.Minimax(root, 'w', 3, -1)
    
    move = game.MiniMaxSearch()
    print(move)
    
    print(root.move(move[0], move[1]).PrintOut())
    print(root.move(move[0], move[1]).score())
