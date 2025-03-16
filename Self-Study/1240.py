from collections import deque


def bfs(start, end):
    queue = deque([(start, 0)])
    visited = [0] * (N + 1)
    visited[start] = 1
    while queue:
        v, d = queue.popleft()
        if v == end:
            return d

        for nv, nd in graph[v]:
            if not visited[nv]:
                visited[nv] = True
                queue.append((nv, d + nd))


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
dist = [float("inf") for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

for _ in range(M):
    n1, n2 = map(int, input().split())
    print(bfs(n1, n2))
