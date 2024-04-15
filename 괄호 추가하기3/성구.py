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


'''
  i->
j    3   8     7     9      2
   3 3,3 11,11 77,59 68,-13 136,-85
|  8     8,8   56,56 47,-16 94,-88
p  7           7,7   -2,-2  -4,-11
|  9                 9,9    18,18
   2                        2,2

'''