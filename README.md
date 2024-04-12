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

```

### [성구](./감시%20피하기/성구.py)

```py

```

### [영준](./감시%20피하기/영준.py)

```py

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

```

### [성구](./봄버맨/성구.py)

```py

```

### [영준](./봄버맨/영준.py)

```py

```

<br/>

## [괄호 추가하기3(GOLD 1)](https://www.acmicpc.net/problem/16639)

### [민웅](./괄호%20추가하기3/민웅.py)

```py

```

### [상미](./괄호%20추가하기3/상미.py)

```py

```

### [성구](./괄호%20추가하기3/성구.py)

```py

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
