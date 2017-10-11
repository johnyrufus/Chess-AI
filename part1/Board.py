#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Pieces

class PlayBoard:
    def __init__(self, new_state):
        self.state = []
        self.score = 0
        
        for r in range(0, 8):
            row = []
            for c in range(0, 8):
                char = new_state[r*8+c]
                if char == "K": row.append(Pieces.King("w", r, c))
                elif char == "k": row.append(Pieces.King("b", r, c))
                elif char == "P": row.append(Pieces.Pawn("w", r, c))
                elif char == "p": row.append(Pieces.Pawn("b", r, c))
                elif char == "B": row.append(Pieces.Bishop("w", r, c))
                elif char == "b": row.append(Pieces.Bishop("b", r, c))
                elif char == "N": row.append(Pieces.Knight("w", r, c))
                elif char == "n": row.append(Pieces.Knight("b", r, c))
                elif char == "R": row.append(Pieces.Rook("w", r, c))
                elif char == "r": row.append(Pieces.Rook("b", r, c))
                elif char == "Q": row.append(Pieces.Rook("w", r, c))
                elif char == "q": row.append(Pieces.Rook("b", r, c))
                else: row.append("")
            self.state.append(row)
