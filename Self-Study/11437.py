import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

maxK = 1
while (1 << maxK) <= N:
    maxK += 1

parent = [[-1] * (N + 1) for _ in range(maxK)]
depth = [0] * (N + 1)
visited = [False] * (N + 1)


def bfs(start):
    q = deque([start])
    visited[start] = True
    depth[start] = 0
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                depth[nxt] = depth[cur] + 1
                parent[0][nxt] = cur
                q.append(nxt)


bfs(1)

for k in range(1, maxK):
    for v in range(1, N + 1):
        if parent[k - 1][v] != -1:
            parent[k][v] = parent[k - 1][parent[k - 1][v]]


def lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a

    diff = depth[a] - depth[b]
    for k in range(maxK):
        if diff & (1 << k):
            a = parent[k][a]

    if a == b:
        return a

    for k in reversed(range(maxK)):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]

    return parent[0][a]


Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    print(lca(a, b))
