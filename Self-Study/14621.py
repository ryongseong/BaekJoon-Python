def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


N, M = map(int, input().split())
parents = [i for i in range(N + 1)]
gender = ["0"] + list(input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])
cost = 0
cnt = 0

for i in range(M):
    u, v, d = edges[i]
    if find(u) != find(v) and gender[u] != gender[v]:
        union(u, v)
        cost += d
        cnt += 1

print(cost if cnt == N - 1 else -1)
