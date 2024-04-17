def check(N):
    for i in range(N):
        for j in range(N):
            if arr[i][j]=='S':          # 학생이면
                for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:  # 각 방향으로
                    ni, nj = i+di, j+dj
                    while 0<=ni<N and 0<=nj<N: #
                        if arr[ni][nj]=='T':        # 교사면 장애물 위치 바꾸기
                            return False
                        if arr[ni][nj]=='O' or arr[ni][nj]=='S':        # 장애물이면 다른 방향으로
                            break
                        ni += di
                        nj += dj
    return True     # 교사를 만난적 없이 끝나면

def f(N):
    for i in range(len(tmp) - 2):              # 장애물을 설치할 3곳을 고르는 조합
        for j in range(i+1, len(tmp)-1):
            for k in range(j+1, len(tmp)):
                arr[tmp[i][0]][tmp[i][1]] = 'O'
                arr[tmp[j][0]][tmp[j][1]] = 'O'
                arr[tmp[k][0]][tmp[k][1]] = 'O'
                if check(N):
                    return 'YES'
                arr[tmp[i][0]][tmp[i][1]] = 'X'
                arr[tmp[j][0]][tmp[j][1]] = 'X'
                arr[tmp[k][0]][tmp[k][1]] = 'X'
    return 'NO'

N = int(input())
arr = [input().split() for _ in range(N)]
tmp = []
for i in range(N):              # 비어있는 칸 목록
    for j in range(N):
        if arr[i][j]=='X':
            tmp.append((i,j))

print(f(N))
