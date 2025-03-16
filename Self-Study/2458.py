N, M = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1

result = 0
for i in range(1, N + 1):
    rank = 0
    for j in range(1, N + 1):
        rank += graph[i][j] + graph[j][i]
    if rank == N - 1:
        result += 1

print(result)
