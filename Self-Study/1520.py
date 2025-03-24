import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline


directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(r, c):
    if r == m - 1 and c == n - 1:
        return 1

    if dp[r][c] != -1:
        return dp[r][c]

    ways = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < m and 0 <= nc < n and graph[r][c] > graph[nr][nc]:
            ways += dfs(nr, nc)

    dp[r][c] = ways
    return dp[r][c]


m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
print(dfs(0, 0))
