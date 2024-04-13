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

'''
테스트 케이스 공유

6
X X X X X X
S X X X X T
X X X X X X
X X X X X X
X X X X X X
T X X X X S

NO


3
S X X
X X X
X X T

YES

4
S O X T
O X X X
X X X X
X X X X

YES

4
X S X T
X X S X
X X X X
T T T X

YES

5
X X S X X
X X X X X
S X T X S
X X X X X
X X S X X

NO

5
X T X T X
T X S X T
X S S S X
T X S X X
X T X X X

YES

5
X S S S X
T X X S X
X T X S X
X X T X S
X X X T X

Yes

3
S O X
S O X
T O S

NO

4
S S S S
T T T S
S S S S
S S S S

NO

4
T T X S
X X X X
T T X S
X X X X

YES

4
S S X T
X X X X
T T T T 
X X X X

YES

4
S S X T
S S X X
X X X X
T T T T 

YES

4
S O X T
O S O T
X O X X
X T X X

YES

'''