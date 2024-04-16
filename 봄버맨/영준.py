'''

0 ---- 1 ---- 2 ---- 3 ---- 4 ---- 5

(1) 일부칸에 폭탄 설치
(2) 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치
(3) 3초 전에 설치된 폭탄이 모두 폭발
(4) 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치
(5) 이후 3,4 반복

'''
R, C, N = map(int, input().split())
arr = [list(input()) for _ in range(R)]
time = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if arr[i][j]=='O':
            time[i][j] = 3
for t in range(1, N+1):
    if t%2==0:           # 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치
        for i in range(R):
            for j in range(C):
                if arr[i][j]=='.':
                    arr[i][j] = 'O'
                    time[i][j] = t+3
    else:
        for i in range(R):
            for j in range(C):
                if time[i][j]==t:
                    time[i][j] = 0
                    arr[i][j] = '.'
                    for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                        ni, nj = i+di, j+dj
                        if 0<=ni<R and 0<=nj<C and time[ni][nj]!=t:
                            arr[ni][nj] = '.'
                            time[ni][nj] = 0
for x in arr:
    print(''.join(x))
