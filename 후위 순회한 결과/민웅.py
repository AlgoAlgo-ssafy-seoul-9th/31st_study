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