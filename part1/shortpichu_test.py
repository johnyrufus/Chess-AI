from shortpichu import get_moves
from shortpichu import mini_max

test = '........' \
       '........' \
       '........' \
       '...K....' \
       '........' \
       '........' \
       '........' \
       '........'
p = 'w'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 8)

test = '........' \
       '........' \
       '..PPP...' \
       '..PKP...' \
       '..PPP...' \
       '........' \
       '........' \
       '........'
p = 'w'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 3)

test = '........' \
       '........' \
       '...p....' \
       '..pKp...' \
       '...p....' \
       '........' \
       '........' \
       '........'
p = 'w'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 8)
p = 'b'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 3)

test = '........' \
       '........' \
       '..ppp...' \
       '..pKp...' \
       '..ppp...' \
       '........' \
       '........' \
       '........'
p = 'w'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 8)
p = 'b'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 5)

test = '........' \
       '........' \
       '........' \
       '...N....' \
       '........' \
       '........' \
       '........' \
       '........'
p = 'w'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 8)

test = '........' \
       '..P.P...' \
       '.P...P..' \
       '...N....' \
       '.P...P..' \
       '..P.P...' \
       '........' \
       '........'
p = 'w'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 8)

test = '........' \
       '..P.P...' \
       '.P...P..' \
       '...n....' \
       '.P...P..' \
       '..P.P...' \
       '........' \
       '........'
p = 'w'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 8)
p = 'b'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 8)

test = '........' \
       '........' \
       '...p....' \
       '..pRp...' \
       '........' \
       '...p....' \
       '........' \
       '........'
p = 'w'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 5)
p = 'b'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 4)

test = '........' \
       '........' \
       '...P....' \
       '..PRP...' \
       '...P....' \
       '........' \
       '........' \
       '........'
p = 'w'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 3)
p = 'b'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 0)

test = '........' \
       '........' \
       '..p.p...' \
       '...B....' \
       '..p.p...' \
       '........' \
       '........' \
       '........'
p = 'w'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 4)
p = 'b'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 6)

test = '........' \
       '........' \
       '..P.P...' \
       '...B....' \
       '..P.P...' \
       '........' \
       '........' \
       '........'
p = 'w'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 4)
p = 'b'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 0)

test = '........' \
       '........' \
       '........' \
       '...P....' \
       '........' \
       '........' \
       '........' \
       '........'
p = 'w'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 1)

test = '........' \
       '........' \
       '........' \
       '...p....' \
       '........' \
       '........' \
       '........' \
       '........'
p = 'b'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 1)

test = '........' \
       '........' \
       '........' \
       '........' \
       '........' \
       '..PpP...' \
       '...p....' \
       '........'
p = 'w'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 4)
p = 'b'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 3)

test = '........' \
       '........' \
       '........' \
       '........' \
       '...P....' \
       '...p....' \
       '........' \
       '........'
p = 'w'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 0)
p = 'b'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 0)

test = '........' \
       '...P....' \
       '...P....' \
       '........' \
       '........' \
       '...p....' \
       '...p....' \
       '........'
p = 'w'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 1)
p = 'b'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 1)

test = '........' \
       '...P....' \
       '...p....' \
       '........' \
       '........' \
       '...P....' \
       '...p....' \
       '........'
p = 'w'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 0)
p = 'b'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 0)

test = '........' \
       '........' \
       '........' \
       '...Q....' \
       '........' \
       '........' \
       '........' \
       '........'
p = 'w'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 27)

test = '........' \
       '........' \
       '........' \
       '........' \
       '........' \
       '..PpP...' \
       '...p....' \
       '........'
p = 'w'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 4)
p = 'b'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 3)

test = '...K....' \
       '.n....Q.' \
       '........' \
       '..PP....' \
       '...k....' \
       '........' \
       '........' \
       '........'
p = 'w'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 26)
p = 'b'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 12)

test = 'K.P.Q...' \
       '........' \
       '........' \
       '....p...' \
       '..p.p...' \
       '..pkp...' \
       '..ppp...' \
       '........'
p = 'w'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 18)
p = 'b'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 3)

test = 'K.P...B.' \
       '........' \
       '........' \
       '..ppp...' \
       '..pp.P..' \
       '..pkpp..' \
       '..ppp...' \
       '........'
p = 'w'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 9)
p = 'b'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 6)

test =   'RNBQKBNR' \
       + 'PPPPPPPP' \
       + '........' \
       + '........' \
       + '........' \
       + '........' \
       + 'pppppppp' \
       + 'rnbqkbnr'
p = 'w'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 12)
p = 'b'
assert(len(get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower )) == 12)

test =   'RNBQKBNR' \
           + 'PPPPPPPP' \
           + '........' \
           + '........' \
           + '........' \
           + '........' \
           + 'pppppppp' \
           + 'rnbqkbnr'
p = 'w'
res = mini_max([list(test[i:i+8]) for i in range(0, 64, 8)], (str.isupper if p == 'w' else str.islower), (str.islower if p == 'w' else str.isupper), (str.isupper if p == 'w' else str.islower), 0, 2)
assert(''.join([''.join(row) for row in res[-2]]) == 'R.BQKBNRPPPPPPPPN...............................pppppppprnbqkbnr')

test = 'R.BQKBNRPPPPPPPPN...............................pppppppprnbqkbnr'
p = 'b'
res = mini_max([list(test[i:i + 8]) for i in range(0, 64, 8)], (str.isupper if p == 'w' else str.islower), (str.islower if p == 'w' else str.isupper), (str.isupper if p == 'w' else str.islower), 0, 2)
assert(''.join([''.join(row) for row in res[-2]]) == 'R.BQKBNRPPPPPPPPN.......................p........ppppppprnbqkbnr')

test = 'R.BQKBNRPPPPPPPPN.......................p........ppppppprnbqkbnr'
p = 'w'
res = mini_max([list(test[i:i + 8]) for i in range(0, 64, 8)], (str.isupper if p == 'w' else str.islower),(str.islower if p == 'w' else str.isupper), (str.isupper if p == 'w' else str.islower), 0, 2)
assert(''.join([''.join(row) for row in res[-2]]) == '.RBQKBNRPPPPPPPPN.......................p........ppppppprnbqkbnr')
