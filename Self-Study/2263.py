import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

nodes = [0] * (n + 1)
for i in range(n):
    nodes[inorder[i]] = i


def preorder(inorder_start, inorder_end, postorder_start, postorder_end):
    if inorder_start > inorder_end or postorder_start > postorder_end:
        return

    root = postorder[postorder_end]

    left_node = nodes[root] - inorder_start
    right_node = inorder_end - nodes[root]

    print(root, end=" ")
    preorder(
        inorder_start,
        inorder_start + left_node - 1,
        postorder_start,
        postorder_start + left_node - 1,
    )
    preorder(
        inorder_end - right_node + 1,
        inorder_end,
        postorder_end - right_node,
        postorder_end - 1,
    )


preorder(0, n - 1, 0, n - 1)
