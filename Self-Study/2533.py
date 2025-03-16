import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(node):
    visited[node] = 1
    if len(graph[node]) == 0:
        dp[node] = [0, 1]
    else:
        for x in graph[node]:
            if not visited[x]:
                dfs(x)
                dp[node][1] += min(dp[x][0], dp[x][1])
                dp[node][0] += dp[x][1]
        dp[node][1] += 1


N = int(input())
graph = [[] for _ in range(N + 1)]
dp = [[0, 0] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(1)
print(min(dp[1][0], dp[1][1]))
