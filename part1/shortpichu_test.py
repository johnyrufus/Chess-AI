from shortpichu import get_moves
from shortpichu import play_pichu

test = '...........................K....................................'
p = 'w'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)

test = '........' \
       '........' \
       '..PPP...' \
       '..PKP...' \
       '..PPP...' \
       '........' \
       '........' \
       '........'
p = 'w'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)

test = '........' \
       '........' \
       '...p....' \
       '..pKp...' \
       '...p....' \
       '........' \
       '........' \
       '........'
p = 'w'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)
p = 'b'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)

test = '........' \
       '........' \
       '..ppp...' \
       '..pKp...' \
       '..ppp...' \
       '........' \
       '........' \
       '........'
p = 'w'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)
p = 'b'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)

test = '........' \
       '........' \
       '........' \
       '...N....' \
       '........' \
       '........' \
       '........' \
       '........'
p = 'w'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)

test = '........' \
       '..P.P...' \
       '.P...P..' \
       '...N....' \
       '.P...P..' \
       '..P.P...' \
       '........' \
       '........'
p = 'w'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)

test = '........' \
       '..P.P...' \
       '.P...P..' \
       '...n....' \
       '.P...P..' \
       '..P.P...' \
       '........' \
       '........'
p = 'w'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)
p = 'b'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)

test = '........' \
       '........' \
       '...p....' \
       '..pRp...' \
       '........' \
       '...p....' \
       '........' \
       '........'
p = 'w'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)
p = 'b'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)

test = '........' \
       '........' \
       '...P....' \
       '..PRP...' \
       '...P....' \
       '........' \
       '........' \
       '........'
p = 'w'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)
p = 'b'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)

test = '........' \
       '........' \
       '..p.p...' \
       '...B....' \
       '..p.p...' \
       '........' \
       '........' \
       '........'
p = 'w'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)
p = 'b'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)

test = '........' \
       '........' \
       '..P.P...' \
       '...B....' \
       '..P.P...' \
       '........' \
       '........' \
       '........'
p = 'w'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)
p = 'b'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)

test = '........' \
       '........' \
       '........' \
       '...P....' \
       '........' \
       '........' \
       '........' \
       '........'
p = 'w'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)

test = '........' \
       '........' \
       '........' \
       '...p....' \
       '........' \
       '........' \
       '........' \
       '........'
p = 'b'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)

test = '........' \
       '........' \
       '........' \
       '........' \
       '........' \
       '..PpP...' \
       '...p....' \
       '........'
p = 'w'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)
p = 'b'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)

test = '........' \
       '........' \
       '........' \
       '........' \
       '...P....' \
       '...p....' \
       '........' \
       '........'
p = 'w'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)
p = 'b'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)

test = '........' \
       '...P....' \
       '...P....' \
       '........' \
       '........' \
       '...p....' \
       '...p....' \
       '........'
p = 'w'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)
p = 'b'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)

test = '........' \
       '...P....' \
       '...p....' \
       '........' \
       '........' \
       '...P....' \
       '...p....' \
       '........'
p = 'w'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)
p = 'b'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)

test = '........' \
       '........' \
       '........' \
       '...Q....' \
       '........' \
       '........' \
       '........' \
       '........'
p = 'w'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)

test = '........' \
       '........' \
       '........' \
       '........' \
       '........' \
       '..PpP...' \
       '...p....' \
       '........'
p = 'w'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)
p = 'b'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)

test = '...K....' \
       '.n....Q.' \
       '........' \
       '..PP....' \
       '...k....' \
       '........' \
       '........' \
       '........'
p = 'w'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)
p = 'b'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)

test = 'K.P.Q...' \
       '........' \
       '........' \
       '....p...' \
       '..p.p...' \
       '..pkp...' \
       '..ppp...' \
       '........'
p = 'w'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)
p = 'b'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)

test = 'K.P...B.' \
       '........' \
       '........' \
       '..ppp...' \
       '..pp.P..' \
       '..pkpp..' \
       '..ppp...' \
       '........'
p = 'w'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)
p = 'b'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)

test =   'RNBQKBNR' \
       + 'PPPPPPPP' \
       + '........' \
       + '........' \
       + '........' \
       + '........' \
       + 'pppppppp' \
       + 'rnbqkbnr'
p = 'w'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)
p = 'b'
get_moves([list(test[i:i + 8]) for i in range(0, 64, 8)], str.isupper if p == 'w' else str.islower, str.islower if p == 'w' else str.isupper)

test =   'RNBQKBNR' \
           + 'PPPPPPPP' \
           + '........' \
           + '........' \
           + '........' \
           + '........' \
           + 'pppppppp' \
           + 'rnbqkbnr'
p = 'w'
res = play_pichu([list(test[i:i+8]) for i in range(0, 64, 8)], (str.isupper if p == 'w' else str.islower), (str.islower if p == 'w' else str.isupper))
print('\n'.join([''.join(row) for row in res[1]]))

test = 'R.BQKBNRPPPPPPPPN...............................pppppppprnbqkbnr'
p = 'b'
res = play_pichu([list(test[i:i + 8]) for i in range(0, 64, 8)], (str.isupper if p == 'w' else str.islower), (str.islower if p == 'w' else str.isupper))
print('\n'.join([''.join(row) for row in res[1]]))
print(''.join([''.join(row) for row in res[1]]))

test = 'R.BQKBNRPPPPPPPPN.......................p........ppppppprnbqkbnr'
p = 'w'
res = play_pichu([list(test[i:i + 8]) for i in range(0, 64, 8)], (str.isupper if p == 'w' else str.islower),(str.islower if p == 'w' else str.isupper))
print('\n'.join([''.join(row) for row in res[1]]))
print(''.join([''.join(row) for row in res[1]]))
