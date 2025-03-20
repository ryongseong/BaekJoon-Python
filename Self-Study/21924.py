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


N, M = map(int, input().split())
parents = [i for i in range(N + 1)]
edges = []

cost, cnt = 0, 0
for _ in range(M):
    a, b, c = map(int, input().split())
    cost += c
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])

for s, e, w in edges:
    if find(s) != find(e):
        union(s, e)
        cost -= w

for i in range(1, N):
    if i == parents[i]:
        cnt += 1

print(-1 if cnt > 1 else cost)
