import sys

input = sys.stdin.readline
INF = float("inf")


def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


n, m, r = map(int, input().split())
items = list(map(int, input().split()))
graph = [[INF] * n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0
for _ in range(r):
    a, b, l = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a][b] = l
    graph[b][a] = l

floyd()
max_items = 0
for i in range(n):
    total = 0
    for j in range(n):
        if graph[i][j] <= m:
            total += items[j]
    max_items = max(max_items, total)

print(max_items)
