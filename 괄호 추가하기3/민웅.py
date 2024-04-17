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
