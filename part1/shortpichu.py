#!/usr/bin/env python3
import sys, copy, operator

'''
    Extra Credit: 
    This is the entire Pichu program, with a reasonable heuristic of counting the number of pieces and the value of the 
    pieces and using mini max 
    Right now, this counts to 13 lines starting at 45 to 60 and excluding blank lines and the main input method 
    as mentioned in the assignment.
    
    Liberties taken in counting lines:
    Lines 45, 55 59 are around 300 characters long
    get_board() has a multiline statement
    Excluding the main method line as that is the I/O line, as given in the assignment.
    
    Following the assignment rules strictly this counts to 17 lines.
    
    The main idea is simple. For a given board, for each piece of the current player, 
    check if the 64 possible moves are valid, for each valid move, call the minimax at the next depth.
    
    
    get_moves(b, f): Given a board and a function f representing the current player, returns all possible next state 
    moves. This is done by considering all the 64 possible locations as potential destinations and for each such 
    destination, determine if it is valid for the (current piece,  starting position, destination position) 
    by calling the is_valid function.
    
    is_valid(b, r, c, r1, c1, f, p, s, sc, sr):  given a board b, and initial position r, c and final position r1, c1, 
    with f denoting the current player, p denoting the piece at r,c, determine if the move is valid for each piece type.  
    (s, sc, sr are just calculations done at the outer function level to reduce lines :), 
    s calculates the sign used for pawn movement, 
    sc and sr calculate the sign used by bishop and rook for their movements)
    
    get_board(b, pos1, pos2): given a new board b and initial position and final position, return the board with the move completed.
    
    mini_max(b, f, fop, fi, d, md): the entire minimax set of 3 functions implemented as one function, where b is the board, 
    f is the current player, fop is the opponent player, fi is the initial player, d is the current depth and md is the max depth.
    
    Heuristics used: The evaluation function is a simple one to fit one line, and it looks at the number of pieces on 
    the board and the value for each piece.
    
    Testing Done: shorpichu.py beats the random player at voltorb 5000 easily every time. [but not the one in 5001]

'''

def get_moves(b, f): return [[(r,c), (r1,c1)]for r in range(0, 8) for c in range(0, 8) if b[r][c] != '.' and f(b[r][c]) for r1 in range(0, 8) for c1 in range(0, 8) if is_valid(b, r, c, r1, c1, f, b[r][c], 1 if f == str.isupper else -1, (c1-c)//abs(c1-c) if c1-c != 0 else 0, (r1-r)//abs(r1-r) if r1-r != 0 else 0)]

def get_board(b, pos1, pos2): b[pos2[0]][pos2[1]], b[pos1[0]][pos1[1]] = b[pos1[0]][pos1[1]], '.'; return b

def is_valid(b, r, c, r1, c1, f, p, s, sc, sr):
    if p.lower() == 'k': return (r != r1 or c != c1) and (b[r1][c1] == '.' or not f(b[r1][c1])) and (abs(r-r1) < 2 and abs(c-c1) < 2 )
    if p.lower() == 'n': return (r != r1 or c != c1) and (b[r1][c1] == '.' or not f(b[r1][c1])) and ((abs(r-r1) == 1 and abs(c-c1) == 2) or (abs(r-r1) == 2 and abs(c-c1) == 1))
    if p.lower() == 'q': return is_valid(b, r, c, r1, c1, f, 'b', s, sc, sr) or is_valid(b, r, c, r1, c1, f, 'r', s, sc, sr)
    if p.lower() == 'p': return (r != r1 or c != c1) and ( (r1 == r+s and c1 == c and b[r1][c1] == '.') or (r1 == r+s and (c1 == c+1 or c1 == c-1) and b[r1][c1] != '.' and not f(b[r1][c1])) )
    if p.lower()=='b':return (r != r1 or c != c1) and (b[r1][c1]=='.' or not f(b[r1][c1])) and (abs(r1-r) == abs(c1-c)) and (all(map(lambda p: b[p[0]][p[1]]=='.',list(zip(list(range(r+sr,r1,sr)),list(range(c+sc,c1,sc)))))))
    if p.lower() == 'r': return (r != r1 or c != c1) and (b[r1][c1] == '.' or not f(b[r1][c1])) and (r == r1 or c == c1) and (all(map(lambda p: b[p[0]][p[1]] == '.', [(r,y) for y in range(c + sc, c1, sc)])) if r == r1 else all(map(lambda p: b[p[0]][p[1]] == '.', [(x,c) for x in range(r + sr, r1, sr)])))

def mini_max(b, f, fop, fi, d, md):
    if len([1 for r in b for p in r if p.lower() == 'k']) != 2: return [-999, b] if f == fi else [999, b]
    if d > md: return [sum([{'q':9, 'r':5, 'b':3, 'n':3, 'k':0, 'p':1}[p.lower()] for row in b for p in row if p != '.' and fi(p)]) + len([1 for r in b for p in r if p != '.' and fi(p)]) - (len([1 for r in b for p in r if p != '.']) - len([1 for r in b for p in r if p != '.' and fi(p)])), b]
    return (max if f == fi else min)([mini_max(get_board(copy.deepcopy(b), pos[0], pos[1]), fop, f, fi, d + 1, md) for pos in get_moves(b, f)], key=operator.itemgetter(0)) + [b]

if __name__ == "__main__":
    print(''.join([''.join(row) for row in mini_max([list(sys.argv[2][i:i+8]) for i in range(0, 64, 8)], (str.isupper if sys.argv[1] == 'w' else str.islower), (str.islower if sys.argv[1] == 'w' else str.isupper), (str.isupper if sys.argv[1] == 'w' else str.islower), 0, 2)[-2]]))
