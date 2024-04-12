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
