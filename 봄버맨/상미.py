import sys
input = sys.stdin.readline

R, C, N =  map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(R)]
time = 1

while time < N:
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '.':
                arr[i][j] = time
    time += 1                   # 3번 지문
    
    if time == N:
        break

    bomb = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'O' or arr[i][j] == time-3:
                bomb.append((i, j))
    for bi, bj in bomb:
        arr[bi][bj] = '.'
        if 0 <= bi+1 < R:
            arr[bi+1][bj] = '.'
        if 0 <= bi-1 < R:
            arr[bi-1][bj] = '.'
        if 0 <= bj+1 < C:
            arr[bi][bj+1] = '.'
        if 0 <= bj-1 < C:
            arr[bi][bj-1] = '.'
    time += 1                      # 4번 지문

for i in range(R):
        for j in range(C):
            if arr[i][j] != '.':
                arr[i][j] = 'O'
for x in arr:
    print(''.join(x))
