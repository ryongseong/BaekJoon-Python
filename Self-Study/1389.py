N, M = map(int, input().split())
graph = [[N] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = []
for r in graph[1:]:
    result.append(sum(r[1:]))

print(result.index(min(result)) + 1)
