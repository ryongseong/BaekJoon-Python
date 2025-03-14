import sys

input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


N, M = map(int, input().split())
edges = []
parents = [i for i in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

result = 0
e_result = 0

for c, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        result += c
        e_result = c

print(result - e_result)
