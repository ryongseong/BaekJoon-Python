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


N, M, t = map(int, input().split())
parents = [i for i in range(N + 1)]
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])
result = 0

for s, e, w in edges:
    if find(s) != find(e):
        union(s, e)
        result += w

print(result + ((N - 2) * (N - 1) // 2) * t)
