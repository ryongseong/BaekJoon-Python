N = int(input())
M = int(input())

INF = float("INF")

graph = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(N + 1):
    graph[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for r in graph[1:]:
    for c in r[1:]:
        print(0 if c == INF else c, end=" ")
    print()
