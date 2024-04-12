# 18428_감시피하기_avoid surveilance
import sys
input = sys.stdin.readline
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def teacher_check(field):
    # visited = [[0]*N for _ in range(N)]
    for t in teachers:
        for d in dxy:
            x = t[0]
            y = t[1]
            while True:
                x = x + d[0]
                y = y + d[1]
                if 0 <= x <= N-1 and 0 <= y <= N-1:
                    if field[x][y] == 'S':
                        return False
                    elif field[x][y] == "O" or field[x][y] == "T":
                        break
                else:
                    break
    return True


def bt(field, x, y, obs_cnt):
    global ans
    if ans == "YES":
        return

    if y == N-1:
        y = 0
        x += 1
    else:
        y += 1

    if x == N and y == 0:
        return

    if obs_cnt == 3:
        tmp = teacher_check(field)
        if tmp:
            ans = 'YES'
        return

    if field[x][y] == "X":
        field[x][y] = 'O'
        bt(field, x, y, obs_cnt+1)
        field[x][y] = "X"
        bt(field, x, y, obs_cnt)
    else:
        bt(field, x, y, obs_cnt)


N = int(input())

field = [list(input().split()) for _ in range(N)]
ans = "NO"
teachers = []
for i in range(N):
    for j in range(N):
        if field[i][j] == 'T':
            teachers.append([i, j])

bt(field, 0, -1, 0)
print(ans)
