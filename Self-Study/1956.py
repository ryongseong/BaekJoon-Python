N, M = map(int, input().split())
INF = int(1e9)
dist = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    s, e, c = map(int, input().split())
    dist[s][e] = c

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

min_cycle = INF
for i in range(1, N + 1):
    min_cycle = min(min_cycle, dist[i][i])

print(min_cycle if min_cycle != INF else -1)
