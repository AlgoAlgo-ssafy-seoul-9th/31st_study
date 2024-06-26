# 31st_study

알고리즘 스터디 31주차

<br/>

# 이번주 스터디 문제

<details markdown="1" open>
<summary>접기/펼치기</summary>

<br/>

## [감시 피하기(GOLD 5)](https://www.acmicpc.net/problem/18428)

### [민웅](./감시%20피하기/민웅.py)

```py
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

```

### [상미](./감시%20피하기/상미.py)

```py
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


```

### [성구](./감시%20피하기/성구.py)

```py
# 18428 감시 피하기
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    classroom = []
    teacher = []
    # input
    # T 인 좌표 뽑아내기 (teacher)
    for i in range(N):
        lines = input().strip().split()
        classroom.append(lines)
        for j in range(N):
            if lines[j] == "T":
                teacher.append((i,j))

    # S를 바라보는 T에서 벽을 놓을 수 있는 후보군 뽑아내기 (candi)
    candi = []
    for i,j in teacher:
        for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
            blank = []
            for k in range(1, N):
                ni, nj = i+di*k, j+dj*k
                if 0 <= ni < N and 0 <= nj < N:
                    if classroom[ni][nj] == "X":
                        blank.append((ni,nj))
                    elif classroom[ni][nj] == "S":
                        # 바로 옆에 있으면 무조건 NO
                        if k == 1:
                            print("NO")
                            return
                        for tu in blank:
                            candi.append(tu)
                        break
                    # 벽이 있거나 다른 T가 있는경우는 체크 안함
                    else:
                        break
                # 범위를 넘어가면 체크 안함
                else:
                    break

    def check(visited):
        arr = []
        # classroom 복사, arguments로 받을 경우 주소값을 받아와 원본도 변경
        for i in range(N):
            arr.append(classroom[i].copy())
        # 벽 설치
        for i in visited:
            arr[candi[i][0]][candi[i][1]] = "O"

        # 검거되는 학생 체크
        for i,j in teacher:
            for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                for k in range(N):
                    ni, nj = i+di*k, j+dj*k
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj]  ==  "S":
                            # 한 명이라도 검거되면 NO
                            return 0
                        if arr[ni][nj] == "O":
                            # 벽인 경우 넘어감
                            break
                    # 범위 밖 체크 NO
                    else:
                        break
        return 1

    def bt(i, visited):
        if len(visited) == 3:
            if check(visited):
                return 1
            else:
                return 0

        tmp = visited.copy()
        # 될 수 있는 경우 모두 체크
        for j in range(i+1, len(candi)):
            tmp.append((j))
            if bt(j, tmp):
                return 1
            tmp.pop()
        return 0

    # 벽 후보군이 3개 이하면 무조건 YES
    if len(candi) <= 3:
        print("YES")
    else:
        for i in range(len(candi)):
            if bt(-1, []):
                print("YES")
                break
        else:
            print("NO")
    return


if __name__ == "__main__":
    main()
```

### [영준](./감시%20피하기/영준.py)

```py
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

```

<br/>

## [봄버맨(SILVER 1)](https://www.acmicpc.net/problem/16918)

### [민웅](./봄버맨/민웅.py)

```py
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
```

### [상미](./봄버맨/상미.py)

```py
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

```

### [성구](./봄버맨/성구.py)

```py
# 16918 봄버맨
import sys
input = sys.stdin.readline


def main():
    R, C, N = map(int, input().split())
    field = [list(input().strip()) for _ in range(R)]

    # 짝수일 때는 모두 폭탄
    if not N % 2:
        for i in range(R):
            print("O" * C)
        return

    # 폭탄 채우기
    def fill_bombs(fields, bombs, now):
        # 자료구조 set을 이용하여 저장
        bombs[now+3] = set()
        for i in range(R):
            for j in range(C):
                if fields[i][j] == ".":
                    bombs[now+3].add((i,j))
                    fields[i][j] = "O"
        return

    # 폭탄 터짐
    def boom(fields, bombs, now):
        # 집합의 discard를 이용하여 없어지는 폭탄 제거
        if now not in bombs:
            return
        for i,j in bombs[now]:
            for di, dj in [(0,0), (0,1), (0,-1), (1,0), (-1,0)]:
                ni,nj = i+di, j+dj
                if 0 <= ni < R and 0 <= nj < C:
                    fields[ni][nj] = "."
                    bombs[now+2].discard((ni,nj))
        return

    # 폭탄 dictionary
    bombs = {}

    # 초기 설정
    bombs[3] = set()
    for i in range(R):
        for j in range(C):
            if field[i][j] == "O":
                bombs[3].add((i,j))


    # t = 1인 경우 while문 돌지 않고 지나감
    t = 2
    while t <= N:
        if t % 2:
            # 홀수 : 폭탄 터트리기
            boom(field, bombs, t)
        else:
            # 짝수 : 3초 뒤에 터질 폭탄 추가
            fill_bombs(field, bombs, t)
        t += 1


    for i in range(R):
        print("".join(field[i]))


    return


if __name__ == "__main__":
    main()



```

### [영준](./봄버맨/영준.py)

```py
'''
# 얼결에 맞춘거라... ^^!
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
```

<br/>

## [괄호 추가하기3(GOLD 1)](https://www.acmicpc.net/problem/16639)

### [민웅](./괄호%20추가하기3/민웅.py)

```py
# 16639_괄호 추가하기3_Add parentheses
import sys
input = sys.stdin.readline

def bt(eq):
    global ans
    try:
        test = int(eq)
        if test > ans:
            ans = test
        return
    except:
        pass

    for i in range(len(eq)):
        if not eq[i].isdigit():
            s, e = i, i+1
            while s > 0 and eq[s-1].isdigit():
                s -= 1

            while e < len(eq) and eq[e].isdigit():
                e += 1

            if s < i and e > i+1:
                try:
                    tmp = eq[:s] + str(eval(eq[s:e])) + eq[e:]
                    # print(tmp)
                    bt(tmp)
                except:
                    continue
    return


N = int(input())
equation = input().strip()
ans = float('-inf')

bt(equation)

print(ans)

```

### [상미](./괄호%20추가하기3/상미.py)

```py

```

### [성구](./괄호%20추가하기3/성구.py)

```py
# 16639 괄호 추가하기 3
# 돌아온 행렬곱셈..
import sys
input = sys.stdin.readline


def main():
    # define
    nums = []
    operator = []

    # input
    N = int(input())
    for s in list(input().strip()):
        if s.isdecimal():
            nums.append(int(s))
        else:
            operator.append(s)

    # length
    maxn = N // 2 + 1
    # dp define
    dp = [[[0,0] for _ in range((maxn))] for _ in range(maxn)]

    # 최대, 최소 구하는 함수
    def get_value(oper,  start, pin, end):
        arr = [
            calculate(oper[pin], dp[start][pin][0], dp[pin+1][end][0]),
            calculate(oper[pin], dp[start][pin][0], dp[pin+1][end][1]),
            calculate(oper[pin], dp[start][pin][1], dp[pin+1][end][0]),
            calculate(oper[pin], dp[start][pin][1], dp[pin+1][end][1])
        ]
        return (max(arr), min(arr))

    # 계산 함수
    def calculate(operator, num1, num2):
        if operator == "*":
            return num1 * num2
        elif operator == "+":
            return num1 + num2
        else:
            return num1 - num2

    # dp 갱신
    for cnt in range(maxn):
        for i in range(maxn-cnt):
            j = i + cnt

            if cnt:         # i != j dp 갱신
                # 초기화, [최대, 최소]
                dp[i][j] = [-9**maxn,9**maxn]
                for p in range(i,j):    # 길이 내 가장 후순위 계산 선택
                    maxv, minv = get_value(operator, i, p, j)
                    # 최대, 최소 갱신
                    dp[i][j] = [max(maxv, dp[i][j][0]), min(minv, dp[i][j][1])]
            else:           # i == j, 같은 수로 초기화
                dp[i][j] = [nums[i], nums[i]]

    # [print(*dp[i]) for i in range(maxn)]
    print(dp[0][-1][0])



if __name__ == "__main__":
    main()

```

### [영준](./괄호%20추가하기3/영준.py)

```py

```

<br/>

</details>

<br/><br/>

# 지난주 스터디 문제

<details markdown="1">
<summary>접기/펼치기</summary>

<br/>

## [최솟값 최댓값 차이 최소화하기](https://www.codetree.ai/problems/minimize-the-difference-between-the-minimum-and-maximum-values/description)

### [민웅](./최솟값%20최댓값%20차이%20최소화하기/민웅.py)

```py
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
```

### [상미](./최솟값%20최댓값%20차이%20최소화하기/상미.py)

```py

```

### [성구](./최솟값%20최댓값%20차이%20최소화하기/성구.py)

```py
import sys
input = sys.stdin.readline


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


def dfs():
    stack = [(0, 10001, 0, [0] *N)] 
    minv = 90001
    while stack:
        i, small, large, visited = stack.pop()
        if i >= N:
            minv = min(minv, large - small)
            continue
        for j in range(N):
            tmp = visited.copy()
            if not tmp[j]:
                tmp[j] = 1
                stack.append((i+1, min(small, arr[i][j]), max(large, arr[i][j]), tmp))
    return minv


print(dfs())

```

### [영준](./최솟값%20최댓값%20차이%20최소화하기/영준.py)

```py


```

<br/>

## [계단수 만들기](https://www.codetree.ai/problems/making-stair-number/description)

### [민웅](./계단수%20만들기/민웅.py)

```py

```

### [상미](./계단수%20만들기/상미.py)

```py

```

### [성구](./계단수%20만들기/성구.py)

```py

```

### [영준](./계단수%20만들기/영준.py)

```py

```

<br/>

## [후위 순회한 결과](https://www.codetree.ai/training-field/home/timer/problems/postorder-traversal-result/description)

### [민웅](./후위%20순회한%20결과/민웅.py)

```py
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def make_tree(preor_s, preor_e, inor_s, inor_e):
    global tree
    if preor_s > preor_e:
        return

    if preor_s == preor_e:
        tree.append(preorder[preor_s])
        return
    root = preorder[preor_s]
    # mid = inorder.index(root) -> 3871ms
    mid = inorder_idx[root]

    left = mid - inor_s
    make_tree(preor_s+1, preor_s+left, inor_s, mid-1)
    make_tree(preor_s+1+left, preor_e, mid+1, inor_e)

    tree.append(root)


N = int(input())

preorder = list(map(int, input().split()))
inorder = list(map(int, input().split()))

# 이 부분 추가 -> 568ms
inorder_idx = {}
for i in range(N):
    inorder_idx[inorder[i]] = i


tree = []
make_tree(0, N-1, 0, N-1)
print(*tree)
```

### [상미](./후위%20순회한%20결과/상미.py)

```py

```

### [성구](./후위%20순회한%20결과/성구.py)

```py
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input())
preorder = tuple(map(int, input().split()))
inorder = tuple(map(int, input().split()))

inindex = {}

for idx, val in enumerate(inorder):
    inindex[val] = idx

def tree(preorder_start, preorder_end, inorder_start, inorder_end):
    if preorder_start > preorder_end:
        return
    
    if preorder_start == preorder_end:
        print(preorder[preorder_start], end = " ")
        return
    
    root = preorder[preorder_start]
    left = inindex[root] - inorder_start
    tree(preorder_start+1, preorder_start+left, inorder_start, inindex[root]-1)
    tree(preorder_start+1+left, preorder_end, inindex[root] + 1, inorder_end)
    print(root, end =" ")
    return


tree(0, N-1, 0, N-1)
```

### [영준](./후위%20순회한%20결과/영준.py)

```py

```

</details>

<br/><br/>

# 알고리즘 설명

<details markdown="1">
<summary>접기/펼치기</summary>

</details>
