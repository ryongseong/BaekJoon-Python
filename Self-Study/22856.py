import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def inorder1(node):
    global cnt
    visited[node] = 1

    if not visited[graph[node][0]] and graph[node][0] != -1:
        cnt += 1
        inorder1(graph[node][0])
    if not visited[graph[node][1]] and graph[node][1] != -1:
        cnt += 1
        inorder1(graph[node][1])


def inorder2(node):
    global cnt2
    visited[node] = 1

    if not visited[graph[node][1]] and graph[node][1] != -1:
        inorder2(graph[node][1])
        cnt2 += 1


N = int(input())
graph = dict()
cnt = cnt2 = 0
for _ in range(N):
    a, b, c = map(int, input().split())
    graph[a] = [b, c]
visited = [0] * (N + 1)
inorder1(1)
visited = [0] * (N + 1)
inorder2(1)
print(2 * cnt - cnt2)
