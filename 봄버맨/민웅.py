# 16918_봄버맨_bomberman
import sys
input = sys.stdin.readline
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

R, C, N = map(int, input().split())

booms = [list(input().strip()) for _ in range(R)]

for n in range(N-1):
    if not n%2:
        for i in range(R):
            for j in range(C):
                if booms[i][j] == '.':
                    booms[i][j] = 'B'
                elif booms[i][j] == 'B':
                    booms[i][j] = 'O'
    elif n%2:
        tmp = [[booms[a][b] for b in range(C)] for a in range(R)]
        visited = [[0] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if booms[i][j] == 'O':
                    visited[i][j] = 1
                    tmp[i][j] = '.'
                    for d in dxy:
                        ni = i + d[0]
                        nj = j + d[1]
                        if 0 <= ni <= R-1 and 0 <= nj <= C-1:
                            if not visited[ni][nj]:
                                visited[ni][nj] = 1
                                tmp[ni][nj] = '.'
        booms = tmp

for line in booms:
    for i in range(C):
        if line[i] != '.':
            print('O', end='')
        else:
            print('.', end='')
    print()