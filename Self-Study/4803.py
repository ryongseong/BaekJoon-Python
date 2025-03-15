import sys
from collections import deque

input = sys.stdin.readline


def dfs(start):
    for x in graph[start]:
        if parent[start] == x:
            continue

        if visited[x]:
            return True

        parent[x] = start
        visited[x] = 1

        if dfs(x):
            return True

    return False


case = 1
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    graph = [[] for _ in range(n + 1)]
    parent = [0] * (n + 1)
    visited = [0] * (n + 1)
    cnt = 0

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n + 1):
        if visited[i] == 0:
            parent[i] = i
            visited[i] = 1
            if not dfs(i):
                cnt += 1

    if cnt == 0:
        print(f"Case {case}: No trees.")
    elif cnt == 1:
        print(f"Case {case}: There is one tree.")
    else:
        print(f"Case {case}: A forest of {cnt} trees.")

    case += 1
