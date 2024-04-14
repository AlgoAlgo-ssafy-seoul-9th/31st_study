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
