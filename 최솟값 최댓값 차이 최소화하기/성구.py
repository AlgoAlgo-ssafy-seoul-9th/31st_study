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