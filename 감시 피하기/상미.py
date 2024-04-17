import sys
input = sys.stdin.readline 
from itertools import combinations

N = int(input())
arr = [list(map(str, input().strip().split())) for _ in range(N)]

stu = []
tea = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'S':
            stu.append((i, j))
        elif arr[i][j] == 'T':
            tea.append((i, j))

def ifBlocked(arr):
    for ti, tj in tea:
        n = 1
        while n < N:
            if 0 <= ti-n < N:
                if arr[ti-n][tj] == 'O':
                    break
                elif arr[ti-n][tj] == 'S':
                    return False
            else:
                break
            n += 1
        n = 1
        while n < N:
            if 0 <= ti+n < N:
                if arr[ti+n][tj] == 'O':
                    break
                elif arr[ti+n][tj] == 'S':
                    return False
            else:
                break
            n += 1
        n = 1
        while n < N:
            if 0 <= tj-n < N:
                if arr[ti][tj-n] == 'O':
                    break
                elif arr[ti][tj-n] == 'S':
                    return False
            else:
                break
            n += 1
        n = 1
        while n < N:
            if 0 <= tj+n < N:
                if arr[ti][tj+n] == 'O':
                    break
                elif arr[ti][tj+n] == 'S':
                    return False
            else:
                break
            n += 1
    return True

Xlst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'X':
            Xlst.append((i, j))
for i in combinations(Xlst, 3):
    for x, y in i:
        arr[x][y] = 'O'
    
    if ifBlocked(arr):
        print('YES')
        break
    else:
        for x, y in i:
            arr[x][y] = 'X'
else:
    print('NO')

