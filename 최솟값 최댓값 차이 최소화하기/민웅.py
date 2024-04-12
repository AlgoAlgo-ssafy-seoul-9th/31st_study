import sys
input = sys.stdin.readline

def bt(r, v, M, m, columns):
    global ans

    if r == N:
        if (M - m) < ans:
            ans = (M - m)
        return

    for i in range(N):
        if i not in columns:
            tmp = field[r][i]
            v[r][i] = 1
            tmp_M = M
            tmp_m = m
            if M < tmp:
                tmp_M = tmp
            if m > tmp:
                tmp_m = tmp
            columns.append(i)
            bt(r+1, v, tmp_M, tmp_m, columns)
            columns.pop()
            v[r][i] = 0



N = int(input())

field = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
ans = float('inf')

bt(0, visited, 0, 10001, [])

print(ans)