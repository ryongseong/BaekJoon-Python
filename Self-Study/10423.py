import sys

input = sys.stdin.readline


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


N, M, K = map(int, input().split())
power_stations = list(map(int, input().split()))
parents = [0] * (N + 1)
min_cost = 0
for i in range(1, N + 1):
    if i in power_stations:
        continue
    parents[i] = i

edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])

for edge in edges:
    u, v, w = edge
    if find(u) != find(v):
        union(u, v)
        min_cost += w

print(min_cost)
