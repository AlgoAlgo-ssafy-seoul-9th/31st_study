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
'''
2
1 543


543

'''

'''
def tree(s, e):
    if s >= e:
        return
    # if s==e:
    #     return 
    root = inorder.index(preorder[s])
    left = tree(s, root-1)
    right = tree(root+1, e)
    print(inorder[root], end=" ")

tree(0, N-1)

0 4
root = 1
left (0 0)
{
    1
}
right (2 4)
{
    2 4
    root = 3 // 5
    left (2 2)
    {
        4
    }
    right (3 4)
    {
        3 4
        root = 3 // 5
        left (3 2)
        {

        }
        right (4 4)
        {
            3
        }
        {
            5
        }
    }
}
{
    2
}
'''