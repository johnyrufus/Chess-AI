#!/usr/bin/env python3
import sys, copy, operator

'''
    Extra Credit: 
    This is the entire Pichu program, with a reasonable heuristic using mini max 
    Right now, this counts to 13 lines starting at 14 to 29 and excluding blank lines and the main input method 
    as mentioned in the assignment.
    
    The main idea is simple. For a given board, for each piece of the current player, 
    check if the 64 possible moves are valid, for each valid move, call the minimax at the next depth.
'''

def get_moves(b, f, fop=None): return [[(r,c), (r1,c1)]for r in range(0, 8) for c in range(0, 8) if b[r][c] != '.' and f(b[r][c]) for r1 in range(0, 8) for c1 in range(0, 8) if is_valid(b, r, c, r1, c1, f, b[r][c], 1 if f == str.isupper else -1, (c1-c)//abs(c1-c) if c1-c != 0 else 0, (r1-r)//abs(r1-r) if r1-r != 0 else 0)]

def get_board(b, pos1, pos2): b1 = copy.deepcopy(b); b1[pos2[0]][pos2[1]] = b[pos1[0]][pos1[1]]; b1[pos1[0]][pos1[1]] = '.'; return b1

def is_valid(b, r, c, r1, c1, f, p, s, sc, sr):
    if p.lower() == 'k': return (r != r1 or c != c1) and (b[r1][c1] == '.' or not f(b[r1][c1])) and (abs(r-r1) < 2 and abs(c-c1) < 2 )
    if p.lower() == 'n': return (r != r1 or c != c1) and (b[r1][c1] == '.' or not f(b[r1][c1])) and ((abs(r-r1) == 1 and abs(c-c1) == 2) or (abs(r-r1) == 2 and abs(c-c1) == 1))
    if p.lower() == 'q': return is_valid(b, r, c, r1, c1, f, 'b', s, sc, sr) or is_valid(b, r, c, r1, c1, f, 'r', s, sc, sr)
    if p.lower() == 'p': return (r != r1 or c != c1) and ( (r1 == r+s and c1 == c and b[r1][c1] == '.') or (r1 == r+s and (c1 == c+1 or c1 == c-1) and b[r1][c1] != '.' and not f(b[r1][c1])) )
    if p.lower() == 'b': return (r != r1 or c != c1) and (b[r1][c1] == '.' or not f(b[r1][c1])) and (abs(r1-r) == abs(c1-c)) and (all(map(lambda p: b[p[0]][p[1]] == '.', list(zip(list(range(r+sr, r1, sr)), list(range(c+sc, c1, sc)))))))
    if p.lower() == 'r': return (r != r1 or c != c1) and (b[r1][c1] == '.' or not f(b[r1][c1])) and (r == r1 or c == c1) and (all(map(lambda p: b[p[0]][p[1]] == '.', [(r,y) for y in range(c + sc, c1, sc)])) if r == r1 else all(map(lambda p: b[p[0]][p[1]] == '.', [(x,c) for x in range(r + sr, r1, sr)])))

def mini_max(b, f, fop, fi, d, md):
    if len([1 for r in b for p in r if p.lower() == 'k']) != 2: return [-999, b] if f == fi else [999, b]
    if d > md: return [sum([{'q':9, 'r':5, 'b':3, 'n':3, 'k':0, 'p':1}[p.lower()] for row in b for p in row if p != '.' and fi(p)]) + len([1 for r in b for p in r if p != '.' and fi(p)]) - (len([1 for r in b for p in r if p != '.']) - len([1 for r in b for p in r if p != '.' and fi(p)])), b]
    return (max if f == fi else min)([mini_max(get_board(b, pos[0], pos[1]), fop, f, fi, d + 1, md) for pos in get_moves(b, f)], key=operator.itemgetter(0)) + [b]

if __name__ == "__main__":
    print(''.join([''.join(row) for row in mini_max([list(sys.argv[2][i:i+8]) for i in range(0, 64, 8)], (str.isupper if sys.argv[1] == 'w' else str.islower), (str.islower if sys.argv[1] == 'w' else str.isupper), (str.isupper if sys.argv[1] == 'w' else str.islower), 0, 2)[-2]]))


























