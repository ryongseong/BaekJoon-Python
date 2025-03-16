import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(node):
    visited[node] = 1
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[node] += dfs(next_node)
    return visited[node]


N, R, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(N - 1):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

dfs(R)

for _ in range(Q):
    print(visited[int(input())])
