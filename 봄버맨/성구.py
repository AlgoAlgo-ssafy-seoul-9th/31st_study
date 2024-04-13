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
    

'''
테스트 케이스
3 4 5
O...
..O.
O...

ans
OO..
OOO.
OO..

설명

1초
O...
..O.
O...

2초
OOOO
OOOO
OOOO

3초
...O
....
...O

4초
OOOO
OOOO
OOOO

5초
OO..
OOO.
OO..

'''